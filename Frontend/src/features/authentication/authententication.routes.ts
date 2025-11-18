import { Routes } from '@angular/router';
import { SignInComponent } from './views/sign-in/sign-in.component';
import { RecoveryPasswordComponent } from './views/recovery-password/recovery-password.component';

export const routes: Routes = [
  { path: 'sign-in', component: SignInComponent },
  { path: 'recovery-password', component: RecoveryPasswordComponent },
];