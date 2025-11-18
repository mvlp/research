import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Router } from "@angular/router";
import { map, Observable } from "rxjs";
import { UserData } from "../../shared/Entities/user-data.type";
import { LocalStorageService } from "../../shared/services/localstorage.service";
import environment from "../../../../environment.dev";
import { BasePermissionSet } from "../../shared/Entities/Permissions";

@Injectable({
  providedIn: "root"
})
export default class AuthenticationService {

  private tokenKey = "authorization";

  constructor (
    private http: HttpClient,
    private storage: LocalStorageService,
    private router: Router,
  ) {}

  signIn(data: { email: string, password: string }): Observable<any> {

    return this.http.post<UserData & { token: string }>(`${environment.base_url}auth/sign-in`, data).pipe(map(res => {
      /* if(!res.permissions) res.permissions = this.getPermissions(); */
      this.storage.set(this.tokenKey, res.token);
      this.storage.set('userId', res.id);
      this.storage.set('user-data', res);
      console.log("USER-DATA", res);
    })) as Observable<any>;
  }

  async signOut(): Promise<void> {
    this.storage.clear();
    this.router.navigate(["sign-in"]);
  }

  async verifyCurrentlyAuth(): Promise<void> {
    const accessToken = this.getToken();
    if(!accessToken) {
      this.storage.clear();
      this.router.navigate(["sign-in"]);
      return;
    };

    this.router.navigate(["dashboard"]);
    // make request to validate token
  }

  isLoggedIn(): boolean {
    let token = this.storage.get(this.tokenKey);
    return !!token;
  }

  getToken(): string | null {
    if (this.isLoggedIn()) {
      const item = localStorage.getItem(this.tokenKey)
      return item? item.slice(1, -1) : null
    }
    return null;
  }

  getUserData(): UserData {
    return this.storage.get('user-data');
  }
  changePassword(data : {recover_password_id: string, email: string, password: string}): Observable<any>{
    return this.http.post<any>(`${environment.base_url}auth/change-password`, data);
  }
  confirmEmail(data : {token: string, email: string}): Observable<any>{
    return this.http.post<any>(`${environment.base_url}auth/confirm-email`, data);
  }
  recoveryPassword(data : {email: string, password: string, confirmPassword: string}): Observable<any>{
    return this.http.post<any>(`${environment.base_url}auth/recovery-password`, data);
  }
  getBasePermission(permissionAccess = true, permissionCreate = true, permissionUpdate = true, permissionDelete = true): BasePermissionSet {
    return { access: true, create: true, update: true, delete: true };
  }

}
