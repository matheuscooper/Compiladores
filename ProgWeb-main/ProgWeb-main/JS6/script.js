
class Fila{
    #cabeca;
    #cauda;
    #comprimento;

    constructor(){
        this.#cabeca = null;
        this.#cauda = null;
        this.#comprimento = 0;
    }

    inserir(ponto){
        let novo = new No(ponto);

        if(this.#comprimento == 0){
            this.#cabeca = novo;
        }else{
            this.#cauda.setProximo(novo);
        }

        this.#cauda = novo;
        
        if(this.#comprimento == 8){
            this.remover();
        }else{
            this.#comprimento++;
        }
    }

    remover(){
        document.body.removeChild(this.#cabeca.getPonto());
        this.#cabeca = this.#cabeca.getProximo();
    }
}

class No{
    #proximo;
    #ponto;

    constructor(ponto){
        this.#proximo = null;
        this.#ponto = ponto;
    }

    getProximo(){
        return this.#proximo;
    }

    setProximo(novo){
        this.#proximo = novo;
    }

    getPonto(){
        return this.#ponto;
    }
}

document.getElementById("tela").addEventListener("mousemove", function(event) {
    const dot = document.createElement("div");
    dot.className = "dot";
    dot.style.left = (event.pageX - 4) + "px";
    dot.style.top = (event.pageY - 4) + "px";
    document.body.appendChild(dot);
    fila.inserir(dot);
});

let fila = new Fila();