import { inject, Inject, Injectable } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpInterceptorFn, HttpHeaders } from '@angular/common/http';
import { catchError, NEVER, Observable } from 'rxjs';
import AuthenticationService from '../services/authentication.service';

export const AuthTokenInterceptor: HttpInterceptorFn = (req, next) => {
  const authToken = inject(AuthenticationService).getToken();

  const authReq = authToken ? req.clone({
    setHeaders: {
      Authorization: `Bearer ${authToken}`,
    },
  }) : req;

  // Se não houver token, continue sem modificar a requisição
  return next(authReq);
}
