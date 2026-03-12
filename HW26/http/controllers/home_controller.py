from controllers.controller_rest import ControllerRest


class HomeController(ControllerRest):
  def html_params_table(self) -> str:
    table_params = "\n".join(f"""
      <tr>
        <td>{x}</td>
        <td>{self.query_params[x]}</td>
      </tr>
    """ for x in self.query_params)
    
    return f"""
      <table>
        <thead>
          <tr>
            <th>Key</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {table_params}
        </tbody>
      </table>
    """

  def send_success(self):
    self.handler.send_response(200, "OK")
    self.handler.send_header("Content-Type", self.content_type)
    self.handler.end_headers()
    self.handler.wfile.write(self.html.encode())

  def do_GET(self):
    links_html = self.generate_links_html()
    tests_table = self.generate_tests_table()

    cats = """
      <img src="/img/cat.png" alt="cat.png" width=200 />
      <img src="/img/cat.jpg" alt="cat.jpg" width=300 />
      <hr/>
    """

    self.html = f"""
      <title>Title</title>
      <link rel="icon" href="/worst_lang_in_the_world.png" />
      <link rel="stylesheet" href="css/site.css" />
      
      {links_html}
      self.path = {self.handler.path}<br/>
      api = {self.handler.api}<br/>

      <h1>HTTP</h1>
      {cats}
      
      <h2>Результат розбору</h2>
      self.path = {self.handler.path}<br/>
      query_params:
      {("empty" if not self.query_params else self.html_params_table())}                      
      <hr/>

      <button onclick="onClick('LINK')">LINK</button>
      <button onclick="onClick('POST')">POST</button>
      <button onclick="onClick('GET', 'user')">GET user</button>
      <button onclick="onClick('POST', 'user')">POST user</button>
      <button onclick="onClick('GET', 'product')">GET product</button>
      <p id="out"></p>
      <hr/>
      {tests_table}
      <script src="/js/site.js"></script>
    """
    self.content_type = "text/html; charset=utf-8"


  def generate_links_html(self) -> str:
    return """
      <h2>Тестування маршрутів</h2>
      <ul>
        <li><a href="/">Без параметрів</a></li>
        <li><a href="/home/">З сервісом</a></li>
        <li><a href="/home/auth/">З розділами</a></li>
        <li><a href="/home?hash=1a2d==&p=50/50&q=who?&x=10&y=20&x=30&json/">З параметрами та повторами ключів</a></li>
        <li><a href="/home/Уніфікований/">URL-кодованими значеннями</a></li>
      </ul>
    """

  def generate_tests_table(self) -> str:
    tests = [
      ("GET no module", "no", "out_no"),
      ("GET no controller", "noclass", "out_noclass"),
      ("GET no constructor", "noinit", "out_noinit"),
      ("GET no serve method", "noserve", "out_noserve"),
      ("GET exception in serve", "exserve", "out_exserve"),
    ]
    table_rows = "\n".join(f"""
      <tr>
        <td>
          <button onclick="onClickTests('GET', '{service}', '{output_id}')">
            {test_name}
          </button>
        </td>
        <td>
          <p id="{output_id}"/>
        </td>
      </tr>
    """ for test_name, service, output_id in tests)
    
    return f"""
      <table>
        <thead><tr><th>Test</th><th>Output</th></tr></thead>
        <tbody>{table_rows}</tbody>
      </table>
    """

  def do_LINK(self):
    self.html = "LINK method response"
    self.content_type = "text/plain; charset=utf-8"
