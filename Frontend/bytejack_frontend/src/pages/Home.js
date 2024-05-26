import "./Home.css";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import BasicModal from "../components/BasicModal";
import RegisterModal from "../components/RegisterModal";
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import Snackbar from "@mui/material/Snackbar";
import Button from '@mui/material/Button';
import { socket } from "../utils/socket";

const Home = () => {
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const [openSnackBar, setOpenSnackBar] = useState(false);
  const [registerOpen, setResgisterOpen] = useState(false);
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const handleSocketStatus = (response) => {
    console.log(response);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    socket.emit("login", formData);
    socket.emit("joinLobbyRoom");

    socket.on("status", handleSocketStatus);
    socket.on("status2", handleSocketStatus);

    navigate("/lobby");
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpenSnackBar(false);
  }

  const action = (
    <React.Fragment>
      <Button color="secondary" size="small" onClick={handleClose}>
        UNDO
      </Button>
      <IconButton
        size="small"
        aria-label="close"
        color="inherit"
        onClick={handleClose}
      >
        <CloseIcon fontSize="small" />
      </IconButton>
    </React.Fragment>
  );


  return (
    <>
      <div className="App" class="background">
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
        <h1 class="bungee-spice-regular">ByteJack</h1>
        <button onClick={() => {
          setOpenSnackBar(true)
        }}>Snackbar</button>
        <p>
          <form onSubmit={handleSubmit}>
            <div class="Wrapper Input">
              <input
                type="text"
                id="input"
                class="Input-text"
                placeholder="Username"
                name="username"
                value={formData.uername}
                onChange={handleChange}
              ></input>
              <input
                type="password"
                id="input"
                class="Input-text"
                placeholder="Password"
                name="password"
                value={formData.password}
                onChange={handleChange}
              ></input>
            </div>

            <button class="button-82-pushable" type="submit">
              <span class="button-82-shadow"></span>
              <span class="button-82-edge"></span>
              <span class="button-82-front text">Log-in</span>
            </button>
          </form>

          <button
            class="button-82-pushable"
            onClick={() => {
              setResgisterOpen(true);
            }}
          >
            <span class="button-82-shadow"></span>
            <span class="button-82-edge"></span>
            <span class="button-82-front text">Register</span>
          </button>
        </p>
        <RegisterModal
          registerOpen={registerOpen}
          setResgisterOpen={setResgisterOpen}
        ></RegisterModal>
        <Snackbar
          open={openSnackBar}
          autoHideDuration={2000}
          onClose={handleClose}
          message="Note archived"
          action={action}
        />
        <BasicModal open={open} setOpen={setOpen}></BasicModal>
      </div>
    </>
  );
};

export default Home;
