// Caminho do Arquivo de Script: scr/static/script/script.js


// Função para carregar a imagem
// __________________________________________________________________
function carregarImagem()
{
    var input = document.getElementById("foto");
    var fReader = new FileReader();
    fReader.readAsDataURL(input.files[0]);
    fReader.onloadend = function(event)
    {
        var img = document.getElementById("img");
        img.src = event.target.result;
        
    }
}
// __________________________________________________________________