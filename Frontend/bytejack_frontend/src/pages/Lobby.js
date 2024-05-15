import React from "react";
import "./Lobby.css"
import { useNavigate, useEffect } from "react-router-dom";
import { socket } from "../utils/socket.js";


const Lobby = () => {
    const navigate = useNavigate();
    return (
        <div class="background">
            <link rel="preconnect" href="https://fonts.googleapis.com" />
            <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
            <link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap" rel="stylesheet" />
            
            <h1 class="bungee-spice-regular">
                Available Lobbies
            </h1>
            <button onClick={() => {
                navigate("/table")
                }}>Join</button>
        </div>
        
    )
}
export default Lobby;