import { CommonModule } from '@angular/common';
import { Component, inject, Type } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { MultiSelectModule } from 'primeng/multiselect';
import { TableModule } from 'primeng/table';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { IndiceEntity } from '../../../entities/Indice.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { IndiceService } from '../../../services/indice.service';
import { IndiceFormComponent } from '../indice-form-component/indice-form-component';

@Component({
  selector: 'app-Dimensao-grupo-list-component',
  imports: [FormsModule, ReactiveFormsModule, CommonModule, CommonModule, TableModule, ButtonModule, TableHeaderComponent, MultiSelectModule],
  templateUrl: './indice-list-component.html',
})
export class IndiceListComponent extends BaseListDirective<IndiceEntity>{
  override service = inject(IndiceService)
  override component = IndiceFormComponent
  override header = "Índice"
  override modalWidth = "45%"

}
