function contar() {
    let numInic = document.getElementById('txti')
    let numTerm = document.getElementById('txtt')
    let passo = document.getElementById('txtp')
    let res = document.getElementById('res')

    if (numInic.value.length == 0 || numTerm.value.length == 0 || passo.value.length == 0) {
        window.alert('ERRO - Insira todos os dados.')
        res.innerHTML = 'Impossível contar!'
    } else {
        res.innerHTML = 'Contando: '
        let i = Number(numInic.value)
        let t = Number(numTerm.value)
        let p = Number(passo.value)
        if (p <= 0) {
            window.alert('Passo inválido! Considerando PASSO igual a 1')
            p = 1
        }
        if (i < t) {
            // contagem crescente
            for(let c = i; c <= t; c += p) {
                res.innerHTML += ` ${c} \u{1F449}`
            }
        } else {
            //contagem regressiva
            for (let c = i; c >= t; c -= p) {
                res.innerHTML += ` ${c} \u{1F449}`
            }           
        }
        res.innerHTML += `\u{1F3C1}`
    }
}