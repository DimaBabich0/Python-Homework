document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById('query-button')
  if (btn) {
    btn.addEventListener('click', onSendClick);
  }
});

function onSendClick() {
  const input = document.getElementById('query-data')
  if (!input) {
    throw "#query-data not found";
  }
  let url = window.location.href;
  console.log("Current URL:", url);
  url = url.split('?')[0];
  url += "?x=" + encodeURIComponent(input.value);
  console.log("New URL:", url);
  setTimeout(() => { window.location = url; }, 3000);
}