const locationInput = document.querySelector('#location');

let locationsResponse;
let weatherResponse;

locationInput.addEventListener('input', selectCity);

let citySet = new Set([]);
let activated = false;

function selectCity(){
    locationSearch = locationInput.value;
    const promise = fetch('/fetchlocationweather/'+encodeURIComponent(locationSearch));
    promise
        .then(result => result.json())
        .then(jsonResult => {
          locationsResponse = jsonResult;

        for (let location in locationsResponse){
          const cityName = locationsResponse[location]['title'];
          const cityID = locationsResponse[location]['woeid'];

          if (!(citySet.has(cityName))){
              $('#selectInitial').after('<option data-value='+cityID+' id='+cityName+'>'+cityName+'</option>');
              citySet.add(locationsResponse[location]['title']);
          }
          if (cityName === locationSearch && activated === false){
              getWeather(cityID);
              activated = true;
          }else if(cityName !== locationSearch){
            activated = false;
        }
    }
    })
}


function getWeather(locationID){
    const promise = fetch('/fetchweather/'+locationID);
    promise
        .then(result => result.json())
        .then(jsonResult => {
          weatherResponse = jsonResult;
          console.log(weatherResponse);
        })
}
