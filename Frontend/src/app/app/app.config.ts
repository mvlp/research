import { ApplicationConfig, provideBrowserGlobalErrorListeners, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from '../app.routes';
import { provideClientHydration, withEventReplay } from '@angular/platform-browser';
import { PRIME_NG_CONFIG, providePrimeNG } from 'primeng/config';
import { MessageService } from 'primeng/api';
import { provideHttpClient } from '@angular/common/http';
import { DialogService } from 'primeng/dynamicdialog';
import { PerguntaService } from '../../features/governanca/services/PerguntaService';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZonelessChangeDetection(),
    providePrimeNG({
      translation: {
        apply: 'Aplicar',
        clear: 'Limpar',
        accept: 'Sim',
        reject: 'Não',
        firstDayOfWeek: 0,
        dayNames: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
        dayNamesShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
        dayNamesMin: ['Do', 'Se', 'Te', 'Qu', 'Qu', 'Se', 'Sa'],
        monthNames: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        monthNamesShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        today: 'Hoje',
      }
    }),
    provideRouter(routes), provideClientHydration(withEventReplay()),
    MessageService, provideHttpClient(), 
    
    DialogService,PerguntaService
  ]
};
