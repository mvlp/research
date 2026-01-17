import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabel } from 'primeng/floatlabel';
import { InputTextModule } from 'primeng/inputtext';
import { MultiSelectModule } from 'primeng/multiselect';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { DimensaoGrupoEntity } from '../../../entities/DimensaoGrupo.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { DimensaoGrupoBuilder } from '../../../builders/DimensaoGrupo.builder';
import { DimensaoGrupoService } from '../../../services/DimensaoGrupo.service';
import { DimensaoGrupoListComponent } from "../Dimensao-grupo-list-component/Dimensao-grupo-list-component";
import { DimensaoListComponent } from "../Dimensao-list-component/Dimensao-list-component";

@Component({
  selector: 'app-Dimensao-grupo-form-component',
  imports: [DatePickerModule, FormsModule, CommonModule, InputTextModule, FloatLabel, ButtonModule, ReactiveFormsModule, MultiSelectModule, DimensaoListComponent, DimensaoListComponent],
  templateUrl: './Dimensao-grupo-form-component.html',
  styleUrl: './Dimensao-grupo-form-component.css',
})
export class DimensaoGrupoFormComponent extends BaseFormDirective<DimensaoGrupoEntity>{
  override builder = new DimensaoGrupoBuilder;
  override service = inject(DimensaoGrupoService)
  

  minDate: Date
    
  override async onNgOnInit(): Promise<void> {
    this.minDate = new Date() // Hoje
  }
}
