// const flashcard = document.getElementsByClassName('flashcards')[0];
// const createBox = document.getElementsByClassName('create-box')[0];
// const question = document.getElementById('txtQuestion');
// const answer = document.getElementById('txtAnswer');

// // var contentArray = localStorage.getItem('items')?
// // JSON.parse(localStorage.getItem('items')) : [];

// let content = {'A':'a'};

// let contentArray = Object.entries(terms);

// function AAA() {
//     console.log('HELO');
//     console.log(contentArray[0]);
// }

// contentArray.forEach(divMaker);
// function divMaker(text) {
//     var div = document.createElement("div");
//     var h2_question = document.createElement('h2');
//     var h2_answer = document.createElement('h2');

//     div.className = 'flashcard';

//     h2_question.setAttribute('style', "border-top:1px solid red; padding: 15px; margin-top:30px");
//     h2_question.innerHTML = text.my_question;
    
//     h2_answer.setAttribute('style', "text-align: center; color: red");
//     h2_answer.innerHTML = text.my_answer;

//     div.appendChild(h2_question);
//     div.appendChild(h2_answer);

//     div.addEventListener("click", function() {
//         if(h2_answer.style.display=="none")
//             h2_answer.style.display=="block";
//         else 
//             h2_answer.style.display=="none";

//     })

//     delFlashcards.appendChild(div);

//     delFlashcards.appendChild(div);
// }

// function addFlashcard() {
//     var flashcard_info = {
//         'my_question' : question.value,
//         'my_answer' : answer.value
//     }

//     console.log(flashcard_info);
//     contentArray.push(flashcard_info);
//     console.log("just pushed: ");
//     console.log(contentArray);
//     // localStorage.setItem('items', JSON.stringify(contentArray));
//     divMaker(contentArray[contentArray.length-1]);
//     question.value = '';
//     answer.value = '';
// }

// //delete all flashcards
// function delFlashcards() {
//     localStorage.clear();
//     delFlashcards.innerHTML = ``;
//     contentArray = [];
// }

// function hideCreateBox() {
//     createBox.style.display = 'none';
//     question.value = '';
//     answer.value = '';
// }

// function showCreateCardBox() {
//     createBox.style.display = 'block';
// }
let terms = {}

var contentArray = localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : [];

document.getElementById("save_card").addEventListener("click", () => {
  addFlashcard();
});

document.getElementById("delete_cards").addEventListener("click", () => {
  localStorage.clear();
  flashcards.innerHTML = '';
  contentArray = [];
});

document.getElementById("show_card_box").addEventListener("click", () => {
  document.getElementById("create_card").style.display = "block";
});

document.getElementById("close_card_box").addEventListener("click", () => {
  document.getElementById("create_card").style.display = "none";
});

flashcardMaker = (text, delThisIndex) => {
  const flashcard = document.createElement("div");
  const question = document.createElement('h2');
  const answer = document.createElement('h2');
  const del = document.createElement('i');

  flashcard.className = 'flashcard';

  question.setAttribute("style", "border-top:1px solid red; padding: 15px; margin-top:30px");
  question.textContent = text.my_question;

  answer.setAttribute("style", "text-align:center; display:none; color:red");
  answer.textContent = text.my_answer;

  del.className = "fas fa-minus";
  del.addEventListener("click", () => {
    contentArray.splice(delThisIndex, 1);
    localStorage.setItem('items', JSON.stringify(contentArray));
    window.location.reload();
  })

  flashcard.appendChild(question);
  flashcard.appendChild(answer);
  flashcard.appendChild(del);

  flashcard.addEventListener("click", () => {
    if(answer.style.display == "none")
      answer.style.display = "block";
    else
      answer.style.display = "none";
  })

  document.querySelector("#flashcards").appendChild(flashcard);
}

contentArray.forEach(flashcardMaker);

addFlashcard = () => {
  const question = document.querySelector("txtQuestion");
  const answer = document.querySelector("txtAnswer");

  let flashcard_info = {
    'my_question' : question.value,
    'my_answer'  : answer.value
  }

  contentArray.push(flashcard_info);
  localStorage.setItem('items', JSON.stringify(contentArray));
  flashcardMaker(contentArray[contentArray.length - 1], contentArray.length - 1);
  question.value = "";
  answer.value = "";
}