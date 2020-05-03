<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;


class SubstractionController extends Controller
{
    public function index()
    {
        return response()->json('index', 200);
    }

    public function do_substraction(Request $request)
    {
        $this->validate($request, [
            'number1' => 'required|integer',
            'number2' => 'required|integer'
        ]);
        $number1 = $request->number1;
        $number2 = $request->number2;

        $result = floor($number1 - $number2);

        $res_data = [
            "status" => "success",
            "result" => $result
        ];

        return response()->json($res_data, 200);
    }
}
