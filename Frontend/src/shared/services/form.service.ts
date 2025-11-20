import { Injectable } from "@angular/core";
import { FormControl, FormGroup, UntypedFormControl } from "@angular/forms";
import { FormSchema, FormSchemaField } from "../interfaces/form-schema.interface";

@Injectable({
  providedIn: "root"
})
export default class FormService {

  create<T>(schema: FormSchema<T>): FormGroup<{ [K in keyof T]: FormControl<T[K]>; }> {
    const form = new FormGroup({}) as any;
    Object.entries(schema).forEach((baseEntry) => {
      let entry = baseEntry as [string, FormSchemaField<T>];
      form.addControl(entry[0], new UntypedFormControl(entry[1].defaultValue, entry[1]?.validators || []));
    });
    return form;
  };

  populate<T>(form: FormGroup, data: {[K in keyof T]?: T[K] }) {
    form.patchValue(data);
  };

}
