import { Builder } from "../shared/interfaces/builder.interface";
import { FormSchemaControl } from "../shared/interfaces/form-schema.interface";
import { DimensaoGrupoEntity, DimensaoGrupoModel } from "../entities/DimensaoGrupo.entity";

export class DimensaoGrupoBuilder implements Builder<DimensaoGrupoModel, DimensaoGrupoEntity> {
  id: number;
  nome: string
  data_ini: Date
  data_fim: Date | null

  assign(props: DimensaoGrupoModel) {
    Object.assign(this, props)
  };

  build() {
    return new DimensaoGrupoEntity(this, this.id);
  };

  unbuild() {
    return this;
  };

  getFormSchema() {
    return new FormSchemaControl<DimensaoGrupoModel>({
      id: { defaultValue: 0 },
      nome: { defaultValue: "" },
      data_ini: { defaultValue: new Date() },
      data_fim: { defaultValue: null },
    }).build();
  };

}