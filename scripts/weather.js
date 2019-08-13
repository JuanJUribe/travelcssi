const locationInput = document.querySelector('#location');

let locationsResponse;

locationInput.addEventListener('input', selectCity);

let citySet = new Set([]);

function selectCity(){
    locationSearch = locationInput.value;
    const promise = fetch('/fetchlocationweather/'+locationSearch);
    promise
        .then(result => result.json())
        .then(jsonResult => {
          locationsResponse = jsonResult;

        for (let location in locationsResponse){
          if (!(citySet.has(locationsResponse[location]['title']))){
            $('#selectInitial').after('<option class="option" data-value='+locationsResponse[location]['woeid']+'>'+locationsResponse[location]['title']+'</option>');
            citySet.add(locationsResponse[location]['title']);
            }
            // = document.querySelector('');
            // = addEventListener('click',getWeather);
          }
        })
}

// function getWeather(){
//
// }
