inputBox = document.querySelector('#inputBox');
resultBox = document.querySelector('#resultBox');
detectedLangBox = document.querySelector('#detectedLang');
outputLang = document.querySelector('#outputLang');

let target;
let clicked = false;

let langResponse;

const langPromise = fetch('/fetchsupportedlangs');
langPromise
    .then(result => result.json())
    .then(jsonResult => {
      langResponse = jsonResult;

      for (let lang in langResponse){
        $('#autoLang').after('<option value='+langResponse[lang]['language']+'>'+langResponse[lang]['name']+'</option>');
        $('#select').after('<option value='+langResponse[lang]['language']+'>'+langResponse[lang]['name']+'</option>');
      }
    })

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
    originalText = inputBox.value;
    target = outputLang.value
    console.log(target)
    const path = '/fetchtranslate/'+originalText+'/'+target
    const promise = fetch(path);
    promise
        .then(result => result.json())
        .then(jsonResult => {
          resultBox.textContent = jsonResult['translatedText'];
          detectedLang = jsonResult['detectedSourceLanguage'];
          detectedLangBox.textContent = 'Detected Language - '+detectedLang
      })
}
