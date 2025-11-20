import { Directive, inject, OnInit, Type } from "@angular/core";
import FormService from "../services/form.service";
import { FormControl, FormGroup } from "@angular/forms";
import ModalService, { ModalWidth } from "../services/modal.service";
import { ConfirmationComponent } from "../components/confirmation/confirmation.component";
import ToastService from "../services/toast.service";
import { FormSchema } from "../interfaces/form-schema.interface";
import { RestService } from "../interfaces/rest-service.interface";
import { UserData } from "../Entities/user-data.type";
import { PermissionKeys } from "../Entities/Permissions";
import { PRIME_NG_CONFIG, PrimeNGConfigType } from "primeng/config";

@Directive()
export abstract class BaseListDirective<E extends { id: number }, P = any> implements OnInit {

  protected formService: FormService = inject(FormService);
  protected modalService: ModalService = inject(ModalService);
  protected toastService: ToastService = inject(ToastService);

  abstract service: RestService<E, P>;
  abstract component: Type<any>;
  abstract header: string;
  permissionKey: PermissionKeys;

  values: E[] = [];
  filteredValues: E[] = [];
  loading: boolean;

  modalWidth: ModalWidth = "85%";
  closeOnSave: boolean = true;
  emptyMessage: string = "Nenhum registro encontrado!";

  filterSchema: FormSchema<P>;
  filter: FormGroup<{ [K in keyof P]: FormControl<P[K]> }>;

  userData: UserData | any;
  modalData: any;

  // permissions
  canCreate: boolean = false;
  canUpdate: boolean = false;
  canDelete: boolean = false;

  async onNgOnInit() {}
  async onUpdateUI() {}
  async onPreviousAdd() {}
  async onPreviousSelect() {}
  async filterFn() {}

  ngOnInit() {

    this.userData =  {}

    if(!this.permissionKey) {
      this.canCreate = true;
      this.canUpdate = true;
      this.canDelete = true;
    };

    if(this.permissionKey) {
      this.canCreate = this.userData?.permissions?.[this.permissionKey]?.create || false;
      this.canUpdate = this.userData?.permissions?.[this.permissionKey]?.update || false;
      this.canDelete = this.userData?.permissions?.[this.permissionKey]?.delete || false;
    };

    this.configureFilter();
    this.onNgOnInit();
    this.updateUI();


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
      await this.onUpdateUI();
    }, async err => {
      console.log(err);
      this.toastService.add({ severity: "error", summary: "ERRO!", detail: err.message || "Erro ao buscar registros!" });
      this.loading = false;
      await this.onUpdateUI();
    });
  }

  protected configureFilter() {
    if(!this.filterSchema) return;
    this.filter = this.formService.create(this.filterSchema);
  }

  async onSelect(id: number) {
    if(!this.canUpdate) {
      this.toastService.add({ severity: "error", summary: "ERRO!", detail: "Você não possui permissão para executar esta ação!" });
      return;
    };

    await this.onPreviousSelect();
    this.modalService.open({
      data: { id, closeOnSave: this.closeOnSave, ...this.modalData },
      header: this.header,
      width: this.modalWidth,
      component: this.component,
      onClose: () => this.updateUI(),
    })
  }

  async add() {
    if(!this.canCreate) {
      this.toastService.add({ severity: "error", summary: "ERRO!", detail: "Você não possui permissão para executar esta ação!" });
      return;
    };

    await this.onPreviousAdd();
    this.modalService.open({
      data: { closeOnSave: this.closeOnSave, ...this.modalData },
      header: this.header,
      width: this.modalWidth,
      component: this.component,
      onClose: () => this.updateUI(),
    });
  }

  async delete(event: any, id: string) {
    if(event) event.stopPropagation();

    if(!this.canDelete) {
      this.toastService.add({ severity: "error", summary: "ERRO!", detail: "Você não possui permissão para executar esta ação!" });
      return;
    };

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
            this.toastService.add({ severity: "success", summary: "SUCESSO!", detail: "Registro excluido com sucesso!" });
            this.updateUI();
          }, err => {
            this.toastService.add({ severity: "error", summary: "ERRO!", detail: "Erro ao excluir registro!" });
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
