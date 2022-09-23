import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailEssaiComponent } from './detail-essai.component';

describe('DetailEssaiComponent', () => {
  let component: DetailEssaiComponent;
  let fixture: ComponentFixture<DetailEssaiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DetailEssaiComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetailEssaiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
