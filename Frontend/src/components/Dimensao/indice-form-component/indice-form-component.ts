import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabel } from 'primeng/floatlabel';
import { InputTextModule } from 'primeng/inputtext';
import { MultiSelectModule } from 'primeng/multiselect';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { IndiceEntity } from '../../../entities/Indice.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { IndiceBuilder } from '../../../builders/indice.builder';
import { IndiceService } from '../../../services/indice.service';
import { IndiceListComponent } from "../indice-list-component/indice-list-component";
import { DimensaoListComponent } from "../Dimensao-list-component/Dimensao-list-component";

@Component({
  selector: 'app-Dimensao-grupo-form-component',
  imports: [DatePickerModule, FormsModule, CommonModule, InputTextModule, FloatLabel, ButtonModule, ReactiveFormsModule, MultiSelectModule, DimensaoListComponent, DimensaoListComponent],
  templateUrl: './indice-form-component.html',
})
export class IndiceFormComponent extends BaseFormDirective<IndiceEntity>{
  override builder = new IndiceBuilder;
  override service = inject(IndiceService)
  minDate: Date
    
  override async onNgOnInit(): Promise<void> {
    this.minDate = new Date() // Hoje
  }
}
