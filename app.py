from flask import Flask
from flask import render_template, request, redirect,url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICTAIONS'] = False
db= SQLAlchemy(app)

class Todo(db.Model):
    task_id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    done = db.Column(db.Boolean)

#Rotas Flask 
@app.route("/")
def index():
    todo_list=Todo.query.all()
    return  render_template('index.html',todo_list = todo_list)

@app.route ('/add',methods=['POST'])
def add():

    name = request.form.get("name")

    if not name:
        flash("O campo 'name' não pode estar vazio.", 'error')
        return redirect(url_for("index"))
    
    name = request.form.get("name")
    new_task = Todo(name = name, done = False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.get(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index"))



@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo= Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))




#rodar a aplicação
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug = True)