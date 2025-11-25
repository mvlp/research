import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabel } from 'primeng/floatlabel';
import { InputTextModule } from 'primeng/inputtext';
import { MultiSelectModule } from 'primeng/multiselect';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { IndiceGrupoEntity } from '../../../entities/IndiceGrupo.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { IndiceGrupoBuilder } from '../../../builders/IndiceGrupo.builder';
import { IndiceGrupoService } from '../../../services/IndiceGrupo.service';
import { IndiceGrupoListComponent } from "../indice-grupo-list-component/indice-grupo-list-component";
import { IndiceListComponent } from "../indice-list-component/indice-list-component";

@Component({
  selector: 'app-indice-grupo-form-component',
  imports: [DatePickerModule, FormsModule, CommonModule, InputTextModule, FloatLabel, ButtonModule, ReactiveFormsModule, MultiSelectModule, IndiceListComponent, IndiceListComponent],
  templateUrl: './indice-grupo-form-component.html',
  styleUrl: './indice-grupo-form-component.css',
})
export class IndiceGrupoFormComponent extends BaseFormDirective<IndiceGrupoEntity>{
  override builder = new IndiceGrupoBuilder;
  override service = inject(IndiceGrupoService)
  

  minDate: Date
    
  override async onNgOnInit(): Promise<void> {
    this.minDate = new Date() // Hoje
  }
}
