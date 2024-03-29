export class Negociacao {
    constructor(_data, quantidade, valor) {
        this._data = _data;
        this.quantidade = quantidade;
        this.valor = valor;
    }
    get volume() {
        const volume = this.quantidade * this.valor;
        return volume;
    }
    get data() {
        const data = new Date(this._data.getTime());
        return data;
    }
}
