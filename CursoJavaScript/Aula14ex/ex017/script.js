function tabuada() {
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')
    if (num.value.length == 0) {
        window.alert('Digite um número')
    } else {
        let n = Number(num.value)
        let c = 1
        tab.innerHTML = ''
        while (c <= 10) {
            let item = document.createElement('option')
            item.text = `${n} X ${c} = ${n*c}`
            item.value = `tab${c}` // este roll serve para demostrar, para outras liguagens como o PhP, qual item o usuário selecionou. Neste exercício, esta tab é a "1", a próxima é a "2", e assim sucessivamente. Para o JavaScript não faz diferença.
            tab.appendChild(item) // Adiciona um elemento filho na tab para poder aparecer no elemento select.
            c++
        }
    }
}