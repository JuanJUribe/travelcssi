const startSection = document.querySelector('#startSection')

let messagesResponse;

const promise = fetch('/fetch-admin-contact');
promise
    .then(result => result.json())
    .then(jsonResult => {
      messagesResponse = jsonResult;
      console.log(messagesResponse)

      for (let messageNum in messagesResponse){
        $('#startSection').after('<section class="messages"><p class="messageEmail">'+messagesResponse[messageNum]['user']+'</p><p class ="messageContent">'+messagesResponse[messageNum]['message']+'</p></section>');
      }
    })
