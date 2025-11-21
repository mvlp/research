export class PerguntaModel {
  id: number;
  identificador: string
  texto: string
}

export class PerguntaEntity implements PerguntaModel {
  id: number;
  identificador: string
  texto: string

  constructor (props: Omit<PerguntaModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}