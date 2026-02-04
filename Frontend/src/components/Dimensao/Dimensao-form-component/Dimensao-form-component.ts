import { Component, inject, Input } from '@angular/core';
import { BaseFormDirective } from '../../../shared/directives/base-form.directive';
import { DimensaoEntity } from '../../../entities/Dimensao.entity';
import { DimensaoBuilder } from '../../../builders/Dimensao.builder';
import { DimensaoService } from '../../../services/Dimensao.service';
import { DatePickerModule } from 'primeng/datepicker';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ButtonModule } from 'primeng/button';
import {  FloatLabelModule } from 'primeng/floatlabel';
import { InputTextModule } from 'primeng/inputtext';
import { PerguntaEntity } from '../../../entities/Pergunta.entity';
import { PerguntaService } from '../../../services/Pergunta.service';
import { MultiSelectModule } from 'primeng/multiselect';
import { TreeTableModule } from 'primeng/treetable';
import { TreeNode } from 'primeng/api';
@Component({
  selector: 'app-Dimensao-form-component',
  imports: [DatePickerModule,FormsModule,CommonModule,InputTextModule, ButtonModule, ReactiveFormsModule, MultiSelectModule, TreeTableModule,FloatLabelModule],
  templateUrl: './Dimensao-form-component.html',
  styleUrl: './Dimensao-form-component.css',
})
export class DimensaoFormComponent extends BaseFormDirective<DimensaoEntity> {
  override builder = new DimensaoBuilder( )
  override service = inject(DimensaoService)

  estado:string = "PARCIAL"

  id_itens: TreeNode[] = [
    {
      label: "1.Acionistas",
      children: []
    },
    {
      label: "2.Conselho de Administração",
      children: []
    },
    {
      label: "3.Diretoria",
      children: []
    },
    {
      label: "4.Órgãos de Fiscalização e Controle",
      children: []
    },
    {
      label: "5.Ética e Conflitos de Interesse",
      children: []
    },
  ];

  @Input("idIndice") idIndice
  perguntaService = inject(PerguntaService)
  perguntaOptions: PerguntaEntity[]

  override async onNgOnInit(): Promise<void> {
    this.form.controls.idIndice.setValue(this.idIndice)
    await this.perguntaService.getByFilters({}).subscribe(res =>{
      for (const item of res){
        const primeiro_numero = item.id.slice(0,1)
        const index = this.id_itens.findIndex(capitulo => capitulo.label?.startsWith(primeiro_numero)) //encontra o capitulo que inicia com o primeiro numero
        this.id_itens[index].children?.push({
          label: item.id,
          data: { id_item:item.id },
        })
      }
      this.cdr.markForCheck()
      
    })
  }

  


  toggleTriState(id_pergunta:string):any {
    if (!this.form.value.perguntas) return

    const idx = this.form.value.perguntas.findIndex(res => res.id_pergunta == id_pergunta)    
    if (idx == -1){
      return this.form.value.perguntas.push({
        id_pergunta,
        peso: 1,
      })
    }      
    const pergunta = this.form.value.perguntas[idx]
    if (pergunta.peso == 1){
      pergunta.peso = -1
    } else {
      this.form.value.perguntas.splice(idx,1)
    }

  }
  getLabel(id_pergunta:string){
    if (!this.form.value.perguntas) return

    const idx = this.form.value.perguntas.findIndex(res => res.id_pergunta == id_pergunta)    
    if (idx == -1) return '0';
    const pergunta = this.form.value.perguntas[idx]
    return String(pergunta.peso)
  }

}
