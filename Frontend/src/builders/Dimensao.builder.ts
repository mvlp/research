import { Builder } from "../shared/interfaces/builder.interface";
import { FormSchemaControl } from "../shared/interfaces/form-schema.interface";
import { DimensaoEntity, DimensaoModel } from "../entities/Dimensao.entity";

export class DimensaoBuilder implements Builder<DimensaoModel, DimensaoEntity> {
  id: number;
  idGrupo: number;
  perguntas: Array<string> 

  assign(props: DimensaoModel) {
    Object.assign(this, props)
  };

  build() {
    return new DimensaoEntity(this, this.id);
  };

  unbuild() {
    return this;
  };

  getFormSchema() {
    return new FormSchemaControl<DimensaoModel>({
      id: { defaultValue: 0 },
      idGrupo: { defaultValue: 0 },
      perguntas: { defaultValue: [] }
    }).build();
  };

}