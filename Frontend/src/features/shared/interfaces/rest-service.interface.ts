import { HttpClient, HttpErrorResponse } from "@angular/common/http";
import { inject } from "@angular/core";
import { catchError, Observable, ObservableInput, throwError } from "rxjs";
import environment from "../../../../environment.dev";
import { formatHttpParams } from "../utils/format-http-params.util";
import { handleHttpError } from "../utils/handle-http-errors.util";
export interface RestService<E = any, P = any> {
  get: (id: string) => Observable<E>,
  getByFilters: (params: P) => Observable<E[]>,
  create: (data: E & { id: string }) => Observable<{ id: string }>,
  update: (data: E & { id: string }) => Observable<{ id: string }>,
  delete: (id: string) => Observable<void>,
}

export abstract class BaseRestService<E, P = any> implements RestService<E, P> {

  http: HttpClient = inject(HttpClient);

  abstract route: string;

  get(id: string): Observable<E> {
    return this.http.get<E>(`${environment.base_url}${this.route}/${id}`).pipe(catchError(handleHttpError)) as Observable<E>;
  };

  getByFilters(params: P): Observable<E[]> {
    params = formatHttpParams(params as any);
    return this.http.get<E[]>(`${environment.base_url}${this.route}`, { params: params as any }).pipe(catchError(handleHttpError)) as Observable<E[]>;
  };

  create(data: E): Observable<{ id: string }> {
    const dataWithoutId = data as any;
    if(dataWithoutId?.id) delete dataWithoutId.id;
    return this.http.post<{ id: string }>(`${environment.base_url}${this.route}`, dataWithoutId).pipe(catchError(handleHttpError)) as Observable<{ id: string }>;
  };

  update(data: Partial<E> & { id: string }): Observable<{ id: string }> {
    return this.http.put<{ id: string }>(`${environment.base_url}${this.route}/${data.id}`, data).pipe(catchError(handleHttpError)) as Observable<{ id: string }>;
  };

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`${environment.base_url}${this.route}/${id}`).pipe(catchError(handleHttpError)) as Observable<any>;
  };

}
