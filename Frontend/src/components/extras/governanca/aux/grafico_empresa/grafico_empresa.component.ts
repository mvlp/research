import { ChangeDetectorRef, Component, inject, Input, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabel } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { AutoCompleteModule } from 'primeng/autocomplete';
import GraficoEntity from '../../../../../entities/Grafico.entity';
import { IndiceService } from '../../../../../services/indice.service';
import { IndiceEntity } from '../../../../../entities/Indice.entity';
import { TabsModule } from 'primeng/tabs';
import { SelectModule } from 'primeng/select';
import { ChartModule } from 'primeng/chart';
import { lastValueFrom } from 'rxjs';
import { get } from 'http';
@Component({
  selector: 'app-grafico-empresa',
  imports: [FormsModule,CommonModule,InputTextModule, AutoCompleteModule,SelectModule, ButtonModule, ReactiveFormsModule,TabsModule,ChartModule],
  templateUrl: './grafico_empresa.component.html',
  styleUrl: './grafico_empresa.component.css'
})
export class GraficoEmpresaComponent implements OnInit {
  service = inject(IndiceService) 
  cdr = inject(ChangeDetectorRef)
  options = {
    scales: {
        r: {
            angleLines: {
                display: false
            },
            suggestedMin: 0,
            suggestedMax: 1
        }
    }
  }


  ano_selecionado:string = ""
  anos: Array<string> = []
  id_indice = 1
  @Input("cnpj_empresa")
  cnpj_empresa: string = ""
  
  
  
  graficos: Record<string,GraficoEntity>
  indices: Array<IndiceEntity>
  
  ngOnInit(): void {
    this.getIndices()
    this.graficos = {}    
    this.anos= []
  }

  async getIndices(){
    this.indices = await lastValueFrom(this.service.getByFilters({}))
    this.cdr.markForCheck()

    this.getEmpresaOverview(undefined,this.indices[0].id)
  }
  getEmpresaOverview(cnpj_empresa: string | undefined,idIndice: number | string | undefined = undefined){
    console.log(`id: ${idIndice} \ncnpj: ${cnpj_empresa}`);
    this.cnpj_empresa = cnpj_empresa || this.cnpj_empresa
    this.id_indice = Number(idIndice) || this.id_indice //Se for undefined caso seja passado pelo pai
    if (!this.cnpj_empresa || !this.id_indice) return
    this.service.getEmpresaOverview(this.cnpj_empresa,this.id_indice).subscribe(res =>{
      this.graficos = res
      this.anos = Array.from(Object.keys(res))
      this.ano_selecionado = this.anos[0]
      this.cdr.markForCheck()
      
    })
  }

}
