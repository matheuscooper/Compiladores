/* Código desenvolvido corretamente */
/* Nota: 2.0 */

class Venda {
    #id
    #quantidade
    #preco

    constructor(id, quant, preco) {
        this.setId(id);
        this.setQuant(quant);
        this.setPreco(preco);
    }

    setId(id) {
        this.#id = id;
    }

    setQuant(quant) {
        this.#quantidade = quant;
    }

    setPreco(preco) {
        this.#preco = preco;
    }

    getId() {
        return this.#id;
    }

    getQuant() {
        return this.#quantidade;
    }

    getPreco() {
        return this.#preco;
    }

    getValorTotal() {
        return (this.getQuant() * this.getPreco());
    }

}

let pizza = new Venda("01", 2, 50);
let kikao = new Venda("02", 3, 10);

console.log(pizza.getValorTotal());
console.log(kikao.getValorTotal());