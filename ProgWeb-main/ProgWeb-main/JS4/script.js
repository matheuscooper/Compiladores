

function faz(){
    let raio = document.circulo.raio.value
    let pi = 3.14
    let area = raio*raio*pi
    let circunferencia = 2*raio*pi

    document.circulo.area.value = area
    document.circulo.circunferencia.value = circunferencia
};

