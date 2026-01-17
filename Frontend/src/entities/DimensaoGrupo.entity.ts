export class DimensaoGrupoModel {
    id: number;
    nome: string
    data_ini: Date
    data_fim: Date | null
}

export class DimensaoGrupoEntity implements DimensaoGrupoModel {
    id: number;
    nome: string
    data_ini: Date
    data_fim: Date | null

  constructor (props: Omit<DimensaoGrupoModel, "id">, id?: number) {
    Object.assign(this, props);
    this.id = id || 0;
  }

}