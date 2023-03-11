from flask import render_template
from app.questions import bp
from app.models.question import Question
from app.extensions import db

@bp.route('/', methos=('GET', 'POST'))
def index():
	questions = Question.query.all()
	
	if request.method == 'POST':
		new_question = Question(content=request.form['content'],
				answer=request.form['answer'])
		db.session.add(new_question)
		db.session.commit()
		return redirect(url_for('question.index'))
	return render_template('questions/index.html',questions=questions)

