export default abstract class BaseEntity{
}

export abstract class BaseBuilder{
  id: string
  clearErrors() {
    for (const item of Object.keys(this)) {
      if (item == "id") continue
      (this as any)[item].error = '';
    }
  }
}
