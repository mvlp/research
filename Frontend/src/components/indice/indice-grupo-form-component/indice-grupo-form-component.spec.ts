import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IndiceGrupoFormComponent } from './indice-grupo-form-component';

describe('IndiceGrupoFormComponent', () => {
  let component: IndiceGrupoFormComponent;
  let fixture: ComponentFixture<IndiceGrupoFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IndiceGrupoFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IndiceGrupoFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
