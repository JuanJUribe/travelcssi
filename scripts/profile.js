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

      console.log(countriesResponse)

      for (let countryNumber in countriesResponse.Response){
        const countryName = countriesResponse.Response[countryNumber]['Name']
        const countryLang = countriesResponse.Response[countryNumber]['Alpha2Code'].toLowerCase()
        $('#selectCountry').after('<option value='+countryName+':'+countryLang+'>'+countryName+'</option>');
      }
    })

// let countriesResponse;
//
// const languagePromise = fetch('');
// languagePromise
//     .then(result => result.json())
//     .then(jsonResult => {
//       languagesResponse = jsonResult;
//
//       for (let language in languagesResponse.Response){
//         const countryName = countriesResponse.Response[countryNumber]['Name']
//         $('#selectLanguage').after('<option value='+countryName+'>'+countryName+'</option>');
//       }
//     })
