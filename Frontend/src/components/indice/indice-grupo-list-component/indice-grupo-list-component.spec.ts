import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndiceGrupoListComponent } from './indice-grupo-list-component';

describe('IndiceGrupoListComponent', () => {
  let component: IndiceGrupoListComponent;
  let fixture: ComponentFixture<IndiceGrupoListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IndiceGrupoListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IndiceGrupoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
