import { ChangeDetectorRef, Component, inject, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TabsModule } from 'primeng/tabs';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabel } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { EmpresasAusentesComponent } from "./aux/empresas_ausentes/empresas_ausentes.component";
import { AnaliseEmpresaComponent } from './aux/anal_empresa/anal_empresa.component';
import { TableModule } from 'primeng/table';
import { GovernancaService } from '../../../services/Govenanca.service';
import { lastValueFrom } from 'rxjs';
import { tabelaData } from '../../../entities/TabelaData.entity';
import { ChartModule } from 'primeng/chart';
import GraficoEntity from '../../../entities/Grafico.entity';
const mapa = {
  "1": "Acionistas",
  "2": "Conselho de Administração",
  "3": "Diretoria",
  "4": "Órgãos de Fiscalização e Controle",
  "5": "Ética e Conflito de Interesses"
} 
@Component({
  selector: 'app-pergunta-form',
  imports: [FormsModule, CommonModule, InputTextModule, TableModule, ChartModule, ButtonModule, ReactiveFormsModule, EmpresasAusentesComponent,AnaliseEmpresaComponent,TabsModule],
  templateUrl: './governanca.component.html',
  styleUrl: './governanca.component.css'
})
export class GovernancaComponent implements OnInit {
  router = inject(Router)
  service = inject(GovernancaService)
  cdr = inject(ChangeDetectorRef)

  value = '1';
  data: Array<tabelaData>;
  tabela: Array<tabelaData>;

  first_option = {

    plugins: {
      title: {
        display: true,
        text: 'Percentual de respostas (%)',
        font: {
          size: 14,  
          weight: 'bold'
        }
      }
    },
    scales: {
      x: {
        display: false  
      },
      y: {
        suggestedMin: 0,
        suggestedMax: 100
      }
    },
    responsive: true,
    maintainAspectRatio: false
  }
  

  first_option2 = {

    plugins: {
      title: {
        display: true,
        text: 'Quantidade de respostas',
        font: {
          size: 14,  
          weight: 'bold'
        }
      }
    },
    scales: {
      x: {
        display: false  
      },
      y: {
        suggestedMin: 0,
        suggestedMax: 100
      }
    },
    responsive: true,
    maintainAspectRatio: false
  }
  
  mid_options = {
    plugins: {
      legend: { display: false }, // legenda única fora
      title: {
        display: false,
      },
    },
    scales: {
      x: {
        display: false   // ⬅️ remove toda a linha X (ticks + grid)
      },
      y: {
        suggestedMin: 0,
        suggestedMax: 100,

      }
    },
    responsive: true,
    maintainAspectRatio: false
  }

  last_option = {
    scales: {
      y: {
        suggestedMin: 0,
        suggestedMax: 100,
      }
    },
    plugins: {
      legend: { display: false }, // legenda única fora
      title: {
        display: false,
      },
    },
    responsive: true,
  }

  percentual_nao: GraficoEntity
  percentual_nao_aplica: GraficoEntity
  percentual_parcialmente: GraficoEntity
  percentual_sim: GraficoEntity
  qtd_nao: GraficoEntity
  qtd_nao_aplica: GraficoEntity
  qtd_parcialmente: GraficoEntity
  qtd_sim: GraficoEntity
  dado:GraficoEntity

  ngOnInit(): void {
    this.getTabela()
    this.getGrafico()
  }


  async getGrafico(){
    const requisicoes: Array<Promise<GraficoEntity>> = []
    requisicoes.push(lastValueFrom(this.service.getGraficoPercentuais(mapa[this.value],"Não")))
    requisicoes.push(lastValueFrom(this.service.getGraficoPercentuais(mapa[this.value],"Não se Aplica")))
    requisicoes.push(lastValueFrom(this.service.getGraficoPercentuais(mapa[this.value],"Parcialmente")))
    requisicoes.push(lastValueFrom(this.service.getGraficoPercentuais(mapa[this.value],"Sim")))

    
    requisicoes.push(lastValueFrom(this.service.getGraficoQtd(mapa[this.value],"Não")))
    requisicoes.push(lastValueFrom(this.service.getGraficoQtd(mapa[this.value],"Não se Aplica")))
    requisicoes.push(lastValueFrom(this.service.getGraficoQtd(mapa[this.value],"Parcialmente")))
    requisicoes.push(lastValueFrom(this.service.getGraficoQtd(mapa[this.value],"Sim")))


    const requisicoesResolvidas = await Promise.all<GraficoEntity>(requisicoes)
    this.percentual_nao = requisicoesResolvidas[0]
    this.percentual_nao_aplica = requisicoesResolvidas[1]
    this.percentual_parcialmente = requisicoesResolvidas[2]
    this.percentual_sim = requisicoesResolvidas[3]


    this.qtd_nao = requisicoesResolvidas[4]
    this.qtd_nao_aplica = requisicoesResolvidas[5]
    this.qtd_parcialmente = requisicoesResolvidas[6]
    this.qtd_sim = requisicoesResolvidas[7]
    this.cdr.markForCheck()
    
  }

  async getTabela(){
    
    this.tabela = await lastValueFrom(this.service.getTable())
    this.cdr.markForCheck()
    this.filter()


  }
  filter(value: number | string | undefined = '1'){
    this.value = String(value)
    this.data = this.tabela.filter(res => res.item.startsWith(String(this.value)))
    this.getGrafico()
  }
  redirectGovernanca(){
    this.router.navigate(["pesquisas","governanca"])
  }
  

}
