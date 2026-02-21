import { ChangeDetectorRef, Component, inject, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabel } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { TableModule } from 'primeng/table';
import { lastValueFrom } from 'rxjs';
import { GovernancaService } from '../../../../../services/Govenanca.service';
@Component({
  selector: 'app-empresas-ausentes',
  imports: [FormsModule,CommonModule,InputTextModule,TableModule, ButtonModule, ReactiveFormsModule],
  templateUrl: './empresas_ausentes.component.html',
  styleUrl: './empresas_ausentes.component.css'
})
export class EmpresasAusentesComponent implements OnInit {
  service = inject(GovernancaService)
  cdr = inject(ChangeDetectorRef)
  faltantes : any
  ngOnInit(): void {
    this.getDadosFaltantes()
  }

  async getDadosFaltantes(){
    this.faltantes = await lastValueFrom(this.service.getDadosFaltantes())
    this.cdr.markForCheck()
  }
    

}
