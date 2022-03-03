var selNums = []

function adicionar(){
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')
    let rep = selNums.find(repet => repet == num.value)

    if (num.value.length == 0) {
        window.alert('Digite um número.')
    } else if (num.value > 100 || num.value < 1) {
        window.alert('Coloque um número entre 1 e 100.')    
    } else if (selNums.includes(rep)) {
        window.alert('Número repetido. Por favor, insira outro.')
    } else {
        let n = Number(num.value)        
        let item = document.createElement('option')
            item.text = `Número ${n} adicionado.`
            item.value = `tab${n}`
            tab.appendChild(item)
            selNums.push(n)
    }
}

function processar() {
    let res = document.querySelector('#res')
    
    function somar(total, number) {
        return total + number
    }

    res.innerHTML = `<p>Ao todo, temos ${selNums.length} números cadastrados.</p>
                    <p>O maior número é ${Math.max.apply(null, selNums)}.</p>
                    <p>O menor número é ${Math.min.apply(null, selNums)}.</p>
                    <p>A soma dos valores é ${selNums.reduce(somar,0)}.</p>
                    <p>A média dos valores é ${selNums.reduce(somar,0)/selNums.length}.</p>
                    `
}