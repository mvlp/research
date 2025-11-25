import { Routes } from '@angular/router';
import { MainLayoutComponent } from '../shared/components/main-layout-component/main-layout-component';
import { PerguntaList } from '../components/pergunta/pergunta-list/pergunta-list';
import { IndiceListComponent } from '../components/indice/indice-list-component/indice-list-component';
import { IndiceGrupoListComponent } from '../components/indice/indice-grupo-list-component/indice-grupo-list-component';

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
                path: "indices",
                component: IndiceGrupoListComponent
            }
        ]
    }
];
