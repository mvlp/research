export class IndiceGrupoModel {
    id: number;
    nome: string
    data_ini: Date
    data_fim: Date | null
}

export class IndiceGrupoEntity implements IndiceGrupoModel {
    id: number;
    nome: string
    data_ini: Date
    data_fim: Date | null

  constructor (props: Omit<IndiceGrupoModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}