import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChecktokenComponent } from './checktoken.component';

describe('ChecktokenComponent', () => {
  let component: ChecktokenComponent;
  let fixture: ComponentFixture<ChecktokenComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChecktokenComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChecktokenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
