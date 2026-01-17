import { Builder } from "../shared/interfaces/builder.interface";
import { FormSchemaControl } from "../shared/interfaces/form-schema.interface";
import { IndiceEntity, IndiceModel } from "../entities/Indice.entity";

export class IndiceBuilder implements Builder<IndiceModel, IndiceEntity> {
  id: number;
  nome: string
  data_ini: Date
  data_fim: Date | null

  assign(props: IndiceModel) {
    Object.assign(this, props)
  };

  build() {
    return new IndiceEntity(this, this.id);
  };

  unbuild() {
    return this;
  };

  getFormSchema() {
    return new FormSchemaControl<IndiceModel>({
      id: { defaultValue: 0 },
      nome: { defaultValue: "" },
      data_ini: { defaultValue: new Date() },
      data_fim: { defaultValue: null },
    }).build();
  };

}