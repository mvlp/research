export default class ValidationError {
  constructor(readonly errors: { [key: string]: string; })
  {}
  updateBuilder(builder:any){
    for (const key of Object.keys(this.errors)){
      builder[key].value = '' // reseta o valor
      builder[key].error = this.errors[key] // define o erro
    }
  }
}
