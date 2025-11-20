import { Component, inject } from '@angular/core';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { PerguntaEntity } from '../../entities/Pergunta.entity';
import { PerguntaForm } from '../pergunta-form/pergunta-form';
import { PerguntaService } from '../../services/PerguntaService'
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import { FloatLabelModule } from 'primeng/floatlabel';
import { InputNumberModule } from 'primeng/inputnumber';
import { InputTextModule } from 'primeng/inputtext';
import { MultiSelectModule } from 'primeng/multiselect';
import { TableModule } from 'primeng/table';
import { ItemSelectorFieldComponent } from '../../../shared/components/item-selector-field/item-selector-field.component';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';

@Component({
  selector: 'app-pergunta-list',
  imports: [TableModule, ButtonModule, InputTextModule, FloatLabelModule, FormsModule, ReactiveFormsModule, CommonModule, TableHeaderComponent, CommonModule, MultiSelectModule, ItemSelectorFieldComponent, InputNumberModule],
  templateUrl: './pergunta-list.html',
  styleUrl: './pergunta-list.css'
})
export class PerguntaList extends BaseListDirective<PerguntaEntity> {
  override service = inject(PerguntaService)
  override component = PerguntaForm;
  override header = "Pergunta";

}
