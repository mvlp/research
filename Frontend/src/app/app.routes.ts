import { Route, Routes } from '@angular/router';
import { MainLayoutComponent } from './layouts/main-layout/main-layout.component';
import { PerguntaList } from '../features/governanca/views/pergunta-list/pergunta-list';

export const routes: Routes = [
    {
        path: "", 
        component: MainLayoutComponent,
        children: [
            {
                path: "perguntas",
                component: PerguntaList,
                
            }
        ]
    },
];
 