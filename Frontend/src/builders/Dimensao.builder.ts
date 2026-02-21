import { Builder } from "../shared/interfaces/builder.interface";
import { FormSchemaControl } from "../shared/interfaces/form-schema.interface";
import { DimensaoEntity, DimensaoModel } from "../entities/Dimensao.entity";

export class DimensaoBuilder implements Builder<DimensaoModel, DimensaoEntity> {
  id: number;
  idIndice: number;
  sigla: string
  perguntas: Array<{
    id_pergunta: string,
    peso: number
  }> 

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
      idIndice: { defaultValue: 0 },
      perguntas: { defaultValue: [] },
      sigla: { defaultValue: ""}

    }).build();
  };

}