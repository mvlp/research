export class PerguntaModel {
  id: number;
}

export class PerguntaEntity implements PerguntaModel {
  id: number;

  constructor (props: Omit<PerguntaModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}