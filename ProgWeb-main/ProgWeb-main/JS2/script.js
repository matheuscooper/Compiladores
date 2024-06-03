
function imprimeInicioRodada(){
    console.log("Ecolha sua jogada:");
    console.log("1 - Papel");
    console.log("2 - Pedra");
    console.log("3 - Tesoura");
}

function randInt(min, max){
    return Math.floor(Math.random()* (max - min) + min);
}

function decisao(joga, game){
    let computador;
    let retorno;
    if(game == 1){
        computador = "Papel";
    }else if(game == 2){
        computador = "Pedra";
    }else if(game == 3){
        computador = "Tesoura";
    }
    console.log("O computador jogou " + computador);

    if(joga == game){
        console.log("A rodada empatou!");
        retorno = 0;
    }else if(((joga > 0) & (joga < game)) | ((joga == 3) & (game == 1))){
        console.log("Voce ganhou!");
        retorno = 1;
    }else{
        retorno = -1;
    }
    return retorno;
}

let pontuacao = 0;
let continua = true;

while(continua){
    imprimeInicioRodada();
    jogadaUsuario = parseInt(prompt());
    jogadaSistema = randInt(1, 4);

    let resultado = decisao(jogadaUsuario, jogadaSistema);

    if(resultado == 1){
        pontuacao++;
    }else if(resultado == -1){
        continua = false
    }
}

console.log("Voce perdeu! A sua pontuacao foi de " + pontuacao);
