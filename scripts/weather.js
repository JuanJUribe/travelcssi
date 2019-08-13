const locationInput = document.querySelector('#location');

let locationsResponse;

locationInput.addEventListener('input', selectCity);

function selectCity(){
    $('.option').remove()
    locationSearch = locationInput.value;
    const promise = fetch('/fetchweather/'+locationSearch);
    promise
        .then(result => result.json())
        .then(jsonResult => {
          locationsResponse = jsonResult;

        for (let location in locationsResponse){
            $('#selectInitial').after('<option class="option" data-value='+locationsResponse[location]['woeid']+'>'+locationsResponse[location]['title']+'</option>');
            }
        })
}
