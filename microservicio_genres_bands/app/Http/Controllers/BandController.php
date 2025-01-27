<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Band;

class BandController extends Controller
{
    public function index()

    {
        $bands = Band::all();
        return $bands;
    }

    public function show(string $id)
    {
        $name = Band::find($id)->name;
        if (!$name) {
            
            return response()->json(['error' => 'No band found'], 404);
        }
        return $name;

    }
}
