from flask import Flask,redirect,render_template,session,url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


class NameForm(Form):
	name=StringField('what is a string?', validators=[Required()])
	submit=SubmitField('Submit')

app=Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap=Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500


@app.route('/',methods=['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		#alpha='abcdefghijklmnopqrstuvwsyx'
		context={}
		name=''.join(name.split())
		for i in name:
			print i,
			count=name.count(i)
			if count>0:
				context[i]=count
		print context
	return render_template('index.html',form=form,name=name, context=context)



@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' %name

if __name__=='__main__':
    app.run(debug=True)
