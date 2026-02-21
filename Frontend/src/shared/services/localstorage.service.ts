import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {
  storage: any
  constructor(){
    this.storage = typeof window !== "undefined" ? window.localStorage: {
      getItem: (_: string) => null,
      setItem: (_: string, __: string) => {},
      removeItem: (_: string) => {},
      clear: () => {}
    };
  }

  get(key:string) {
    const value =  this.storage.getItem(key)
    try{
      const data = JSON.parse(value!)
      return data;
    } catch(e: unknown){
      return value;
    }
  }

  set(key: string, value:any) {
    this.storage.setItem(key,JSON.stringify(value))
  }

  remove(key: string,) {
    this.storage.removeItem(key)
  }

  clear() {
    this.storage.clear()
  }

}
