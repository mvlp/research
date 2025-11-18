import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule, UntypedFormControl, UntypedFormGroup, Validators } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabelModule } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import AuthenticationService from '../../services/authentication.service';
import { InputOtpModule } from 'primeng/inputotp';
import { PasswordModule } from 'primeng/password';

@Component({
  standalone: true,
  selector: 'app-recovery-password',
  providers: [AuthenticationService],
  imports: [ReactiveFormsModule, InputTextModule, FloatLabelModule, ButtonModule, CommonModule, InputOtpModule, FormsModule, PasswordModule],
  templateUrl: './recovery-password.component.html',
  styleUrl: './recovery-password.component.css',
})
export class RecoveryPasswordComponent implements OnInit {

  constructor (
    private authenticationService: AuthenticationService,
    private router: Router,
  ) {}

  code: string

  form: UntypedFormGroup;
  formChangePassword: UntypedFormGroup;
  formReady: boolean;
  loading: boolean;
  notSended: boolean = true;
  sended: boolean;
  changePassword: boolean;
  finish: boolean;
  recoveryId: string;

  error: string;

  background: string = 'url("./../../../../assets/images/background.jpg")';

  ngOnInit(): void {
    this.initForm();
  }

  initForm() {
    this.form = new UntypedFormGroup({
      email: new UntypedFormControl("", [Validators.required]),
    });
    this.formChangePassword = new UntypedFormGroup({
      email: new UntypedFormControl("", [Validators.required]),
      password: new UntypedFormControl("", [Validators.required]),
      confirmPassword: new UntypedFormControl("", [Validators.required]),
    });
    this.formReady = true;
  }

  async onSubmit() {

    if(this.form.invalid) return;

    this.loading = true;
    await this.authenticationService.recoveryPassword(this.form.value).subscribe({
      next: () => {
        this.loading = false;
        this.notSended = false;
        this.sended = true;
        this.error = "";
      },
      error: (err:any) => {
        console.log(err);
        this.error = err?.error.message;
        this.loading = false;
      },
    });

  }

  async onCompleteCode() {
    this.loading = true;
    await this.authenticationService.confirmEmail({
      email: this.form.value.email,
      token: this.code,
    }).subscribe({
      next: (res:any) => {
        console.log(res);
        this.loading = false;
        this.notSended = false;
        this.sended = false;
        this.changePassword = true;
        this.recoveryId = res.recover_password_id;
        this.formChangePassword.controls["email"].setValue(this.form.value.email);
        this.error = "";
      },
      error: (err:any) => {
        console.log(err);
        this.error = err?.error.message;
        this.loading = false;
      },
    });
  }

  async onSubmitChangePassword() {
    if(this.formChangePassword.invalid) return;

    this.loading = true;
    await this.authenticationService.changePassword({
      recover_password_id: this.recoveryId,
      email: this.formChangePassword.value.email,
      password: this.formChangePassword.value.password,
    }).subscribe({
      next: () => {
        this.loading = false;
        this.notSended = false;
        this.sended = false;
        this.changePassword = false;
        this.sended = false;
        this.finish = true;
        this.error = "";
      },
      error: (err:any) => {
        console.log(err);
        this.error = err?.error.message;
        this.loading = false;
      },
    });
  }

}
