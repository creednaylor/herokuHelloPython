import flask

flaskApp = flask.Flask(__name__, static_folder='../frontend/', template_folder='../frontend/')
flaskApp.config['TEMPLATES_AUTO_RELOAD'] = True


@flaskApp.route('/getrequest', methods=['GET'])
def respondToGetRequest():

   jsonToSendToFrontend = {
        'cat eyes': 'yellow',
        'collar': 'red'
    }
   
   return str(jsonToSendToFrontend)

 

@flaskApp.route('/postrequest', methods=['POST'])
def respondToPostRequest():

   console.log(request)



@flaskApp.route('/')
def returnMainPage():
   return flask.render_template('index.html')




if __name__ == '__main__':
    
    import waitress
    waitress.serve(flaskApp, host='0.0.0.0', port=8000)

    flaskApp.run()