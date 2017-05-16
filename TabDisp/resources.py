html_string = """
<body class="large-screen">
  <div class="wrap">
    <div class="table-wrapper">
      <table class="table-responsive card-list-table">
        <thead>
          <tr>
            <th>Symbol</th>
            <th>LTP</th>
            <th>% Change</th>
            <th>Traded Qty</th>
            <th>Value in Lakhs</th>
            <th>Open</th>
            <th>High</th>
            <th>Low</th>
            <th>Prev. Close</th>
            <th>Latest Ex. date</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>

          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
          <tr>
            <td data-title="Column #1">{}</td>
            <td data-title="Column #2">{}</td>
            <td data-title="Column #3">{}</td>
            <td data-title="Column #4">{}</td>
            <td data-title="Column #5">{}</td>
            <td data-title="Column #6">{}</td>
            <td data-title="Column #7">{}</td>
            <td data-title="Column #8">{}</td>
            <td data-title="Column #9">{}</td>
            <td data-title="Column #10">{}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</body>
<br/>
<br/>
"""
items_label = ['Symbol', 'LTP', '% Change', 'Traded Qty', 'Value', 'Open', 'High', 'Low', 'Close', 'Latest Ex Date']
prod_index = 1
TIME = 300 # 5 minutes in seconds