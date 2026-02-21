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
import { Router } from '@angular/router';
import ModalService from '../../../shared/services/modal.service';
import { ContatoComponent } from '../contato/contato.component';
import { DialogService } from 'primeng/dynamicdialog';
import { MessageService } from 'primeng/api';
@Component({
  selector: 'app-pergunta-form',
  imports: [FormsModule,CommonModule,InputTextModule,FloatLabel, ButtonModule, ReactiveFormsModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  router = inject(Router)
  modalService = inject(ModalService)
  toastService = inject(MessageService)
  goTo(str: string){
    window.open(str, '_blank', 'noopener,noreferrer');
  }
  openContato(){
    this.modalService.open({
      header: "Entrar em contato",
      width: "45%",
      component: ContatoComponent,
      onClose: (res) => {
        if (res.status){
          this.toastService.add({
            severity:'success',
            summary: 'Sucesso',
            detail: 'Feature ainda não implementada'
          })
        }
      },
      
    });
  }
  redirectPublicacoes(){
    this.router.navigate(["publicacoes"])
  }

}
