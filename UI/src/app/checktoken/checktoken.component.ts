import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { map, switchMap, mergeMap } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-checktoken',
  templateUrl: './checktoken.component.html',
  styleUrls: ['./checktoken.component.css']
})
export class ChecktokenComponent implements OnInit {

  constructor(private actroute: ActivatedRoute, 
    private router: Router,
    private http: HttpClient) { 
    
  }

  ngOnInit() {
    this.actroute.fragment.pipe(
      map(fragment => new URLSearchParams(fragment)),
      map(prms => ({
        access_token: prms.get('access_token')
      })), 
      mergeMap( token => 
        this.http.get('http://127.0.0.1:5000/api/users/checkauthtoken/'+token.access_token)
      )
    ).subscribe( res => { 
      console.log(res);
      if(res['status'] == 200){
        this.router.navigate(['/home']);
      }else{
        this.router.navigate(['/']);
      }
     },
    (err) => {
      debugger;
      this.router.navigate(['/']);
    });
  }

}
 