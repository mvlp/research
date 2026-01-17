import { Routes } from '@angular/router';
import { MainLayoutComponent } from '../shared/components/main-layout-component/main-layout-component';
import { PerguntaList } from '../components/pergunta/pergunta-list/pergunta-list';
import { DimensaoListComponent } from '../components/Dimensao/Dimensao-list-component/Dimensao-list-component';
import { DimensaoGrupoListComponent } from '../components/Dimensao/Dimensao-grupo-list-component/Dimensao-grupo-list-component';

export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            {
                path: "perguntas",
                component: PerguntaList
            },
            {
                path: "dimensoes",
                component: DimensaoGrupoListComponent
            }
        ]
    }
];
