function enviar(){
    let nome = document.getElementsByName('txtNome')[0].value
    let idade = document.getElementsByName('txtIdade')[0].value
    let email = document.getElementsByName('txtEmail')[0].value

    let msg = "" 
    if (nome.trim() == "" | email.trim() == "" || idade.trim() == ""){
        msg = 'ERRO, você não digitou todos os campos!'
    }
    else{
        msg = `Sucesso, bem-vindo ${nome}`
    }
    alert(msg)
}