from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)
    data = response.text.strip().split('\n')

    personas = []
    for linea in data:
        partes = linea.strip().split("|")
        if partes and partes[0][0] in ['3', '4', '5', '7']:
            if len(partes) >= 3:  # asegurarse que haya al menos 3 columnas
                id_persona = partes[0]
                nombre = partes[1]
                ciudad = partes[2]
                personas.append([id_persona, nombre, ciudad])

    html = '''
    <html>
        <head>
            <title>Tabla de Personas</title>
            <style>
                table { border-collapse: collapse; width: 90%; margin: auto; }
                th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h2 style="text-align:center;">Personas con ID que empieza en 3, 4, 5 o 7</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Ciudad</th>
                </tr>
                {% for persona in personas %}
                <tr>
                    <td>{{ persona[0] }}</td>
                    <td>{{ persona[1] }}</td>
                    <td>{{ persona[2] }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
    </html>
    '''
    return render_template_string(html, personas=personas)

if __name__ == '__main__':
    app.run(debug=True)