import { CommonModule } from '@angular/common';
import { Component, Input, OnInit, inject } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { PanelMenuModule } from 'primeng/panelmenu';
import { TooltipModule } from 'primeng/tooltip';
import { Router, RouterLink } from '@angular/router';
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
  items: Array<MenuItem>;

  userData: UserData | any;

  @Input() collapsed: Boolean = false;

  async ngOnInit() {

    this.userData = {}

    this.items = [
    ];

  }

  checkActiveSegment(segment: string) {
    return this.router.url.includes(segment);
  }

}



