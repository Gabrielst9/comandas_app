function carregarImagem(){
    var input = document.getElementById("foto");
    var fReader = new FileReader();
    fReader.readAsDataURL(input.files[0]);
    fReader.onloadend = function(event){
        var img = document.getElementById("img");
        img.src = event.target.result;
        
    }
}