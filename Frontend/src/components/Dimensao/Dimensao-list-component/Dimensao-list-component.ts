import { Component, inject, Input, Type } from '@angular/core';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { DimensaoEntity } from '../../../entities/Dimensao.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { DimensaoService } from '../../../services/Dimensao.service';
import { DimensaoFormComponent } from '../Dimensao-form-component/Dimensao-form-component';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, FormRecord, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';
import { PerguntaService } from '../../../services/Pergunta.service';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { MultiSelectModule } from 'primeng/multiselect';

@Component({
  selector: 'app-Dimensao-list-component',
  imports: [FormsModule, ReactiveFormsModule, CommonModule, CommonModule, TableModule, ButtonModule, TableHeaderComponent, MultiSelectModule],
  templateUrl: './Dimensao-list-component.html',
  styleUrl: './Dimensao-list-component.css',
})
export class DimensaoListComponent extends BaseListDirective<DimensaoEntity>{
  @Input("idIndice") idIndice: number = 0;
  override filter = new FormRecord<FormControl<any>>({});
  override service = inject(DimensaoService)
  override component = DimensaoFormComponent
  override header = "Dimensão"
  override modalWidth = "35%";

  override async onNgOnInit(): Promise<void> {
    this.filter.addControl('idIndice', new FormControl(this.idIndice))
  }

  override async onPreviousAdd(): Promise<void> {
    this.modalData = {
      idIndice: this.idIndice
    }
    
  }
}
