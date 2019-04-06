import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExploreFoodAdditivesComponent } from './explore-food-additives.component';

describe('ExploreFoodAdditivesComponent', () => {
  let component: ExploreFoodAdditivesComponent;
  let fixture: ComponentFixture<ExploreFoodAdditivesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExploreFoodAdditivesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExploreFoodAdditivesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
