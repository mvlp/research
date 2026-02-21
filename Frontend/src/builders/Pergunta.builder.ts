import { Validators } from "@angular/forms";
import { PerguntaModel, PerguntaEntity } from "../entities/Pergunta.entity";
import { Builder } from "../shared/interfaces/builder.interface";
import { FormSchemaControl } from "../shared/interfaces/form-schema.interface";

export class PerguntaBuilder implements Builder<PerguntaModel, PerguntaEntity> {
  id: string;
  texto: string

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
      id: { defaultValue: "" },
      texto: { defaultValue: "" },
    }).build();
  };

}