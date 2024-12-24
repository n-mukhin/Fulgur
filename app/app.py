from flask import Flask, render_template, Response
from diagrams.component_diagram import generate_component_diagram
from diagrams.use_case_diagram import generate_use_case_diagram

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/component_diagram')
def component_diagram():
    svg = generate_component_diagram()
    return Response(svg, mimetype='image/svg+xml')

@app.route('/use_case_diagram')
def use_case_diagram():
    svg = generate_use_case_diagram()
    return Response(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
