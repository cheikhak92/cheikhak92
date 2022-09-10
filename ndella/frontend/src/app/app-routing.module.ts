import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DetailEssaiComponent } from './detail-essai/detail-essai.component';
import { EssaiComponent } from './essai/essai.component';
import { ListEssaiComponent } from './list-essai/list-essai.component';

const routes: Routes = [
  { path:'essai', component: EssaiComponent },
  { path:'essailist', component: ListEssaiComponent },
  { path:'essailist/:id', component: DetailEssaiComponent },
  { path:'', redirectTo: 'essai', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
