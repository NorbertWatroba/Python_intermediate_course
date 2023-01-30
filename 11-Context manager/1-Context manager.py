class HtmlCM:
    def __enter__(self):
        print('''<table>
    <tr>
        <th>Number</th><th>Description</th>
    </tr>''')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</table>')


with HtmlCM():
    print('''    <tr>
        <td>1</td><td>Say hello!</td)
    </tr>
    <tr>
        <td>2</td><td>Say good bye!</td)
    </tr>''')
