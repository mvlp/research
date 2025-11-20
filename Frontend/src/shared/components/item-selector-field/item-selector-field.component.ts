import { CommonModule } from "@angular/common";
import { Component, forwardRef, OnInit, inject, Input, Output, EventEmitter } from "@angular/core";
import { FormsModule, ReactiveFormsModule, NG_VALUE_ACCESSOR } from "@angular/forms";
import { SelectItem } from "primeng/api";
import { ButtonModule } from "primeng/button";
import { DialogService } from "primeng/dynamicdialog";
import { FloatLabelModule } from "primeng/floatlabel";
import { MultiSelectModule } from "primeng/multiselect";
import { BaseRestService } from "../../interfaces/rest-service.interface";
import ModalService from "../../services/modal.service";

type ItemSelector = "a";

@Component({
  standalone: true,
  selector: 'app-item-selector-field',
  imports: [CommonModule, FormsModule, ReactiveFormsModule, MultiSelectModule, FloatLabelModule, ButtonModule],
  templateUrl: './item-selector-field.component.html',
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => ItemSelectorFieldComponent),
      multi: true
    },
  ]
})
export class ItemSelectorFieldComponent implements OnInit {

  protected dialogService: DialogService = inject(DialogService);
  modalService: ModalService = inject(ModalService);

  @Input() selector: ItemSelector = "a";
  @Input() all: boolean = true;
  @Input() allLabel: string = "Todos";
  @Input() label?: string;
  @Input() multiselector: boolean = false;
  @Input() params: any;
  @Input() modalCreate: boolean = true;
  @Input() modalData: any;
  @Input() readOnly: boolean = false;

  @Output() change = new EventEmitter<{ value: any, option: any, item: any }>();
  @Output() onGetOptions = new EventEmitter<SelectItem[]>();

  items: any[] = [];
  options: SelectItem[] = [];
  loading: boolean = false;

  value: any;

  onChange = (value: string) => {};
  onTouched = () => {};

  writeValue(value: any): void {
    this.value = value;
  }

  registerOnChange(fn: (value: string) => void): void {
    this.onChange = fn;
  }

  registerOnTouched(fn: () => void): void {
    this.onTouched = fn;
  }

  ngOnInit() {
    this.getOptions();
  }

  onSelectValue(value: any) {
    if (!this.multiselector) {
      this.value = value;
      this.onChange(this.value);
      this.change.emit({
        value: this.value,
        option: this.options.find(item => item.value === this.value),
        item: this.items.find(item => item?.id === this.value),
      });
      return;
    }

    this.value = value;

    if (value.length === 0) {
      this.value = ["*"];
      this.onChange(this.value);
      return;
    }

    if (value[value.length - 1] === "*") {
      this.value = ["*"];
      this.onChange(this.value);
      return;
    }

    if (value[value.length - 1] !== "*") {
      this.value = value.filter((item: any) => item !== "*");
      this.onChange(this.value);
      return;
    }

    this.onChange(this.value);
  }

  createRegistry() {
    this.modalService.dynamicOpen(this.selector, [], { closeOnSave: true, ...this.modalData }, (res: any) => {
      if (res?.status === "OK") this.onCreateRegistry(res.data);
    });
  }

  async onCreateRegistry(data: any) {
    await this.getOptions();
    if (this.multiselector) this.value.push(data.id);
    if (!this.multiselector) this.value = data.id;
    this.onSelectValue(this.value);
  }

  async getOptions() {
    // placeholder por enquanto
    this.options = [];
    this.items = [];
  }

  formatOptions(items: any[], labelKey: string = "name", valueKey: string = "id"): SelectItem[] {
    const options = items.map(item => ({ label: item[labelKey], value: item[valueKey] }));
    if (this.all) options.unshift({ label: this.allLabel, value: "*" });
    return options;
  }

  getOptionsByService(service: BaseRestService<any>, params: { [key: string]: any } = {}, labelKey: string = "name", valueKey: string = "id") {
    this.loading = true;
    service.getByFilters({ ...params, ...this.params }).subscribe({
      next: (res: any) => {
        this.options = this.formatOptions(res, labelKey, valueKey);
        this.items = res;
        if (this.options.length) this.onGetOptions.emit(this.options);
      },
      error: () => (this.loading = false),
      complete: () => (this.loading = false)
    });
  }
}
