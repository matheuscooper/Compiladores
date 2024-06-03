
class IntegerSet{
    #conjunto;
    #limite;

    constructor(limite){
        this.#conjunto = new Array(limite+1).fill(false);
        this.#limite = limite;
    }

    getLimite(){
        return this.#limite;
    }

    getConjunto(){
        return this.#conjunto;
    }

    insercao(n){
        if((n <= this.#limite) & (n >= 0)){
            this.#conjunto[n] = true;
        }
    }

    exclusao(n){
        if((n <= this.#limite) & (n >= 0)){
            this.#conjunto[n] = false;
        }
    }

    uniao(outroConj){
        let l1 = this.getLimite();
        if(outroConj.getLimite() > l1){
            l1 = outroConj.getLimite();
        }

        let resultado = new IntegerSet(l1);

        for(let i = 0 ; i < l1 ; i++){
            if(this.getConjunto()[i] | outroConj.getConjunto()[i]){
                resultado.insercao(i);
            }
        }
        return resultado;
    }

    intersecao(outroConj){
        let l1 = this.getLimite();
        if(outroConj.getLimite() > l1){
            l1 = outroConj.getLimite();
        }

        let resultado = new IntegerSet(l1);

        for(let i = 0 ; i < l1 ; i++){
            if(this.getConjunto()[i] & outroConj.getConjunto()[i]){
                resultado.insercao(i);
            }
        }
        return resultado;
    }

    diferenca(outroConj){
        let l1 = this.getLimite();
        if(outroConj.getLimite() > l1){
            l1 = outroConj.getLimite();
        }

        let resultado = new IntegerSet(l1);

        for(let i = 0 ; i < l1 ; i++){
            if(this.getConjunto()[i] & !outroConj.getConjunto()[i]){
                resultado.insercao(i);
            }
        }
        return resultado;
    }

    toString(){
        let aux = new Array(1);
        let i = 0;
        for(let j = 0 ; j < this.#limite+1 ; j++){
            if(this.#conjunto[j]){
                aux[i]=j;
                i++;
            }
        }
        // console.log(String(aux));
        return(String(aux));
    }
}

function atualizaLista(id, lista){
    document.getElementById(id).innerHTML = '[' + lista.toString() + ']';
}

function insereLista(id, lista){
    let novo = document.operacoes.entrada.value;/////////////////////////////////////
    // console.log(novo);
    if(novo == undefined){

    }else if(novo > lista.getLimite() | novo < 0){
        alert("Esse valor excede os limites do conjunto!");
    }else{
        lista.insercao(novo);
    }
    
    atualizaLista(id, lista);
}

function removeLista(id, lista){
    let novo = document.operacoes.entrada.value;/////////////////////////////////////
    // console.log(novo);

    lista.exclusao(novo);
    
    atualizaLista(id, lista);
}

function uneListas(){
    document.getElementById("Res").innerHTML = '[' + L1.uniao(L2).toString() + ']';
}

function interListas(){
    document.getElementById("Res").innerHTML = '[' + L1.intersecao(L2).toString() + ']';
}

function difListas(l1, l2){
    document.getElementById("Res").innerHTML = '[' + l1.diferenca(l2).toString() + ']';
}

let limite = parseInt(prompt("Defina o tamanho maximo dos conjuntos\nex:", "100"));

L1 = new IntegerSet(limite);
L2 = new IntegerSet(limite);

// L1.insercao(0);

atualizaLista("L1", L1);
atualizaLista("L2", L2);


// IssoAqui = new IntegerSet(10);
// EsseAqui = new IntegerSet(10);
// IssoAqui.insercao(5);
// IssoAqui.insercao(6);
// // EsseAqui.insercao(5);
// // EsseAqui.insercao(6);

// IssoAqui.diferenca(EsseAqui).toString();