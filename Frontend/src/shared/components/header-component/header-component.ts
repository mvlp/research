import { Component, inject } from '@angular/core';
import { MenuModule } from 'primeng/menu';
import { ButtonModule } from 'primeng/button';
import { MenuItem, MessageService } from 'primeng/api';
import { FormsModule } from '@angular/forms';
import { PopoverModule } from 'primeng/popover';
import { Router } from '@angular/router';
import { ContatoComponent } from '../../../components/extras/contato/contato.component';
import ModalService from '../../services/modal.service';
@Component({
  selector: 'app-header-component',
  imports: [ButtonModule,MenuModule,FormsModule,PopoverModule],
  templateUrl: './header-component.html',
  styleUrl: './header-component.css',
})
export class HeaderComponent {
  router: Router= inject(Router)
  modalService = inject(ModalService)
  toastService = inject(MessageService)
  items: MenuItem[] = [{
    label: "Governança",
    items: [
      // {
      //   label: "Perguntas",
      //   icon: "pi pi-question",
      //   command: () => {this.router.navigate(["perguntas"])}
      // },
      {
        label: "Dimensões",
        icon: "pi pi-chart-bar",
        command: () => {this.router.navigate(["dimensoes"])}
      }

    ]
  }]

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
}
