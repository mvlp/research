import { FormSchema } from "./form-schema.interface";

export type Builder<P = any, E = any> = P & {
  build: () => E;
  unbuild: (entity: E) => any;
  assign: (props: P) => void;
  getFormSchema: () => FormSchema<P>;
}