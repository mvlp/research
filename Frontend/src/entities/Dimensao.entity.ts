export class DimensaoModel {
    id: number;
    idGrupo: number
    perguntas: Array<string> 
}

export class DimensaoEntity implements DimensaoModel {
    id: number;
    idGrupo: number
    perguntas: Array<string> 

  constructor (props: Omit<DimensaoModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}