<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class GatewayController extends Controller
{
    private $apiUrl;

    public function __construct()
    {
        $this->apiUrl = env ('MICROSERVICIO_URL');
    }

    public function bands()
   {
    // Realizar una solicitud GET al microservicio para obtener los productos
    $response = Http::get($this->apiUrl . '/bands');
    // Retornar la respuesta del microservicio en formato JSON
    return $response->json();
    
    }

    public function bandsId()
    {
    // Realizar una solicitud GET al microservicio para obtener los productos
    $response = Http::get($this->apiUrl . '/bands/{id}');
    // Retornar la respuesta del microservicio en formato JSON
    return $response->json();
    }

    public function genres()
    {
        // Realizar una solicitud GET al microservicio para obtener los productos
        $response = Http::get($this->apiUrl . '/genres');
        // Retornar la respuesta del microservicio en formato JSON
        return $response->json();
    }

    public function genresId()
    {
        // Realizar una solicitud GET al microservicio para obtener los productos
        $response = Http::get($this->apiUrl . '/genres/{id}');
        // Retornar la respuesta del microservicio en formato JSON
        return $response->json();
    }

}
