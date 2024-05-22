import { useState } from "react";
import "./Lobby.css";
import { useNavigate } from "react-router-dom";
import { socket } from "../utils/socket.js";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";
import { ListItemButton } from "@mui/material";
import { FixedSizeList, ListChildComponentProps } from "react-window";
import axios from "axios";

const Lobby = ({ userData, setUserData }) => {
  const navigate = useNavigate();
  const [lobbyList, setLobbyList] = useState(["No Lobbies Found"]);

  const handleJoinLobby = (lobbyID) => {
    console.log(lobbyList);
    if((lobbyList != "No Lobbies Found"))
    {
      setUserData({
        gameID: lobbyID,
      });
      navigate("/table");
    }
  };

  const handleSocketStatus = (response) => {
    console.log(response);
  };

  const handleSocketData = (data) => {
    console.log(data)
    setLobbyList(data.lobbies)
  }

  const handleRefresh = () => {
    socket.emit("lobbies", handleSocketData)
    socket.on("status", handleSocketStatus);

  };

  const handleCreateLobby = () => {
    socket.emit("makeLobby")
    socket.on("status", handleSocketStatus);

  };

  return (
    <div class="background">
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link
        rel="preconnect"
        href="https://fonts.gstatic.com"
        crossOrigin="true"
      />
      <link
        href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap"
        rel="stylesheet"
      />
      <div>
        <h1 class="bungee-spice-regular">Available Lobbies</h1>
      </div>
      <div className="lobby-list">
        <button onClick={handleRefresh}>Refesh</button>
        <button onClick={handleCreateLobby}>Create Lobby</button>
        <List
          sx={{
            width: "100%",
            maxWidth: 360,
            bgcolor: "background.paper",
            position: "relative",
            overflow: "auto",
            maxHeight: 300,
            "& ul": { padding: 0 },
          }}
          subheader={<li />}
        >
          <li>
            <ul>
              {lobbyList.map((lobbyID) => (
                <ListItem key={`${lobbyID}`}>
                  <ListItemButton onClick={() => handleJoinLobby(lobbyID)}>
                    <ListItemText primary={`Lobby: ${lobbyID}`} />
                  </ListItemButton>
                </ListItem>
              ))}
            </ul>
          </li>
        </List>
      </div>
    </div>
  );
};
export default Lobby;
