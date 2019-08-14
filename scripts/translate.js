inputBox = document.querySelector('#inputBox');
resultBox = document.querySelector('#resultBox');
translateButton = document.querySelector('#translateButton');

let target = 'es';
let clicked = false;

inputBox.addEventListener('click', eraseInputContent);

if (clicked){
  inputBox.removeEventListener('click', eraseInputContent)
}

function eraseInputContent(){
  inputBox.textContent = '';
  resultBox.textContent = '';
  clicked = true;
}

translateButton.addEventListener('click', translation);

function translation(){
    originalText = inputBox.value;
    const path = '/fetchtranslate/'+originalText+'/'+target
    const promise = fetch(path);
    promise
        .then(result => result.json())       })
        .then(jsonResult => {
          console.log("JSON RESULT:")
          console.log(jsonResult);
          resultBox.textContent = jsonResult['translatedText'];
      })
}
