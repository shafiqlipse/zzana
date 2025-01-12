const roomName = "{{ room_name }}"; // Automatically available from the context processor
let chatSocket; // Declare chatSocket only once

function connectWebSocket() {
    chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
    );

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        document.querySelector("#chat-log").value +=
            data.sender + ": " + data.message + "\n";
    };

    chatSocket.onclose = function (e) {
        console.warn("WebSocket closed unexpectedly. Reconnecting...");
        setTimeout(connectWebSocket, 1000); // Retry connection after 1 second
    };

    chatSocket.onerror = function (e) {
        console.error("WebSocket error:", e);
    };
}

// Establish initial connection
connectWebSocket();

document.querySelector("#chat-message-input").focus();
document.querySelector("#chat-message-input").onkeyup = function (e) {
    if (e.key === "Enter") {
        // Press Enter to send the message
        document.querySelector("#chat-message-submit").click();
    }
};

document.querySelector("#chat-message-submit").onclick = function (e) {
    if (chatSocket.readyState === WebSocket.OPEN) {
        const messageInputDom = document.querySelector("#chat-message-input");
        const message = messageInputDom.value;
        chatSocket.send(
            JSON.stringify({
                message: message,
                sender: "{{ user.username }}", // Replace with actual sender
                receiver: "{{ receiver.username }}", // Replace with actual receiver
            })
        );
        messageInputDom.value = "";
    } else {
        console.error("WebSocket is not open. ReadyState:", chatSocket.readyState);
    }
};
