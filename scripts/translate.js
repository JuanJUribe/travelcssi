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
          resultBox.textContent = jsonResult['translatedText'];
          detectedLang = jsonResult['detectedSourceLanguage'];
          detectedLangBox.textContent = 'Detected Language - '+detectedLang
      })
}

let langResponse;

const langPromise = fetch('/fetchsupportedlangs');
langPromise
    .then(result => result.json())
    .then(jsonResult => {
      langResponse = jsonResult;
      console.log('JSON RESULT:')
      console.log(langResponse)

      for (let lang in langResponse){
        $('#autoLang').after('<option value='+langResponse[lang]['language']+'>'+langResponse[lang]['name']+'</option>');
      }
    })
