export class DimensaoModel {
    id: number;
    idIndice: number
    sigla: string
    perguntas: Array<{
      id_pergunta: string,
      peso: number
    }> 
}

export class DimensaoEntity implements DimensaoModel {
    id: number;
    idIndice: number
    sigla: string
    perguntas: Array<{
      id_pergunta: string,
      peso: number
    }> 

  constructor (props: Omit<DimensaoModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}