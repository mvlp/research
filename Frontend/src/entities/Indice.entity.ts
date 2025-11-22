export class IndiceModel {
    id: number;
    idGrupo: number
    perguntas: Array<string> 
}

export class IndiceEntity implements IndiceModel {
    id: number;
    idGrupo: number
    perguntas: Array<string> 

  constructor (props: Omit<IndiceModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}