import { Component, OnInit, inject } from '@angular/core';
import { AvatarModule } from 'primeng/avatar';
import { MenuModule } from 'primeng/menu';
import { MenuItem } from 'primeng/api';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { InputGroupModule } from 'primeng/inputgroup';
import { InputGroupAddonModule } from 'primeng/inputgroupaddon';
import { DialogService } from 'primeng/dynamicdialog';
import { DividerModule } from 'primeng/divider';
import { TooltipModule } from 'primeng/tooltip';
import ModalService from '../../services/modal.service';
import { UserData } from '../../Entities/user-data.type';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-main-header',
  standalone: true,
  imports: [AvatarModule ,MenuModule, ButtonModule, CommonModule, InputGroupAddonModule, InputGroupModule, DividerModule, TooltipModule],
  providers: [DialogService],
  templateUrl: './main-header.component.html',
  styleUrl: './main-header.component.css'
})
export class MainHeaderComponent implements OnInit {

  userData: UserData | any;

  modalService: ModalService = inject(ModalService);

  ngOnInit(): void {

    this.items = [
      { label: 'Configurações', icon: 'pi pi-cog', command: () => {
      } },
      { separator: true },
      /* { separator: true },
      { label: 'Auditoria', route: '', icon: 'fa-regular fa-file-lines' }, */
    ];

    this.itemsNavigation = [
    ];
  }

  logOut() {
  }

  items: MenuItem[] = [];

  itemsNavigation: MenuItem[] = [];


}
