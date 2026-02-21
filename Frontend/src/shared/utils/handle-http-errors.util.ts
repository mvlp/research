import { HttpErrorResponse } from "@angular/common/http";
import { throwError } from "rxjs";

export function handleHttpError(err: HttpErrorResponse) {
  console.log(err)
  let message = err?.error?.message || "";
  if(message === "Internal server error") message = "Ocorreu um erro inesperado!";
  if(Array.isArray(err.error.message)) {
    message = err.error.message[0].constraints[Object.keys(err.error.message[0].constraints)[0]];
  };
  if(message == "Invalid token"){
    localStorage.clear()
    window.location.href = "sign-in"

  }
  return throwError(() => new Error(message));
}
