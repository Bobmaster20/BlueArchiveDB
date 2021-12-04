document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.character-card').forEach(function(card){
        const portrait = card.querySelector(".character-card-portrait");
        card.onmouseover= function(){
            portrait.style.border ="3px solid #F6E94B";
        }
        card.onmouseleave= function(){
            portrait.style.border ="3px solid #B9DFF2";
        }
    });
});