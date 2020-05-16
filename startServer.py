import flask

flaskApp = flask.Flask(__name__, static_folder='frontend')
# print(flaskApp.static_folder)

@flaskApp.route('/cat')
def returnCatDetails():

   jsonToReturn = {
        'cat eyes': 'yellow',
        'collar': 'red'
    }
   
   return str(jsonToReturn)



# @flaskApp.route('/<path:fileName>', defaults={'fileName': 'index.html'})
# def returnMainPage(fileName):

#    # print(fileName)
#    return flask.send_from_directory(flaskApp.static_folder, fileName)
   


@flaskApp.route('/')
def returnMainPage():
   return flask.render_template('index.html')




if __name__ == '__main__':
    
    from waitress import serve
    serve(flaskApp, host='0.0.0.0', port=8000)

    flaskApp.run()