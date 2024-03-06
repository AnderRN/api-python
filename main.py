from flask import Flask, jsonify, request
app= Flask(__name__)

@app.route("/")
def root():
    list=[
        {'name':'anderson'},
        {'name':'andres'},
        {'name':'julian'},
        {'name':'juan'},
        {'name':'pablo'}]
    return jsonify(list)

if __name__ == '__main__':
    app.run(debug=True)