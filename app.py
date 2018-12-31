        #return render_template('name.html',Firstname = first_name)
		#return render_template('FORM.html')
        #return render_template('name.html',title = title)
        #return render_template('name.html',xlabel = xlabel)
from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import mpld3

app = Flask(__name__)
@app.route('/')
def index():
	return render_template("FORM.html")

@app.route('/send',methods=['POST','GET'])
def send():
	if request.method=='POST':
		
		title = request.form['title']	
		xlabel = request.form['xlabel']
		ylabel = request.form['ylabel']
		xdata = request.form['xdata']
		ydata = request.form['ydata']
		
		
		X = [float(x) for x in xdata.split(",")]
		Y = [float(x) for x in ydata.split(",")]
	
		plt.plot(X,Y)

		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)

		mpld3.show()
		
	return	
app.run(host='0.0.0.0')
