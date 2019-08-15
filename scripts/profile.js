let ratesResponse;

const ratesPromise = fetch('http://data.fixer.io/api/latest?access_key=7d92924d0f0566a0e74cc504ccd4596a');
ratesPromise
    .then(result => result.json())
    .then(jsonResult => {
      ratesResponse = jsonResult;

      for (let rate in ratesResponse['rates']){
        $('#selectCurrency').after('<option value='+rate+'>'+rate+'</option>');
      }
    })

let countriesResponse;

const countryPromise = fetch('/fetchcountry');
countryPromise
    .then(result => result.json())
    .then(jsonResult => {
      countriesResponse = jsonResult;

      for (let countryNumber in countriesResponse.Response){
        const countryName = countriesResponse.Response[countryNumber]['Name']
        $('#selectCountry').after('<option value='+countryName+'>'+countryName+'</option>');
      }
    })
