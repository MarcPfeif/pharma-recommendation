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




// Test Routes
Route::get('/test-db', function() {
    try {
        DB::connection()->getPdo();
        return "success connected to db";
    } catch (\Exception $e) {
        die("Could not connect to the database.  Please check your configuration. error:" . $e );
    }
});
