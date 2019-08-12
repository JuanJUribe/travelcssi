const locationInput = document.querySelector('#location');

let locationsResponse;

const promise = fetch('/fetchweather');
promise
    .then(result => result.json())
    .then(jsonResult => {
      locationsResponse = jsonResult;

    for (let location in locationsResponse){
        $('#selectInitial').after('<option data-value='+locationsResponse[location]['woeid']+'>'+locationsResponse[location]['title']+'</option>');
        console.log(location);
        }
    })

locationInput.addEventListener('input', selectCity);

function selectCity(){

  const locationID = locationInput.dataValue;

  console.log(locationID);
}
