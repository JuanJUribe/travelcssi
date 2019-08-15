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

          const newDivv = $('<div/>', {
            class: 'title',
            html: weatherResponse.title
          })
          document.body.append(newDivv[0]);

        const weatherData = weatherResponse.consolidated_weather[0];
          const newDiivv = $('<div/>', {
            class: 'weather',
              html: `<img width=70 src="https://www.metaweather.com/static/img/weather/${weatherData.weather_state_abbr}.svg"><br>
                    Date: ${weatherData.applicable_date}<br>
                    Humidity: ${weatherData.humidity + '%'}<br>`

            })
            document.body.append(newDiivv[0]);


        const newDev = $('<div/>', {
            class: 'sun-rise',
            html: 'Sunrise: ' + weatherResponse.sun_rise.substring(weatherResponse.sun_rise.indexOf("T")+1, weatherResponse.sun_rise.indexOf("."))
          })

          document.body.append(newDev[0]);

          const newDiiv = $('<div/>', {
              class: 'sun-set',
              html: 'Sunset: ' + weatherResponse.sun_set.substring(weatherResponse.sun_set.indexOf("T")+1, weatherResponse.sun_rise.indexOf("."))
            })
            document.body.append(newDiiv[0]);
g
            const newDeb = $('<div/>', {
                class: 'timezone',
                html: 'Time zone: ' + weatherResponse.timezone
              })
              document.body.append(newDeb[0]);
      })
}
