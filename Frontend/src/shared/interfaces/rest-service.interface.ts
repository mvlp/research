import { HttpClient, HttpErrorResponse } from "@angular/common/http";
import { inject } from "@angular/core";
import { catchError, Observable, ObservableInput, throwError } from "rxjs";
import { formatHttpParams } from "../utils/format-http-params.util";
import { handleHttpError } from "../utils/handle-http-errors.util";
export interface RestService<E = any, P = any> {
  get: (id: number) => Observable<E>,
  getByFilters: (params: P) => Observable<E[]>,
  create: (data: E & { id: number }) => Observable<{ id: number }>,
  update: (data: E & { id: number }) => Observable<{ id: number }>,
  delete: (id: number) => Observable<void>,
}
export const environment = { base_url : "http://127.0.0.1:5000/"}

export abstract class BaseRestService<E, P = any> implements RestService<E, P> {

  http: HttpClient = inject(HttpClient);

  abstract route: string;

  get(id: number): Observable<E> {
    return this.http.get<E>(`${environment.base_url}${this.route}/getOne`,{
      params: {id}
    }).pipe(catchError(handleHttpError)) as Observable<E>;
  };

  getByFilters(params: P): Observable<E[]> {
    params = formatHttpParams(params as any);
    return this.http.get<E[]>(`${environment.base_url}${this.route}`, { params: params as any }).pipe(catchError(handleHttpError)) as Observable<E[]>;
  };

  create(data: E): Observable<{ id: number }> {
    let dataWithoutId = data as any;
    if ((typeof (data as any).id) !== "string" ){
      if(dataWithoutId?.id) delete dataWithoutId.id;
    }
    return this.http.post<{ id: number }>(`${environment.base_url}${this.route}`, dataWithoutId).pipe(catchError(handleHttpError)) as Observable<{ id: number }>;
  };

  update(data: Partial<E> & { id: number }): Observable<{ id: number }> {
    return this.http.put<{ id: number }>(`${environment.base_url}${this.route}`, data).pipe(catchError(handleHttpError)) as Observable<{ id: number }>;
  };

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${environment.base_url}${this.route}/${id}`).pipe(catchError(handleHttpError)) as Observable<any>;
  };

}
