function c(textToLogToConsole) {
	console.log(textToLogToConsole)
}

async function receiveGetResponseFromServer() {
	async function sendGetRequestFromBrowser() {
		try {
			return (await axios.get('/datarequests')).data
		} catch (e) {
			return null;
		}
	}

	var dataReceivedFromServer = await sendGetRequestFromBrowser();

	c(`Data received from server: ${dataReceivedFromServer}`)
};


function sendPostRequestFromBrowser(spreadsheetType) {

	// Creating a XHR object
	let xhr = new XMLHttpRequest();
	let url = '/datarequests';

	// open a connection
	xhr.open('POST', url, true);

	// Set the request header i.e. which type of content you are sending
	xhr.setRequestHeader('Content-Type', 'application/json');

	// Create a state change callback
	xhr.onreadystatechange = function () {
		if (xhr.readyState === 4 && xhr.status === 200) {

			// Print received data from server
			// result.innerHTML = this.responseText;
			cl('Received data from server: ${this.responseText}')

		}
	};

	// Converting JSON data to string
	var spreadSheetTypePostData = JSON.stringify({ "spreadsheetType": spreadsheetType });

	// Sending data with the request
	xhr.send(spreadSheetTypePostData);
}





function publicClickFunction() {
	sendPostRequestFromBrowser('public');
}


function privateClickFunction() {
	receiveGetResponseFromServer()
	sendPostRequestFromBrowser('private');
}

function reconcileClickFunction() {

}




