from flask import Flask
from flask import render_template

app = Flask(__name__)



#Rotas Flask 
@app.route("/")
def index():
    return  render_template('index.html')



#rodar a aplicação
if __name__ == "__main__":
    app.run(debug = True)