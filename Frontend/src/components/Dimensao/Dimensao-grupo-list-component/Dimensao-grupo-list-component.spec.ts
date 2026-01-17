import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DimensaoGrupoListComponent } from './Dimensao-grupo-list-component';

describe('DimensaoGrupoListComponent', () => {
  let component: DimensaoGrupoListComponent;
  let fixture: ComponentFixture<DimensaoGrupoListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DimensaoGrupoListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DimensaoGrupoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
