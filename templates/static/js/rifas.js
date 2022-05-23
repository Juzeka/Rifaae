class Rifas {
    constructor () {
        this.carrinho
    }

    teste = []
    $('.cota').on('click', function() {
        var id = `#${this.innerText}`
        teste.push(this.innerText)

        $(id).addClass('disabled')
        console.log(teste)
    })
}