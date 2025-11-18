import { Component, Inject, OnInit } from '@angular/core';
import { ReactiveFormsModule, UntypedFormControl, UntypedFormGroup, Validators } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabelModule } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import AuthenticationService from '../../services/authentication.service';

@Component({
  standalone: true,
  selector: 'app-sign-in',
  providers: [ AuthenticationService ],
  imports: [ ReactiveFormsModule, RouterLink, InputTextModule, FloatLabelModule, ButtonModule, CommonModule ],
  templateUrl: './sign-in.component.html',
  styleUrl: './sign-in.component.css',
})
export class SignInComponent implements OnInit {

  constructor (
    private authenticationService: AuthenticationService,
  ) {}

  form: UntypedFormGroup;
  formReady: boolean;
  loading: boolean;

  error: string;

  background: string = 'url("./../../../../assets/images/background.jpg")';


  ngOnInit(): void {
    this.initForm();
  }

  initForm() {
    this.form = new UntypedFormGroup({
      email: new UntypedFormControl("", [Validators.required]),
      password: new UntypedFormControl("", [Validators.required]),
    });
    this.formReady = true;
  }

  async onSubmit() {

    if(this.form.invalid) return;

    this.loading = true;
    await this.authenticationService.signIn(this.form.value).subscribe({
      next: () => {
        this.loading = false;
      },
      error: err => {
        console.log(err);
        this.error = err?.error.message;
        this.loading = false;
      },
    });

  }

}
