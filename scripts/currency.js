const inputBox = document.querySelector('#inputValue');
const conversionResult = document.querySelector('#conversionResult');
const initialCurrency = document.querySelector('#initialCurrency');
const conversionCurrency = document.querySelector('#conversionCurrency');


inputBox.addEventListener('input', conversion);

function conversion(){
  const initialValue = inputBox.value;
  const conversionValue = conversionCurrency.value/initialCurrency.value;
  const resultValue = initialValue*conversionValue;

  conversionResult.textContent = resultValue;
}
