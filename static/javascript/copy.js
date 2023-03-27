'use strict';

let shortUrl = document.getElementById('short-url');

function copyShortFunc() {
  shortUrl.select();
  shortUrl.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(shortUrl.value);
  setTimeout(function(){
      alert('Copied')
    }, 500);
}

