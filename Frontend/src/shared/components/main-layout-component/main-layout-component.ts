import { Component } from '@angular/core';
import { HeaderComponent } from '../header-component/header-component';
import { RouterOutlet } from "../../../../node_modules/@angular/router/types/_router_module-chunk";

@Component({
  selector: 'app-main-layout-component',
  imports: [HeaderComponent, RouterOutlet],
  templateUrl: './main-layout-component.html',
  styleUrl: './main-layout-component.css',
})
export class MainLayoutComponent {

}
