import { Component, inject } from '@angular/core';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { PerguntaBuilder } from '../../../builders/Pergunta.builder';
import { PerguntaService } from '../../../services/Pergunta.service';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabel } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-pergunta-form',
  imports: [FormsModule,CommonModule,InputTextModule,FloatLabel, ButtonModule, ReactiveFormsModule],
  templateUrl: './projetos.component.html',
  styleUrl: './projetos.component.css'
})
export class ProjetosComponent {
  

}
