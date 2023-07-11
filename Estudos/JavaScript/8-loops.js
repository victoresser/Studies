console.log("\nTrabalhando com condicionais");

const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`,
    `Curitiba`
);
const idadeComprador = 18;
const acompanhante = true;
let temPassagem = false;
const destino = "Rio de Janeiro";

console.log(`\nDestinos Possíveis:`);
console.log(listaDeDestinos);

const podeComprar = idadeComprador >= 18 || acompanhante == true;
let contador = 0;
let destinoExiste = false;

console.log("Verificando disponibilidade de destino...")
// while (contador < 3) {
//     if (listaDeDestinos[contador] == destino) {
//         console.log(`Destino encontrado! -> ${destino}`)
//         listaDeDestinos.splice(contador, 1);
//         destinoExiste = true;
//         break;
//     }
//     contador += 1;
// }

for (let cont = 0; cont < 3; cont++) {
    if (listaDeDestinos[cont] == destino) {
        console.log(`Destino encontrado! -> ${destino}`)
        listaDeDestinos.splice(cont, 1);
        destinoExiste = true;
    }
}

console.log(`Lista de destinos ainda disponíveis:`);
console.log(listaDeDestinos);

if (podeComprar && destinoExiste) {
    console.log("\nBoa Viagem!")
} else {
    console.log("\nDesculpe, tivemos um erro!")
}

