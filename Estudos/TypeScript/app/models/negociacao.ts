export class Negociacao {

    constructor(
        private _data: Date,
        public readonly quantidade: number,
        public readonly valor: number
    ) { }

    get volume(): number {
        const volume = this.quantidade * this.valor
        return volume;
    }

    get data(): Date {
        const data = new Date(this._data.getTime());
        return data;
    }
}