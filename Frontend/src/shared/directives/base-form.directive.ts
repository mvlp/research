import { ChangeDetectorRef, Directive, inject, Input, OnInit } from "@angular/core";
import { FormControl, FormGroup } from "@angular/forms";
import FormService from "../services/form.service";
import { DynamicDialogRef } from "primeng/dynamicdialog";
import { Message } from "primeng/message";
import { Toast } from "primeng/toast";
import { Builder } from "../interfaces/builder.interface";
import { FormSchema } from "../interfaces/form-schema.interface";
import { RestService } from "../interfaces/rest-service.interface";
import { UserData } from "../Entities/user-data.type";

export type Resolve = () => void;
export type Reject = () => void;
@Directive()
export abstract class BaseFormDirective<T extends { id: any } = any, E extends { id: any } = any> implements OnInit {

  @Input() id: any;
  @Input() closeOnSave: boolean;
  @Input() showMessages: boolean = true;

  protected formService: FormService = inject(FormService);
  protected dialogRef: DynamicDialogRef = inject(DynamicDialogRef);
  protected cdr = inject(ChangeDetectorRef)

  abstract builder: Builder<T, E>;
  abstract service: RestService<E>;

  public schema: FormSchema<T>;
  public form: FormGroup<{ [K in keyof T]: FormControl<T[K]> }>;
  public registry: E;
  public formReady: boolean;
  public processing: boolean;

  userData: UserData | any;

  async onNgOnInit() {}
  async onUpdateUI() {}
  async onInsertRegistry() {}
  async onUpdateRegistry() {}
  async onPreviousOnSubmit() {}
  async onPreviousInsertRegistry() {}
  async onPreviousUpdateRegistry() {}
  async setDefaultData() {}
  async formatRegistry() {}
  async onPopulateForm() {}

  async ngOnInit() {

    this.userData = {}
    this.configureForm();
    await this.onNgOnInit();
    await this.updateUI();

  }

  async updateUI() {

    if(!this.id) {
      this.formReady = true;
      await this.onUpdateUI();
      this.setDefaultData();
      return;
    };

    await this.service.get(this.id).subscribe(async res => {
      this.formService.populate(this.form, res);
      console.log("REGISTRY", res);
      this.registry = res;
      await this.onPopulateForm();
      this.formReady = true;
      await this.onUpdateUI();
      this.cdr.markForCheck()
    }, async err => {
      console.log(err);
      this.configureForm();
      this.setDefaultData();
      this.formReady = true;
      await this.onUpdateUI();
      this.cdr.markForCheck()

    });

  };

  private configureForm() {
    this.schema = this.builder.getFormSchema();
    this.form = this.formService.create(this.schema);
  };

  validateSubmit(resolve: Resolve, reject: Reject): void {
    resolve();
  };

  private async getValidateSubmit(): Promise<any> {
    return new Promise((resolve, reject) => {
      this.validateSubmit(() => {
        console.log("SUBMIT VALIDATION RESOLVED");
        resolve(null)
      }, () => {
        console.log("SUBMIT VALIDATION REJECTED");
        reject();
      });
    });
  }

  async onSubmit() {
    await this.onPreviousOnSubmit();
    console.log(`SUBMIT-FORM-VALUE - ${this.form.invalid? "INVALID" : "VALID"}`, this.form.value);
    if(this.form.invalid) return;

    // get submit function validation
    const validationFn = this.getValidateSubmit();
    validationFn.then(async () => {

      this.processing = true;
      this.builder.assign(this.form.value as T);
      this.registry = this.builder.build();
      await this.formatRegistry();

      // form submission
      !this.id? await this.insertRegistry() : await this.updateRegistry();

    }).catch(() => {
      this.processing = false;
    });

  };

  async insertRegistry() {
    this.processing = true;
    await this.onPreviousInsertRegistry();
    console.log("INSERT-REGISTRY-DATA", this.registry);
    await this.service.create(this.registry).subscribe(async res => {
      console.log(res)
      this.id = res.id;
      await this.onInsertRegistry();
      if(this.closeOnSave) this.dialogRef.close({ status: "OK", data: res });
      if(!this.closeOnSave) this.updateUI();
      this.processing = false;
      this.cdr.markForCheck()

    }, (err:any) => {
      console.log(err);
      this.processing = false;
      this.cdr.markForCheck()

    });
  };

  async updateRegistry() {
    this.processing = true;
    await this.onPreviousUpdateRegistry();
    console.log("UPDATE-REGISTRY-DATA", this.registry);
    await this.service.update(this.registry).subscribe(async res => {
      await this.onUpdateRegistry();
      if(this.closeOnSave) this.dialogRef.close({ status: "OK", data: res });
      if(!this.closeOnSave) this.updateUI();
      this.processing = false;
      this.cdr.markForCheck()
    }, (err:any) => {
      console.log(err);
      this.processing = false;
      this.cdr.markForCheck()

    });
  };

  back() {
    this.dialogRef.close();
    this.cdr.markForCheck()

  }

}
