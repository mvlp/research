import { Validators } from "@angular/forms";
import { PerguntaEntity, PerguntaModel } from "../../../features/governanca/entities/Pergunta.entity";
import { Builder } from "../../../features/shared/interfaces/builder.interface";
import { FormSchemaControl } from "../../../features/shared/interfaces/form-schema.interface";

export class PerguntaBuilder implements Builder<PerguntaModel, PerguntaEntity> {
  id: number;

  assign(props: PerguntaModel) {
    Object.assign(this, props)
  };

  build() {
    return new PerguntaEntity(this, this.id);
  };

  unbuild() {
    return this;
  };

  getFormSchema() {
    return new FormSchemaControl<PerguntaModel>({
      id: { defaultValue: 0 },
    }).build();
  };

}