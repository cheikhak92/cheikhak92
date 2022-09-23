import { Component, OnInit } from '@angular/core';
import { DataService } from '../../service/data.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { Essai } from '../model/essai.model';


@Component({
  selector: 'app-list-essai',
  templateUrl: './list-essai.component.html',
  styleUrls: ['./list-essai.component.css']
})
export class ListEssaiComponent implements OnInit {

  essais : any;


  constructor(private http: HttpClient,
    private dataService: DataService,
    private activatedRoute: ActivatedRoute,
    private router: Router) {}

  ngOnInit(): void {
    this.getEssai();
  }

  getEssai(){
    this.dataService.get('/essais')
    .then(
      (response:any) => {
        this.essais = response;
        // console.log(this.essais);
      },
      err => {
      }
    );
  }

}
