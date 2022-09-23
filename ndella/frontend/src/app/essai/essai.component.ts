import { Component, OnInit } from '@angular/core';
import { DataService } from '../../service/data.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ActivatedRoute, Router } from '@angular/router';
import { Essai } from '../model/essai.model';


@Component({
  selector: 'app-essai',
  templateUrl: './essai.component.html',
  styleUrls: ['./essai.component.css']
})
export class EssaiComponent implements OnInit {

  newEssai : Essai;


  constructor(
    private http: HttpClient,
    private dataService: DataService,
    private activatedRoute: ActivatedRoute,
    private router: Router) {
      this.newEssai = new Essai();
    }
  ngOnInit() {
  }

  postEssai(){
    let data =
    {
      nom: this.newEssai.nom,
      prenom: this.newEssai.prenom,
    }
    this.dataService.post('/essais',data)
    .then(
      (response:any) => {
        // console.log(response);
      },
      err => {
      }
    );
  }
}
