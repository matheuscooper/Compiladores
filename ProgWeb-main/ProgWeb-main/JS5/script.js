
function barras(){
    let n1 = document.entrada.n1.value;
    let n2 = document.entrada.n2.value;
    let n3 = document.entrada.n3.value;
    let n4 = document.entrada.n4.value;
    let n5 = document.entrada.n5.value;
    let n6 = document.entrada.n6.value;

    document.getElementById("n1").style.cssText = "height: "+n1+"px; width:"+n6+"px; background-color:red;";
    document.getElementById("n2").style.cssText = "height: "+n2+"px; width:"+n6+"px; background-color:red;";
    document.getElementById("n3").style.cssText = "height: "+n3+"px; width:"+n6+"px; background-color:red;";
    document.getElementById("n4").style.cssText = "height: "+n4+"px; width:"+n6+"px; background-color:red;";
    document.getElementById("n5").style.cssText = "height: "+n5+"px; width:"+n6+"px; background-color:red;";

}