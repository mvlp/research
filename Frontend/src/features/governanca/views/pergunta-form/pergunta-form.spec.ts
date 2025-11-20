import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PerguntaForm } from './pergunta-form';

describe('PerguntaForm', () => {
  let component: PerguntaForm;
  let fixture: ComponentFixture<PerguntaForm>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PerguntaForm]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PerguntaForm);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
