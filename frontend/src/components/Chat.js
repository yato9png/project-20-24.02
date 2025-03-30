import React, { useState, useEffect } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5000");

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState("");

    useEffect(() => {
        socket.on("receive_message", (data) => {
            setMessages((prev) => [...prev, data]);
        });
    }, []);

    const sendMessage = () => {
        socket.emit("send_message", { content: message });
        setMessage("");
    };

    return (
        <div>
            <div>
                {messages.map((msg, index) => (
                    <p key={index}>{msg.content}</p>
                ))}
            </div>
            <input value={message} onChange={(e) => setMessage(e.target.value)} />
            <button onClick={sendMessage}>Отправить</button>
        </div>
    );
};

export default Chat;
