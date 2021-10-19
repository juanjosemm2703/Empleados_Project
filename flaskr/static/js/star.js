var estrella = document.querySelector(".stars")
var estrellas  = document.querySelectorAll('.stars i');
var score= document.getElementById('puntaje');


estrellas.forEach((star, clickIdx) => {
    star.addEventListener('click',()=>{
        estrellas.forEach((otherStar,otherIdx)=>{
            if (otherIdx <= clickIdx){
                otherStar.classList.add('active');
            };
            if (otherIdx > clickIdx){
                otherStar.classList.remove('active');
            };
        });
        score.value = clickIdx+1;
    });
});
