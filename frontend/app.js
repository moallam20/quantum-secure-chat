const socket = io("http://localhost:5000");

socket.on("message", function(msg) {
    document.getElementById("chat").innerHTML += "<p>" + msg + "</p>";
});

function sendMsg() {
    let msg = document.getElementById("msg").value;

    socket.send(msg);

    document.getElementById("chat").innerHTML += "<p>You: " + msg + "</p>";

    document.getElementById("msg").value = "";
}