from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# database model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    
    
@app.route('/')
def index():
    # all the todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)



# run the app
if __name__ == '__main__':
    with app.app_context():    
        db.create_all()
        
        # dummy todo
        # new_todo = Todo(title = 'todo1', complete = False)
        # db.session.add(new_todo)
        # db.session.commit()
    app.run(debug=True)