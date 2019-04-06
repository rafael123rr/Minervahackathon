import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExploreFoodComponent } from './explore-food.component';

describe('ExploreFoodComponent', () => {
  let component: ExploreFoodComponent;
  let fixture: ComponentFixture<ExploreFoodComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExploreFoodComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExploreFoodComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
