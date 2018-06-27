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

Route::get('/', function () { phpinfo(); //return view('welcome');
});
Route::get('test2', function () { return view('welcome'); });

Route::get('dashboard', 'DashboardController@home');
