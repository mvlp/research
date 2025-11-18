import { ValidatorFn } from "@angular/forms";

export type FormSchema<T = any> = {[K in keyof T]: FormSchemaField<T[K]> };

export type FormSchemaField<FV> = {
  defaultValue: FV;
  validators?: ValidatorFn[];
};

export class FormSchemaControl<T> {

  constructor (
    private schema: FormSchema<T>
  ) {}

  build(): FormSchema<T> {
    return this.schema;
  }

}