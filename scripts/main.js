window.onload = function() {
  let booking = document.querySelector(".booking")

  booking.addEventListener('click', bookingRedirect);

  function bookingRedirect() {
    let loc = window.location.pathname;
    let dir = loc.substring(0, loc.lastIndexOf('/'));
    window.location.href = dir + "/booking";
  }
 // ---
 let currency = document.querySelector(".currency")

 currency.addEventListener('click', currencyRedirect);

 function currencyRedirect() {
   let loc = window.location.pathname;
   let dir = loc.substring(0, loc.lastIndexOf('/'));
   window.location.href = dir + "/currency-exchange";
 }
 // ---

 // ---
 let translator = document.querySelector(".translator")

 translator.addEventListener('click', translatorRedirect);

 function translatorRedirect() {
   let loc = window.location.pathname;
   let dir = loc.substring(0, loc.lastIndexOf('/'));
   window.location.href = dir + "/translate";
 }
 // ---
 // ---
 let weather = document.querySelector(".weather")

 weather.addEventListener('click', weatherRedirect);

 function weatherRedirect() {
   let loc = window.location.pathname;
   let dir = loc.substring(0, loc.lastIndexOf('/'));
   window.location.href = dir + "/weather";
 }
 // ---



}
