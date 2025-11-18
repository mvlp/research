import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocalStorageService {

  get(key:string) {
    const value =  localStorage.getItem(key)
    try{
      const data = JSON.parse(value!)
      return data;
    } catch(e: unknown){
      return value;
    }
  }

  set(key: string, value:any) {
    localStorage.setItem(key,JSON.stringify(value))
  }

  remove(key: string,) {
    localStorage.removeItem(key)
  }

  clear() {
    localStorage.clear()
  }

}
