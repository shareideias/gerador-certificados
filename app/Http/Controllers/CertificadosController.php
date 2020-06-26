<?php


namespace App\Http\Controllers;


use Illuminate\Http\Request;

class CertificadosController extends Controller
{
    function certificados(Request $request) {
        $dir = getcwd();
        $id = $request->query('id');
        $pydir = 'py "C:\Users\vinic\OneDrive\Área de Trabalho\Share\gerador-certificados\app\Utils\certificados.py" ' . $id;
        $output = exec($pydir);

        return view('certificados');
    }
}
