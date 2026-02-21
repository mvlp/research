import { ChangeDetectorRef, Component, inject, OnInit, QueryList, ViewChild, ViewChildren } from '@angular/core';
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
import { GraficoEmpresaComponent } from '../grafico_empresa/grafico_empresa.component';
import { GovernancaService } from '../../../../../services/Govenanca.service';
import { lastValueFrom } from 'rxjs';

@Component({
  selector: 'app-analise-empresa',
  imports: [FormsModule,CommonModule,InputTextModule, AutoCompleteModule,GraficoEmpresaComponent, ButtonModule, ReactiveFormsModule,TabsModule],
  templateUrl: './anal_empresa.component.html',
  styleUrl: './anal_empresa.component.css'
})
export class AnaliseEmpresaComponent {
  service = inject(GovernancaService)
  cdr = inject(ChangeDetectorRef)
  cnpj_empresa = ""
  empresas: Array<SelectDataEntity> = []

  @ViewChildren(GraficoEmpresaComponent) graficos: QueryList<GraficoEmpresaComponent>

  async filter(event: any){
    this.empresas = await lastValueFrom(this.service.getEmpresas(event.query))
    this.cdr.markForCheck()
  }
  selecionado(event: any){
    for (const grafico of this.graficos)
      grafico.getEmpresaOverview(event,undefined)
  }
}
