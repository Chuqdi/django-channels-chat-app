let username = JSON.parse(document.getElementById("username")!.textContent!);
let chat_room:string = JSON.parse(document.getElementById("chat_room")!.textContent!);

let websocketUrl = `ws://${window.location.host}/ws/chat/${chat_room}/${username}/`;
let chatSocket = new WebSocket(websocketUrl);
chatSocket.onmessage = (e)=>{
    var data:{ message?:string, username?:string } = JSON.parse(e.data);
    console.log(data)
    const { message, username } = data;

    if(username){
        messages.innerText+=`${messages.innerText}
        \n
        ${username}:${message}
        `
        return;
    }

    if(message == "Subsription to room java succesful"){
        console.log("Connection secured")
    }
}


let messages = document.getElementById("messages") as HTMLTextAreaElement;
let message = document.getElementById("message") as HTMLInputElement;
let form = document.getElementById("form") as HTMLFormElement;

form.onsubmit = (e:Event)=>{
    e.preventDefault();
    if (message.value.length > 1){
        chatSocket.send(JSON.stringify({
            "message":message.value,
            username
        }))
    }
}
