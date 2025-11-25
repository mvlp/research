import { Component, inject, Input } from '@angular/core';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { IndiceEntity } from '../../../entities/Indice.entity';
import { Builder } from '../../../shared/interfaces/builder.interface';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { IndiceBuilder } from '../../../builders/Indice.builder';
import { IndiceService } from '../../../services/Indice.service';
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
  selector: 'app-indice-form-component',
  imports: [DatePickerModule,FormsModule,CommonModule,InputTextModule, ButtonModule, ReactiveFormsModule, MultiSelectModule],
  templateUrl: './indice-form-component.html',
  styleUrl: './indice-form-component.css',
})
export class IndiceFormComponent extends BaseFormDirective<IndiceEntity> {
  override builder = new IndiceBuilder( )
  override service = inject(IndiceService)

  @Input("idGrupo") idGrupo
  perguntaService = inject(PerguntaService)
  perguntaOptions: PerguntaEntity[]

  override async onNgOnInit(): Promise<void> {
    this.form.controls.idGrupo.setValue(this.idGrupo)
    await this.perguntaService.getByFilters({}).subscribe(res =>{
      this.perguntaOptions = res
      console.log("OPIÇÔES" ,this.perguntaOptions)
    })
  }

}
