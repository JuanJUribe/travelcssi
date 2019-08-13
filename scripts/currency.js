const inputBox = document.querySelector('#inputValue');
const conversionResult = document.querySelector('#conversionResult');
const initialCurrency = document.querySelector('#initialCurrency');
const conversionCurrency = document.querySelector('#conversionCurrency');

let ratesResponse;

const promise = fetch('http://data.fixer.io/api/latest?access_key=7d92924d0f0566a0e74cc504ccd4596a');
promise
    .then(result => result.json())
    .then(jsonResult => {
      ratesResponse = jsonResult;

      for (let rate in ratesResponse['rates']){
        $('#selectInitial').after('<option value='+rate+'>'+rate+'</option>');
        $('#selectConversion').after('<option value='+rate+'>'+rate+'</option>');
      }
    })



inputBox.addEventListener('input', conversion);
initialCurrency.addEventListener('input', conversion);
conversionCurrency.addEventListener('input', conversion);

function conversion(){
  const initialValue = inputBox.value;
  const conversionBaseEURValue = ratesResponse['rates'][conversionCurrency.value]
  const initialBaseEURValue = ratesResponse['rates'][initialCurrency.value]
  const conversionValue = conversionBaseEURValue/initialBaseEURValue;
  const resultValue = initialValue*conversionValue;


  if (isNaN(resultValue)) {
    conversionResult.textContent = '?';
  } else {
    conversionResult.textContent = resultValue;
  }
}
