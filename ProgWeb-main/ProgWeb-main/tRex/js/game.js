(function () {
  const FPS = 300;
  const HEIGHT = 300;
  const WIDTH = 1024;
  const PROB_CENARIO = 0.5;
  const PROB_CACTO = 0.1;
  const PROB_PTERO = 0.05;
  
  let gameLoop;
  let deserto;
  let dino;
  let dia;
  let umMinuto;
  let gover;
  let restart;
  let cenario = [];
  let obstacles = [];
  let score = [];
  let frame = 0;
  let pause = 0;
  let comecou = 0;
  let dn = 0;
  let derrota = 0;
  let velocidade = 2;

  const esperando = 0;
  const correndo = 1;
  const subindo = 2;
  const descendo = 3;
  const abaixado = 4;

  function init() {
    deserto = new Deserto();
    dino = new Dino();
    iniciaScore(score, 5);
    dia = 1;
    gameLoop = setInterval(run, (1000/FPS));
  }

  //começa
  window.addEventListener("keydown", (e) => {
    if (e.code === "Space" && comecou === 0){
      dino.status = subindo;
      umMinuto = setInterval(dianoite, 1000);
      comecou = 1;
    }
  })

  //pula
  window.addEventListener("keydown", (e) => {
    if (e.code === "Space" && comecou === 1 && pause === 0 && derrota === 0) {
      if (dino.status === correndo) dino.status = subindo;
    }
  })

  //pausa
  window.addEventListener("keydown", (e) => {
    if (e.code === "KeyP" && comecou == 1 && derrota === 0) {
      if(pause == 0){
        pause = 1;
        clearInterval(gameLoop);
      }else{
        pause = 0;
        gameLoop = setInterval(run, (1000/FPS));
      }
    }
  })

  //abaixa
  window.addEventListener("keydown", (e) => {
    if (e.code === "ArrowDown" && comecou === 1 && pause === 0 && derrota === 0) {
      dino.element.style.backgroundPositionX = dino.backgroundPositionsX.abaixado1;
      dino.status = abaixado;
      // dino.element.style.bottom = `${dino.altumaMinima}px`;
    }
  })

  //levanta
  window.addEventListener("keyup", (e) => {
    if (e.code === "ArrowDown" && comecou === 1 && derrota === 0) {
      dino.status = correndo;
      dino.element.style.backgroundPositionX = dino.backgroundPositionsX.correndo1;
    }
  })
 

  class Deserto {
    constructor() {
      this.element = document.createElement("div")
      this.element.className = "deserto";
      this.element.style.width = `${WIDTH}px`;
      this.element.style.height = `${HEIGHT}px`;
      document.getElementById("game").appendChild(this.element)

      this.chao = document.createElement("div")
      this.chao.className = "chao"
      this.chao.style.backgroundPositionX = 0;
      this.element.appendChild(this.chao)
    }
    mover() {
      this.chao.style.backgroundPositionX = `${parseInt(this.chao.style.backgroundPositionX) - velocidade }px`
    }
  }

  class Dino {
    #status
    constructor() {
      this.backgroundPositionsX = {
        esperando: "-57px",
        correndo1: "-1391px",
        correndo2: "-1457px",
        pulando: "-1259px",
        abaixado1: "-1654px",
        abaixado2: "-1743px"
      }// 0-esperando, 1-correndo, 2-subindo, 3-descendo, 4-abaixado
      this.#status = esperando;
      this.altumaMinima = 2;
      this.altumaMaxima = 160;
      this.element = document.createElement("div");
      this.element.className = "dino";
      this.element.style.backgroundPositionX = this.backgroundPositionsX.esperando ;
      this.element.style.backgroundPositionY = "-2px";
      this.element.style.bottom = `${this.altumaMinima}px`;
      deserto.element.appendChild(this.element);
    }
    /**
     * @param {number} value
     */
    set status(value) {
      if (value >= 0 && value <= 5) this.#status = value;
    }
    get status() {
      return this.#status;
    }
    correr() {
      if(this.#status === abaixado){
        this.element.style.backgroundPositionY = "-29px";
        this.element.style.width = "85px";
        this.element.style.height = "40px";
      }else{
        this.element.style.backgroundPositionY = "-2px";
        this.element.style.width = "66px";
        this.element.style.height = "70px";
      }

      if (this.#status === correndo && frame % 20 === 0){
        this.element.style.backgroundPositionX = this.element.style.backgroundPositionX === this.backgroundPositionsX.correndo1 ? this.backgroundPositionsX.correndo2 : this.backgroundPositionsX.correndo1;
      }
        else if (this.#status === subindo) {
        this.element.style.backgroundPositionX = this.backgroundPositionsX.pulando;
        this.element.style.bottom = `${parseInt(this.element.style.bottom) + 3}px`;
        if (parseInt(this.element.style.bottom) >= this.altumaMaxima) this.status = descendo;
      }
      else if (this.#status === descendo) {
        this.element.style.bottom = `${parseInt(this.element.style.bottom) - 1}px`;
        if (parseInt(this.element.style.bottom) <= this.altumaMinima) this.status = correndo;
      }
      else if(this.#status === abaixado && frame % 20 === 0){
        this.element.style.bottom = `${this.altumaMinima}px`;
        this.element.style.backgroundPositionX = this.element.style.backgroundPositionX === this.backgroundPositionsX.abaixado1 ? this.backgroundPositionsX.abaixado2 : this.backgroundPositionsX.abaixado1;
      }
    }
  }

  class Nuvem {
    constructor() {
      this.element = document.createElement("div");
      this.element.className = "nuvem";
      this.element.style.right = 0;
      this.element.style.top = `${parseInt(Math.random() * 200)}px`
      deserto.element.appendChild(this.element);
    }
    mover() {
      this.element.style.right = `${parseInt(this.element.style.right) + velocidade }px`;
    }
  }

  class Estrela {
    constructor() {
      this.element = document.createElement("div");
      this.element.className = `estrela${parseInt(Math.random() * 3)}`;
      this.element.style.right = 0;
      this.element.style.top = `${parseInt(Math.random() * 200)}px`
      deserto.element.appendChild(this.element);
    }
    mover() {
      this.element.style.right = `${parseInt(this.element.style.right) + velocidade }px`;
    }
  }

  class Cacto{
    constructor() {
      this.element = document.createElement("div");
      this.element.className = `cacto${parseInt(Math.random() * 22)}`;
      this.element.style.right = 0;
      this.element.style.bottom = 0;
      deserto.element.appendChild(this.element);
    }
    mover() {
      this.element.style.right = `${parseInt(this.element.style.right) + velocidade }px`; 
    }
  }

  class Pterodatil{
    constructor() {
      this.element = document.createElement("div");
      this.element.className = "ptero";
      this.element.style.right = 0;
      this.element.style.bottom = `${2 + parseInt(Math.random() * 3)*40}px`;
      deserto.element.appendChild(this.element);
    }
    mover() {
      this.element.style.right = `${parseInt(this.element.style.right) + 2*velocidade }px`;
      if (frame % 20 == 0){
        this.element.style.backgroundPositionX = this.element.style.backgroundPositionX === '-198px' ? this.element.style.backgroundPositionX = '-266px' : this.element.style.backgroundPositionX = '-198px';
      }
    }
  }

  class Score{
    #valor;
    constructor(x){
      this.element = document.createElement("div");
      this.element.className = "num";
      this.element.style.right = `${2+(15*x)}px`;
      this.element.style.top = "2px";
      deserto.element.appendChild(this.element);
      this.#valor = 0;
      this.element.style.backgroundPositionX = "-970px";
    }
    incrementa(v){
      this.#valor += v;
      let r = this.#valor === 10 ? 1 : 0;
      this.#valor %= 10;
      switch(this.#valor) {
        case 0:
          this.element.style.backgroundPositionX = "-970px";
          break;
        case 1:
          this.element.style.backgroundPositionX = "-985px";
          break;
        case 2:
          this.element.style.backgroundPositionX = "-1000px";
          break;
        case 3:
          this.element.style.backgroundPositionX = "-1015px";
          break;
        case 4:
          this.element.style.backgroundPositionX = "-1030px";
          break;
        case 5:
          this.element.style.backgroundPositionX = "-1045px";
          break;
        case 6:
          this.element.style.backgroundPositionX = "-1060px";
          break;
        case 7:
          this.element.style.backgroundPositionX = "-1075px";
          break;
        case 8:
          this.element.style.backgroundPositionX = "-1090px";
          break;
        case 9:
          this.element.style.backgroundPositionX = "-1105px";
          break;
      }
      return r;
    }
  }

  function run() {
    if(comecou === 1 && derrota === 0){
      frame = frame + 1;
      if (frame === FPS){
        frame = 0;
      }
      if (frame % 30 === 0){
        incrementaScore(score);
      }

      deserto.mover();
      dino.correr();

      if (Math.random() * 100 <= PROB_CENARIO){
        if(dia === 1){
          cenario.push(new Nuvem());
        }else{
          cenario.push(new Estrela());
        }
      }
      if (Math.random() * 100 <= PROB_CACTO) obstacles.push(new Cacto());
      if (Math.random() * 100 <= PROB_PTERO) obstacles.push(new Pterodatil());
      if (frame % 2 === 0) cenario.forEach(nuvem => nuvem.mover());
      obstacles.forEach(cacto => cacto.mover());
      removedor(cenario);
      removedor(obstacles);

      let i = 0;
      while(i < obstacles.length){
        if(colisao(dino.element, obstacles[i].element)){
          derrota = 1;
          perdeu();
        }
        i++;
      }
    }
  }

  function dianoite(){
    if(pause === 0 && derrota === 0){
      dn++;
      if(dn === 60){
        dn = 0;
        if(deserto.element.style.backgroundColor != "black"){
          deserto.element.style.backgroundColor = "black";
          dia = 0;
        }else{
          deserto.element.style.backgroundColor = "white";
          dia = 1;
        }
        velocidade++;
        dn = 0;
      }      
    }
  }

  function removedor(vetor){
    while(vetor.length > 0 && vetor[0].element.style.right === 0){
      deserto.element.removeChild(vetor.shift());
    }
  }

  function iniciaScore(vetor, v){
    for(let i = 0 ; i < v ; i++){
      vetor.push(new Score(i))
    }
  }

  function incrementaScore(vetor){
    let aux = 1;
    for(let i = 0 ; i < vetor.length ; i++){
      aux = vetor[i].incrementa(aux);
    }
  }

  function colisao(div1, div2) {
    const rect1 = div1.getBoundingClientRect();
    const rect2 = div2.getBoundingClientRect();

    return (
        rect1.right > rect2.left &&
        rect1.left < rect2.right &&
        rect1.bottom > rect2.top &&
        rect1.top < rect2.bottom);
  }

  function perdeu(){
    gover = document.createElement("div");
    gover.className = "gover";

    restart = document.createElement("div");
    restart.className = "restart";

    deserto.element.appendChild(gover);
    deserto.element.appendChild(restart);

    dino.element.style.backgroundPositionX = "-1522px";

    restart.addEventListener("click", reinicia);
  }

  function reinicia(){
    while(cenario.length > 0){
      deserto.element.removeChild(cenario.shift().element);
    }

    while(obstacles.length > 0){
      deserto.element.removeChild(obstacles.shift().element);
    }

    while(score.length > 0){
      deserto.element.removeChild(score.shift().element);
    }

    gover.removeEventListener("click", reinicia);

    deserto.element.removeChild(gover);
    deserto.element.removeChild(restart);

    deserto.element.style.backgroundColor = "white";

    dino.status = correndo;
    dino.element.style.bottom = `${dino.altumaMinima}px`;
    
    iniciaScore(score, 5);
    velocidade = 2;
    dia = 1; 
    derrota = 0;
    dn = 0;
  }

  init();

})()