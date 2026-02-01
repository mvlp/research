export default class IndiceEmpresaEntity{
    nome: string
    cnpj: string
    dados: Array<{
      ano: number,
      dimensoes: Array<{
        sigla: string
        dado: Array<number>
      }>
    }>
  }
