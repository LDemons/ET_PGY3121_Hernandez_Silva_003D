$(document).ready(function(){

    $("#sumar").click(function(){

        var a= parseInt($("#num1").val());
        var b= parseInt($("#num2").val());
        var suma=a+b;
        $("#resultado").val(suma);
    });

    $("#multiplicar").click(function(){
        var a= parseInt($("#num1").val());
        var b= parseInt($("#num2").val());
        var multi=a*b;
        $("#resultado").val(multi);

    });

    $("#restar").click(function(){
        var a= parseInt($("#num1").val());
        var b= parseInt($("#num2").val());
        var resta=a-b;
        $("#resultado").val(resta);

    });

    $("#dividir").click(function(){
        var a= parseInt($("#num1").val());
        var b= parseInt($("#num2").val());
        var divi=a/b;
        $("#resultado").val(divi);

    });
});