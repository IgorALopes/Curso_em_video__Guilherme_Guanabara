function contar(){
    let numInic = document.getElementById('txti')
    let numFim = document.getElementById('txtf')
    let numPassos = document.getElementById('txtp')
    let res = document.getElementById('res')

    if (numInic.value.length == 0 || numFim.value.length == 0 || numPassos.value.length == 0) {
        window.alert('ERRO - Preencha todos os campos')
        res.innerHTML = 'Impossível contar...'
    } else {
        res.innerHTML = 'Contando...'
        let i = Number(numInic.value)
        let f = Number(numFim.value)
        let p = Number(numPassos.value)
        if (p <= 0) {
            window.alert('Valor inválido. Considerando passo igual a 1.')
            p = 1
        }
        if (i < f) {
            for (let c = i; c <= f; c += p) {
                res.innerHTML += ` ${c} \u{1F449}`
            }
        } else {
            for (let c = i; c >= f; c -= p) {
                res.innerHTML += ` ${c} \u{1F449}`
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }

}