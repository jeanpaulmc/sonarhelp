/*document.getElementById("mensaje").onsubmit = function (e) {
    e.preventDefault();
    fetch('/authenticate/login', {
        method: 'POST',
        body: JSON.stringify({
            'mensaje': document.getElementById('mensaje').value,
            'password': document.getElementById('password').value
        }),
        headers: {
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
        return response.json()
    }).then(function (jsonResponse) {
        console.log(jsonResponse)
        if (jsonResponse['error'] === false) {
            alert("Te logeaste")
            document.getElementById("error").className = 'hidden'
        } else {
            document.getElementById("error").className = ''
            document.getElementById("error").innerHTML = jsonResponse['error_message']
        }
    }).catch(function (error) {
        console.log(error)
        document.getElementById("error").className = ''
    });
}*/