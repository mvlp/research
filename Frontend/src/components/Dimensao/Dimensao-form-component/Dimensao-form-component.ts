import { Component, inject, Input } from '@angular/core';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { DimensaoEntity } from '../../../entities/Dimensao.entity';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { DimensaoBuilder } from '../../../builders/Dimensao.builder';
import { DimensaoService } from '../../../services/Dimensao.service';
import { DatePickerModule } from 'primeng/datepicker';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { FloatLabel } from 'primeng/floatlabel';
import { InputTextModule } from 'primeng/inputtext';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { PerguntaService } from '../../../services/Pergunta.service';
import { MultiSelectModule } from 'primeng/multiselect';

@Component({
  selector: 'app-Dimensao-form-component',
  imports: [DatePickerModule,FormsModule,CommonModule,InputTextModule, ButtonModule, ReactiveFormsModule, MultiSelectModule],
  templateUrl: './Dimensao-form-component.html',
  styleUrl: './Dimensao-form-component.css',
})
export class DimensaoFormComponent extends BaseFormDirective<DimensaoEntity> {
  override builder = new DimensaoBuilder( )
  override service = inject(DimensaoService)

  @Input("idGrupo") idGrupo
  perguntaService = inject(PerguntaService)
  perguntaOptions: PerguntaEntity[]

  override async onNgOnInit(): Promise<void> {
    this.form.controls.idGrupo.setValue(this.idGrupo)
    await this.perguntaService.getByFilters({}).subscribe(res =>{
      this.perguntaOptions = res
    })
  }

}
