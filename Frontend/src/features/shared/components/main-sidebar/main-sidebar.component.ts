import { CommonModule } from '@angular/common';
import { Component, Input, OnInit, inject } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { PanelMenuModule } from 'primeng/panelmenu';
import { TooltipModule } from 'primeng/tooltip';
import { Router, RouterLink } from '@angular/router';
import AuthenticationService from '../../../authentication/services/authentication.service';
import { UserData } from '../../Entities/user-data.type';

@Component({
  selector: 'app-main-sidebar',
  standalone: true,
  imports: [PanelMenuModule,RouterLink,CommonModule,TooltipModule],
  templateUrl: './main-sidebar.component.html',
  styleUrl: './main-sidebar.component.css'
})
export class MainSidebarComponent implements OnInit {

  router = inject(Router);
  authenticationService: AuthenticationService = inject(AuthenticationService);
  items: Array<MenuItem>;

  userData: UserData;

  @Input() collapsed: Boolean = false;

  async ngOnInit() {

    this.userData = this.authenticationService.getUserData();

    this.items = [
    ];

  }

  checkActiveSegment(segment: string) {
    return this.router.url.includes(segment);
  }

}



