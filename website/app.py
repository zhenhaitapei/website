from flask import Flask, request, send_from_directory, render_template
import requests
import json

app = Flask(__name__)
feedback_url = 'https://hooks.slack.com/services/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'


@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    message = request.form.get('message', '')
    data = {'name': name,
            'email': email,
            'phone': phone,
            'message': message}
    text = '```{0}```'.format(json.dumps(data))

    r = requests.post(feedback_url, json={'text': text})
    return ('', 204)

@app.route('/', defaults=dict(path=None))
@app.route('/<path:path>')
def send_statics(path):
    path = path or 'index.html'
    return send_from_directory('src/HTML', path)
