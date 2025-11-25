import { Component, inject, Input, Type } from '@angular/core';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { IndiceEntity } from '../../../entities/Indice.entity';
import { RestService } from '../../../shared/interfaces/rest-service.interface';
import { IndiceService } from '../../../services/Indice.service';
import { IndiceFormComponent } from '../indice-form-component/indice-form-component';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, FormRecord, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';
import { PerguntaService } from '../../../services/Pergunta.service';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { MultiSelectModule } from 'primeng/multiselect';

@Component({
  selector: 'app-indice-list-component',
  imports: [FormsModule, ReactiveFormsModule, CommonModule, CommonModule, TableModule, ButtonModule, TableHeaderComponent, MultiSelectModule],
  templateUrl: './indice-list-component.html',
  styleUrl: './indice-list-component.css',
})
export class IndiceListComponent extends BaseListDirective<IndiceEntity>{
  @Input("idGrupo") idGrupo: number = 0;
  override filter = new FormRecord<FormControl<any>>({});
  override service = inject(IndiceService)
  override component = IndiceFormComponent
  override header = "Indice"

  override async onNgOnInit(): Promise<void> {
    this.filter.addControl('idGrupo', new FormControl(this.idGrupo))
  }

  override async onPreviousAdd(): Promise<void> {
    this.modalData = {
      idGrupo: this.idGrupo
    }
  }
}
