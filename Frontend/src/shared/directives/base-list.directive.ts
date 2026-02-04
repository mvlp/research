import { ChangeDetectorRef, Directive, inject, OnInit, Type } from "@angular/core";
import FormService from "../services/form.service";
import { FormControl, FormGroup } from "@angular/forms";
import ModalService from "../services/modal.service";
import { ConfirmationComponent } from "../components/confirmation/confirmation.component";
import { FormSchema } from "../interfaces/form-schema.interface";
import { RestService } from "../interfaces/rest-service.interface";
import { UserData } from "../Entities/user-data.type";

@Directive()
export abstract class BaseListDirective<E extends { id: any }, P = any> implements OnInit {

  protected formService: FormService = inject(FormService);
  protected modalService: ModalService = inject(ModalService);
  protected cdr = inject(ChangeDetectorRef)

  abstract service: RestService<E, P>;
  abstract component: Type<any>;
  abstract header: string;

  values: E[] = [];
  filteredValues: E[] = [];
  loading: boolean;

  modalWidth: string = "85%";
  closeOnSave: boolean = true;
  emptyMessage: string = "Nenhum registro encontrado!";

  filterSchema: FormSchema<P>;
  filter: FormGroup<{ [K in keyof P]: FormControl<P[K]> }>;

  userData: UserData | any;
  modalData: any;

  async onNgOnInit() {}
  async onUpdateUI() {}
  async onPreviousAdd() {}
  async onPreviousSelect() {}
  async filterFn() {}

  async ngOnInit() {

    this.userData =  {}
    await this.configureFilter();
    await this.onNgOnInit();
    await this.updateUI();


  }

  async updateUI() {
    this.loading = true;
    if(this.filter) console.log("FILTERS", this.filter.value);
    await this.service.getByFilters(this.filter?.value as any || {}).subscribe(async res => {
      console.log("DATA", res);
      this.values = res;
      this.filteredValues = res;
      await this.filterFn();
      this.loading = false;
      this.cdr.markForCheck();

      await this.onUpdateUI();
    }, async err => {
      console.log(err);
      this.loading = false;
      await this.onUpdateUI();
      this.cdr.reattach();

    });
  }

  protected configureFilter() {
    if(!this.filterSchema) return;
    this.filter = this.formService.create(this.filterSchema);
  }

  async onSelect(id: any) {
    await this.onPreviousSelect();
    this.modalService.open({
      data: { id, closeOnSave: this.closeOnSave, ...this.modalData },
      header: this.header,
      width: this.modalWidth,
      component: this.component,
      onClose: () => {
        this.cdr.markForCheck()
        this.updateUI()
      },
    })
  }

  async add() {

    await this.onPreviousAdd();
    this.modalService.open({
      data: { closeOnSave: this.closeOnSave, ...this.modalData },
      header: this.header,
      width: this.modalWidth,
      component: this.component,
      onClose: () => {
        this.cdr.markForCheck()
        this.updateUI()
      },
    });
  }

  async deleteRegistry(event: any, id: any) {
    if(event) event.stopPropagation();

    this.modalService.open({
      header: `Deseja excluir este item?`,
      width: "35%",
      component: ConfirmationComponent,
      data: {
        severity: "danger",
      },
      onClose: (res) => {
        if(res?.status === "OK") {
          this.loading = true;
          this.service.delete(id).subscribe(() => {
            this.updateUI();
          }, err => {
            this.loading = false;
            console.log(err);
          });
        }
      },
    });
  }

  applyFilters() {
    if(!this.filter) return;
    this.updateUI();
  }

  clearFilters() {
    if(!this.filter) return;
    this.configureFilter();
    this.updateUI();
  }

}
