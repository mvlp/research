import { CommonModule } from '@angular/common';
import { Component, inject, Type } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { MultiSelectModule } from 'primeng/multiselect';
import { TableModule } from 'primeng/table';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { IndiceGrupoEntity } from '../../../entities/IndiceGrupo.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { IndiceGrupoService } from '../../../services/IndiceGrupo.service';
import { IndiceGrupoFormComponent } from '../indice-grupo-form-component/indice-grupo-form-component';

@Component({
  selector: 'app-indice-grupo-list-component',
  imports: [FormsModule, ReactiveFormsModule, CommonModule, CommonModule, TableModule, ButtonModule, TableHeaderComponent, MultiSelectModule],
  templateUrl: './indice-grupo-list-component.html',
  styleUrl: './indice-grupo-list-component.css',
})
export class IndiceGrupoListComponent extends BaseListDirective<IndiceGrupoEntity>{
  override service = inject(IndiceGrupoService)
  override component = IndiceGrupoFormComponent
  override header = "Indice"

}
