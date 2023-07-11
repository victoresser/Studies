console.log("Trabalhando com condicionais");

const listaDeDestinos = new Array(
    `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`,
    `Curitiba`
);
const idadeComprador = 18;
const acompanhante = true;
let temPassagem = false;

console.log(`Destinos Possíveis:`);
console.log(listaDeDestinos);

// if (idadeComprador >= 18) {
//     console.log("Comprador maior de idade!")
//     listaDeDestinos.splice(1, 1); // Removendo item
// } else if (acompanhada == true) {
//     console.log("O comprador é menor de idade, porém está acompanhado.");
//     listaDeDestinos.splice(1, 1); // Removendo item
// } else {
//     console.log("Comprador não é maior de Idade e não posso vender:")
// }

if (temPassagem == false) {
    if (idadeComprador >= 18 || acompanhante == true) {
        console.log("Comprando passagem...");
        console.log(`Passagem comprada para: ${listaDeDestinos[2]}`);
        temPassagem = true;
        listaDeDestinos.splice(2, 1);
    } else {
        console.log("Você não é maior de idade e não tem acompanhante. Por tanto, não pode comprar a passagem.");
    }
}

if (temPassagem == true) {
    console.log("Entrando em área de embarque...");
    if (idadeComprador >= 18 || acompanhante == true) {
        console.log("Embarcando... Boa viagem!");
    } else {
        console.log("Você é menor de idade e/ou não tem acompanhante. Infelizmente, não pode viajar.")
    }
}

console.log(`Lista de destinos ainda disponíveis:`);
console.log(listaDeDestinos);