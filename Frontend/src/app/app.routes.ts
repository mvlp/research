import { Routes } from '@angular/router';
import { MainLayoutComponent } from '../shared/components/main-layout-component/main-layout-component';
import { PerguntaList } from '../components/pergunta/pergunta-list/pergunta-list';
import { DimensaoListComponent } from '../components/Dimensao/Dimensao-list-component/Dimensao-list-component';
import { IndiceListComponent } from '../components/Dimensao/indice-list-component/indice-list-component';
import { HomeComponent } from '../components/extras/home/home.component';
import { ContatoComponent } from '../components/extras/contato/contato.component';
import { PesquisaComponent } from '../components/extras/pesquisa/pesquisa.component';
import { ProducoesComponent } from '../components/extras/producoes/producoes.component';
import { ProjetosComponent } from '../components/extras/projetos/projetos.component';
import { GovernancaComponent } from '../components/extras/governanca/governanca.component';

export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            {
                path: "",
                component: HomeComponent
            },
            {
                path: "pesquisas",
                children: [
                    {
                        path: "",
                        component: PesquisaComponent
                    },
                    {
                        path: "governanca",
                        component: GovernancaComponent   
                    }
                ]
            },
            {
                path: "publicacoes",
                component: ProducoesComponent
            },
            {
                path: "projetos",
                component: ProjetosComponent
            },
            {
                path: "perguntas",
                component: PerguntaList
            },
            {
                path: "dimensoes",
                component: IndiceListComponent
            },
            
        ]
    }
];
