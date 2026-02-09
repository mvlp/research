import { Component } from '@angular/core';
import { HeaderComponent } from '../header-component/header-component';
import { RouterOutlet } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { ToastModule } from 'primeng/toast';

@Component({
  selector: 'app-main-layout-component',
  imports: [HeaderComponent, RouterOutlet,ToastModule],
  templateUrl: './main-layout-component.html',
  styleUrl: './main-layout-component.css',
})
export class MainLayoutComponent {

}
