function parimpar(n) {
    if (n%2 == 0) { //se o resto da divisão de "n" por 2 for igual a 0...
        return 'Par'
    } else {
        return 'Impar'
    }
}
console.log(parimpar(223))