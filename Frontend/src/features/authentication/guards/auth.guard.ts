import { inject } from '@angular/core';
import { CanActivateFn, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import AuthenticationService from '../services/authentication.service';
import { PermissionKeys } from '../../shared/Entities/Permissions';

export const ManagerAuthGuard: CanActivateFn = (_, state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree=> {

  const authenticationService = inject(AuthenticationService);
  const router = inject(Router);

  const userData = authenticationService.getUserData();
  const path: string = state.url;
  let canActive: boolean | UrlTree = false;

  canActive = authenticationService.isLoggedIn()? true : router.createUrlTree(["/sign-in"]);

  if(userData?.permissions) {
    console.log("ACTIVATED PATH", path);

    const config: { activeKey: PermissionKeys; paths: string[], redirect?: string }[] = [
    ];

    config.map(permission => {
      if(permission.paths.includes(path)) canActive = userData.permissions[permission.activeKey]?.access? true : router.createUrlTree([ permission.redirect || "/dashboard" ]);
    });

  }

  return canActive;

};

export const ArtistAuthGuard: CanActivateFn = (): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree=> {
  const authenticationService = inject(AuthenticationService);
  const userData = authenticationService.getUserData();
  return authenticationService.isLoggedIn()? true : inject(Router).createUrlTree(["/sign-in"]);
};
