
function counter(numero){
    return function nova(){
        return ++numero;
    }
}

const incrementar = counter(10);
console.log('Primeira chamada ' + incrementar());
console.log('Segunda chamada ' + incrementar());
console.log('Terceira chamada ' + incrementar());
