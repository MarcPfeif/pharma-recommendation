<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group.
|
*/

Route::get('/', function () { phpinfo(); });


Route::get('dashboard', 'DashboardController@home');

// Start Facility Route
Route::get('facility/{id}', 'FacilityController@pending');

// End Facility Routes
