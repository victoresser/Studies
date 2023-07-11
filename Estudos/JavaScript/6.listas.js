console.log("Trabalhando com listas");

const listaDeDestinos = new Array(
    `Salvador`,
    ` São Paulo`,
    ` Rio de Janeiro`,
    ` Curitiba`
);

console.log(`Destinos Possíveis: ${listaDeDestinos}`);
console.log(listaDeDestinos);

listaDeDestinos.splice(1, 1);
console.log(listaDeDestinos);