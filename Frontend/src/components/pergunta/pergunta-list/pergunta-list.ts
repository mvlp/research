import { Component, inject } from '@angular/core';
import { BaseListDirective } from '../../../shared/directives/base-list.directive';
import { PerguntaForm } from '../pergunta-form/pergunta-form';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ItemSelectorFieldComponent } from '../../../shared/components/item-selector-field/item-selector-field.component';
import { TableHeaderComponent } from '../../../shared/components/table-header/table-header.component';
import { PerguntaService } from '../../../services/Pergunta.service';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-pergunta-list',
  imports: [FormsModule, ReactiveFormsModule, CommonModule, CommonModule, TableModule, ButtonModule, TableHeaderComponent],
  templateUrl: './pergunta-list.html',
  styleUrl: './pergunta-list.css'
})
export class PerguntaList extends BaseListDirective<PerguntaEntity> {
  override service = inject(PerguntaService)
  override component = PerguntaForm;
  override header = "Pergunta";

}
