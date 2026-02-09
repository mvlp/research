import { Component, inject } from '@angular/core';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { PerguntaBuilder } from '../../../builders/Pergunta.builder';
import { PerguntaService } from '../../../services/Pergunta.service';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabel } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { DynamicDialogRef } from 'primeng/dynamicdialog';
@Component({
  selector: 'app-pergunta-form',
  imports: [FormsModule, CommonModule, InputTextModule, FloatLabel, ButtonModule, ReactiveFormsModule],
  templateUrl: './contato.component.html',
  styleUrl: './contato.component.css'
})
export class ContatoComponent {
  dialogRef = inject(DynamicDialogRef)
  form: FormGroup = new FormGroup({
    nome: new FormControl("", {
      nonNullable: true,
      validators: [
        Validators.required,
        Validators.minLength(3)
      ]
    }),
    texto: new FormControl('', {
      nonNullable: true,
      validators: [
        Validators.required,
      ]
    }),
    
    email: new FormControl('', {
      nonNullable: true,
      validators: [
        Validators.required,
        Validators.email
      ]
    }),
    assunto: new FormControl('', {
      nonNullable: true,
      validators: [
        Validators.required,
      ]
    }),
    
  })
  cancelar(){
    console.log("CANCELADO");
    this.dialogRef.close({});
  }

  enviarEmail(){
    console.log("precisa implementar");
    this.dialogRef.close({ status: "OK" });
    
  }
  nome:string
  email:string
  assunto:string
  texto:string
  

}
