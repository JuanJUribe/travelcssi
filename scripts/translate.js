inputBox = document.querySelector('#inputBox');
resultBox = document.querySelector('#resultBox');
translateButton = document.querySelector('#translateButton');

let target = 'es';


inputBox.addEventListener('click', e =>{
  inputBox.textContent = '';
  resultBox.textContent = '';
});

translateButton.addEventListener('click', translation);

function translation(){
    originalText = inputBox.value;
    const path = '/fetchtranslate/'+originalText+'/'+target
    // const path = '/fake'
    // const path = 'https://dog.ceo/api/breeds/image/random'
    console.log("PATH: " + path)
    // const promise = fetch('/fetchtranslate/'+originalText+'/'+target);
    const promise = fetch(path);
    promise
        .then(result => {

          // result = UTF8.decode(result.bodyBytes)

          console.log("RESULT:")
          console.log(result)
          resultJSON = result.json()
          console.log("RESULT JSON:")
          console.log(resultJSON)
          return resultJSON
        })
        .then(jsonResult => {
          console.log("JSON RESULT:")
          console.log(jsonResult);
          resultBox.textContent = jsonResult['translatedText'];
      })
}
