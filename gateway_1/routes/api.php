<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\GatewayController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::get('/bands', [GatewayController::class, 'bands']);
Route::get('/bands/{id}', [GatewayController::class, 'bandsId']);
Route::get('/genres', [GatewayController::class, 'genres']);
Route::get('/genres/{id}', [GatewayController::class, 'genresId']);
