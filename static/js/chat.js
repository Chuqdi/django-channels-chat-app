"use strict";
var username = JSON.parse(document.getElementById("username").textContent);
var chat_room = JSON.parse(document.getElementById("chat_room").textContent);
var websocketUrl = "ws://" + window.location.host + "/ws/chat/" + chat_room + "/" + username + "/";
var chatSocket = new WebSocket(websocketUrl);
chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    console.log(data);
    var message = data.message, username = data.username;
    if (username) {
        messages.innerText += messages.innerText + "\n        \n\n        " + username + ":" + message + "\n        ";
        return;
    }
    if (message == "Subsription to room java succesful") {
        console.log("Connection secured");
    }
};
var messages = document.getElementById("messages");
var message = document.getElementById("message");
var form = document.getElementById("form");
form.onsubmit = function (e) {
    e.preventDefault();
    if (message.value.length > 1) {
        chatSocket.send(JSON.stringify({
            "message": message.value,
            username: username
        }));
    }
};
