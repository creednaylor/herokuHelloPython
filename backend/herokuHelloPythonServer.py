from flask import Flask, request, render_template
from pprint import pprint as p

flaskApp = Flask(__name__, static_folder='../frontend/', template_folder='../frontend/htmlTemplates')
flaskApp.config['TEMPLATES_AUTO_RELOAD'] = True


@flaskApp.route('/datarequests', methods=['GET', 'POST'])
def datarequests():

	if request.method == 'GET':

		dataToSendToFrontend = {
			'cat eyes': 'yellow',
			'collar': 'red'
		}

		return str(dataToSendToFrontend)


	if request.method == 'POST':
		requestObj = request.json

		if requestObj['spreadsheetType'] == 'public':
			p('begin rendering...')
			return render_template('result.html')

		return 'Received data from browser: {}'.format(requestObj['spreadsheetType'])


@flaskApp.route('/')
def returnMainPage():
	return render_template('index.html')



if __name__ == '__main__':

    import waitress
    waitress.serve(flaskApp, host='0.0.0.0', port=8000)

    flaskApp.run()
