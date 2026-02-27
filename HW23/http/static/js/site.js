function linkClick() {
  fetch("/", {
    method: "LINK",
  }).then(r => r.text()).then(t => out.innerText = t);
}