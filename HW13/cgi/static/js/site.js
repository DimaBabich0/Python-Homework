document.addEventListener("DOMContentLoaded", () => {
  initApiTests()
});

function initApiTests() {
  const apiNames = ["user", "order"];
  const apiMethods = ["get", "post", "put", "patch", "delete"];

  for (let apiName of apiNames) {
    for (let apiMethod of apiMethods) {
      let btnId = `api-${apiName}-${apiMethod}-btn`;
      let btn = document.getElementById(btnId);
      if (btn) {
        btn.addEventListener("click", apiTestBtnClick);
      }
    }
  }
}

function apiTestBtnClick(e) {
  const [prefix, apiName, apiMethod, _] = e.target.id.split("-");
  const resId = `${prefix}-${apiName}-${apiMethod}-result`;
  const td = document.getElementById(resId);

  if (td) {
    console.log(prefix, `/${apiName}`, "method: " + apiMethod.toUpperCase())

    let headers = {
      "Access-Control-Allow-Origin": "cgi221.loc",
      "Authorization": "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=="
    }

    if (apiMethod === "get" || apiMethod === "post") {
      headers["Custom-Header"] = "My-Value";
    }

    fetch(`/uk-UA/${apiName}`, {
      method: apiMethod.toUpperCase(),
      headers
    })
      .then(r => {
        if (r.ok) {
          r.json().then(j => td.innerHTML = `<div class="td-scroll">${JSON.stringify(j, null, 4)}</div>`);
        } else {
          r.text().then(t => td.innerText = t);
        }
      })
      .then(t => td.innerText = t);
  } else {
    throw "Container not found: " + resId;
  }
}