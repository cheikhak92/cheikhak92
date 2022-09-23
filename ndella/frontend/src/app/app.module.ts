import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { EssaiComponent } from './essai/essai.component';
import { ListEssaiComponent } from './list-essai/list-essai.component';
import { DetailEssaiComponent } from './detail-essai/detail-essai.component';
import { DataService } from 'src/service/data.service';


@NgModule({
  declarations: [
    AppComponent,
    EssaiComponent,
    ListEssaiComponent,
    DetailEssaiComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    HttpModule,
    FormsModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
