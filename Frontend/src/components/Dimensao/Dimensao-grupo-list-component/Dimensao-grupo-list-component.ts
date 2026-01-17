import { CommonModule } from '@angular/common';
import { Component, inject, Type } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { MultiSelectModule } from 'primeng/multiselect';
import { TableModule } from 'primeng/table';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { DimensaoGrupoEntity } from '../../../entities/DimensaoGrupo.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { DimensaoGrupoService } from '../../../services/DimensaoGrupo.service';
import { DimensaoGrupoFormComponent } from '../Dimensao-grupo-form-component/Dimensao-grupo-form-component';

@Component({
  selector: 'app-Dimensao-grupo-list-component',
  imports: [FormsModule, ReactiveFormsModule, CommonModule, CommonModule, TableModule, ButtonModule, TableHeaderComponent, MultiSelectModule],
  templateUrl: './Dimensao-grupo-list-component.html',
  styleUrl: './Dimensao-grupo-list-component.css',
})
export class DimensaoGrupoListComponent extends BaseListDirective<DimensaoGrupoEntity>{
  override service = inject(DimensaoGrupoService)
  override component = DimensaoGrupoFormComponent
  override header = "Dimensão"

}
