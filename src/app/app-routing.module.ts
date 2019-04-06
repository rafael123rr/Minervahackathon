import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ExploreFoodComponent } from './explore-food/explore-food.component';
import { ExploreFoodAdditivesComponent } from './explore-food-additives/explore-food-additives.component';
import { SearchComponent } from './search/search.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  { path: 'foods', component: ExploreFoodComponent },
  { path: 'additives', component: ExploreFoodAdditivesComponent},
  { path: 'search', component: SearchComponent},
  { path: '', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
