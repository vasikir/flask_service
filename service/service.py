from flask import Flask, jsonify, abort

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

person_dict = {
    "1": "Иванов Сергей Иванович",
    "2": "Петров Николай Семенович"
}

@app.route('/person/<person_id>', methods=['GET'])
def get_person(person_id):
    person = person_dict.get(person_id)
    if person is None:
        abort(404)
    return jsonify({'ФИО': person})

if __name__ == '__main__':
    app.run(debug=True)