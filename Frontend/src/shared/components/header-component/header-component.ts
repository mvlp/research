import { Component, inject } from '@angular/core';
import { MenuModule } from 'primeng/menu';
import { ButtonModule } from 'primeng/button';
import { MenuItem } from 'primeng/api';
import { FormsModule } from '@angular/forms';
import { PopoverModule } from 'primeng/popover';
import { Router } from '@angular/router';
@Component({
  selector: 'app-header-component',
  imports: [ButtonModule,MenuModule,FormsModule,PopoverModule],
  templateUrl: './header-component.html',
  styleUrl: './header-component.css',
})
export class HeaderComponent {
  router: Router= inject(Router)
  items: MenuItem[] = [{
    label: "Governança",
    items: [
      {
        label: "Perguntas",
        icon: "pi pi-question",
        command: () => {this.router.navigate(["perguntas"])}
      },
      {
        label: "Dimensões",
        icon: "pi pi-chart-bar",
        command: () => {this.router.navigate(["dimensoes"])}
      }

    ]
  }]
}
