<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FacilityController extends Controller
{
    public function pending( $facilityId )
    {
        return view('facility.pending');
    }
}
