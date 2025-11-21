import { Routes } from '@angular/router';
import { MainLayoutComponent } from '../shared/components/main-layout-component/main-layout-component';
import { PerguntaList } from '../components/pergunta/pergunta-list/pergunta-list';

export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            {
                path: "perguntas",
                component: PerguntaList
            }
        ]
    }
];
