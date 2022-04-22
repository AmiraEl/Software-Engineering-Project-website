const term = document.querySelector('.term');
const definition = document.querySelector('.definition');
const checkBtn = document.querySelector('.btnDef');
const nextBtn = document.querySelector('.btnNext');
const prevBtn = document.querySelector('.btnPrev');

let terms = {
    CMM : 'Capability Maturity Model',
    "What are non-functional requirements?": "quality attribute, performance attribute, security attribute, or general system constraint",
    "Use-cases are an example of _ based models": "scenario-based models"
}
let data = Object.entries(terms);

// //from tutorial
// function getRandomTerm() {
//     randomTerm = data[Math.floor(Math.random()*data.length)];
//     term.innerHTML =`<h3>${randomTerm[0]}</h3>`;
//     definition.innerHTML =`<h3>${randomTerm[1]}</h3>`;
// }

let i =0; 

function loadCards() {
    term.innerHTML =`<h3>${data[i][0]}</h3>`;
    definition.innerHTML =`<h3>${data[i][1]}</h3>`;
}

checkBtn.addEventListener('click', function(){
    definition.style.display = 'block'; //show definition card
});

nextBtn.addEventListener('click', function(){
    // getRandomTerm();
    i+=1;
    loadCards();
    definition.style.display = 'none';
});

prevBtn.addEventListener('click', function(){
    // getRandomTerm();
    i-=1;
    loadCards();
    definition.style.display = 'none'; 
});
