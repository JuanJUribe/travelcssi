inputBox = document.querySelector('#inputBox');
resultBox = document.querySelector('#resultBox');
detectedLangBox = document.querySelector('#detectedLang');

let target = 'de';
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

inputBox.addEventListener('input', translation);

function translation(){
    console.log('translatio gonig on')
    originalText = inputBox.value;
    const path = '/fetchtranslate/'+originalText+'/'+target
    const promise = fetch(path);
    promise
        .then(result => result.json())
        .then(jsonResult => {
          console.log("JSON RESULT:")
          console.log(jsonResult);
          resultBox.textContent = jsonResult['translatedText'];
          detectedLang = jsonResult['detectedSourceLanguage'];
          console.log(detectedLang);
          detectedLangBox.textContent = 'Detected Language - '+detectedLang
      })
}
