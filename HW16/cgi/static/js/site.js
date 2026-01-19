document.addEventListener("DOMContentLoaded", () => {
  initApi()
});

function initApi() {
  const apiNames = ["user", "order", "discount"];
  const apiMethods = ["get", "post", "put", "patch", "delete"];

  // Add listeners for api buttons
  for (let apiName of apiNames) {
    for (let apiMethod of apiMethods) {
      let btnId = `api-${apiName}-${apiMethod}-btn`;
      let btn = document.getElementById(btnId);
      if (btn) {
        btn.addEventListener("click", apiBtnClick);
      }
    }
  }

  // Add listeners for tests
  const testNames = ["correctAuth", "noAuth", "invalidAuthScheme", "shortAuthData", "invalidBase64"];
  for (let testName of testNames) {
    btn = document.querySelector(`[data-test-name="${testName}"]`);
    if (btn)
      btn.addEventListener("click", apiTestBtnClick);
  }
}

const authorizationTestHeaders = {
  "correctAuth": {
    headers: { Authorization: "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==" }
  },
  "noAuth": {
    headers: {}
  },
  "invalidAuthScheme": {
    headers: { Authorization: "Qwerty QWxhZGRpbjpvcGVuIHNlc2FtZQ==" }
  },
  "shortAuthData": {
    headers: { Authorization: "Basic QWE==" }
  },
  "invalidBase64": {
    headers: { Authorization: "Basic #&*%!?|@" }
  },
}

function apiBtnClick(e) {
  const [prefix, apiName, apiMethod, _] = e.target.id.split("-");
  const resId = `${prefix}-${apiName}-${apiMethod}-result`;
  const td = document.getElementById(resId);

  if (!td) {
    throw "Container not found";
  }

  console.log(prefix, `/${apiName}`, "method: " + apiMethod.toUpperCase())

  let headers = {
    "Access-Control-Allow-Origin": "cgi221.loc",
    "Custom-Header": "My-Value",
    "Authorization": "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=="
  }

  fetch(`/uk-UA/${apiName}`, {
    method: apiMethod.toUpperCase(),
    headers
  })
    .then(r => {
      if (r.ok) {
        r.json().then(j => td.innerHTML = `<div class="json">${JSON.stringify(j, null, 4)}</div>`);
      } else {
        r.text().then(t => td.innerText = t);
      }
    })
    .then(t => td.innerText = t);
}

function apiTestBtnClick(e) {
  const btn = e.currentTarget;
  const dataset = btn.dataset;

  const apiName = dataset.apiName;
  const apiMethod = dataset.apiMethod;
  const testName = dataset.testName;

  const output = btn.closest('tr').querySelector('.api-user-get-result');

  if (!output) {
    throw "Container not found";
  }

  const headers = {
    "Access-Control-Allow-Origin": "cgi221.loc",
    "Custom-Header": "My-Value",
    ...authorizationTestHeaders[testName].headers
  }

  fetch(`/uk-UA/${apiName}`, {
    method: apiMethod.toUpperCase(),
    headers
  })
    .then(r => r.json())
    .then(j => {
      const result = {
        status: j.status,
        data: j.data
      };
      output.innerHTML = `<div class="json">${JSON.stringify(result, null, 4)}</div>`;
    })
    .catch(err => {
      output.innerText = 'Error: ' + err.message;
    });
}