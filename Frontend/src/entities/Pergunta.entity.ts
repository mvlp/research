export class PerguntaModel {
  id: string;
  texto: string
}

export class PerguntaEntity implements PerguntaModel {
  id: string;
  texto: string

  constructor (props: Omit<PerguntaModel, "id">, id?: string) {
    Object.assign(this, props);
    this.id = id || "";
  }

}