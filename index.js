const button = document.getElementById('inputButton');
const input = document.getElementById('inputText');

function changeIframe(url) {
  document.getElementById("map").src = url;
}

button.addEventListener('click', () => {
  changeIframe('foliumMap.html')
})