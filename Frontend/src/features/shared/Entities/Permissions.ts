
export enum PermissionKeys {
  a,b,c
}

export type BasePermissionSet = {
  access: boolean;
  create: boolean;
  update: boolean;
  delete: boolean;
}
