import { Component, inject, OnInit } from '@angular/core';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { PanelMenuModule } from 'primeng/panelmenu';
import { AvatarModule } from 'primeng/avatar';
import { BadgeModule } from 'primeng/badge';
import { RippleModule } from 'primeng/ripple';
import { CommonModule } from '@angular/common';
import { TooltipModule } from 'primeng/tooltip';
import { ToastModule } from 'primeng/toast';
import { MainHeaderComponent } from '../../../features/shared/components/main-header/main-header.component';
import { MainSidebarComponent } from '../../../features/shared/components/main-sidebar/main-sidebar.component';
import { LocalStorageService } from '../../../features/shared/services/localstorage.service';


@Component({
  selector: 'app-main-layout',
  standalone: true,
  imports: [RouterOutlet, PanelMenuModule, AvatarModule, BadgeModule, ToastModule, RippleModule, CommonModule, MainHeaderComponent, TooltipModule, MainSidebarComponent],
  templateUrl: './main-layout.component.html',
  styleUrl: './main-layout.component.css'
})
export class MainLayoutComponent implements OnInit {

  router = inject(Router);
  localStorage = inject(LocalStorageService);
  collapsed: Boolean;

  toogleCollapse() {
    this.collapsed = !this.collapsed
    this.collapsed ? this.localStorage.set('aside_status', 'collapsed') : this.localStorage.set('aside_status', 'expanded');
  };

  ngOnInit(): void {
    this.collapsed = true;
    this.localStorage.set('aside_status', 'collapsed');
  };

}


