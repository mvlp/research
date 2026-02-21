export class IndiceModel {
    id: number;
    nome: string
    data_ini: Date
    data_fim: Date | null
}

export class IndiceEntity implements IndiceModel {
    id: number;
    nome: string
    data_ini: Date
    data_fim: Date | null

  constructor (props: Omit<IndiceModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}