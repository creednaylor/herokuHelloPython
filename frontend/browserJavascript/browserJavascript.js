(async function main() {
  async function getRequestFunction() {
    try {
      return (await axios.get('/getrequest')).data
    } catch(e) {
      return null;
    }
  }
  
  var jsonFromBackend = await getRequestFunction();

  console.log(jsonFromBackend)
})()
