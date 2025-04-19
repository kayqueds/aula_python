function enviar(){
    let nome = document.getElementsByName('txtNome')[0].value
    let idade = document.getElementsByName('txtIdade')[0].value
    let email = document.getElementsByName('txtEmail')[0].value

    if (nome.trim() == "" | email.trim() == "" || idade.trim() == ""){
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Preencha todos os campos!",

          });
    }
    else{
        Swal.fire({
            title: "Parabéns!",
            text: "Seu cadastro foi enviado com sucesso!",
            icon: "success"
          });
    }
    alert(msg)
}