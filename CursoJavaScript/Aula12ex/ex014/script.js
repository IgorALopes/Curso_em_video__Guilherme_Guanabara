function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        //BOM DIA
        img.src = 'fotomanha.jpg'
        document.body.style.background = '#C0F24C'
    } else if (hora >= 12 && hora < 18) {
        //BOA TARDE
        img.src = 'fototarde.jpg'
        document.body.style.background = '#F99F1E'
    } else {
        // BOA NOITE
        img.src = 'fotonoite.jpg'
        document.body.style.background = '#2C3252'
    }
}