import { Builder } from "../shared/interfaces/builder.interface";
import { FormSchemaControl } from "../shared/interfaces/form-schema.interface";
import { IndiceGrupoEntity, IndiceGrupoModel } from "../entities/IndiceGrupo.entity";

export class IndiceGrupoBuilder implements Builder<IndiceGrupoModel, IndiceGrupoEntity> {
  id: number;
  nome: string
  data_ini: Date
  data_fim: Date | null

  assign(props: IndiceGrupoModel) {
    Object.assign(this, props)
  };

  build() {
    return new IndiceGrupoEntity(this, this.id);
  };

  unbuild() {
    return this;
  };

  getFormSchema() {
    return new FormSchemaControl<IndiceGrupoModel>({
      id: { defaultValue: 0 },
      nome: { defaultValue: "" },
      data_ini: { defaultValue: new Date() },
      data_fim: { defaultValue: null },
    }).build();
  };

}