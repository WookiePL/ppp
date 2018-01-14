import {Injectable} from "@angular/core";
import {Observable} from "rxjs/Observable";
import {IPoem} from "./poem";


import 'rxjs/add/operator/do';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import 'rxjs/add/operator/map';
import 'rxjs/add/observable/of';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {AuthService} from "../shared/services/auth.service";

@Injectable()
export class PoemService {
    constructor(private http: HttpClient, private _authService: AuthService) {
    }

    getPoems(): Observable<IPoem[]> {
        return this.http.get<IPoem[]>('/api/poems')
            .do(data => console.log('getPoems' + JSON.stringify(data)))
            .catch(this.handleError);
    }

    private handleError(error: HttpErrorResponse) {
        console.error(error);
        return Observable.throw(error || 'Server error');
    }
}