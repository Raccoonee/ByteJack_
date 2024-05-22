import "./Home.css";
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import BasicModal from "../components/BasicModal";
import axios from "axios";
import RegisterModal from "../components/RegisterModal";
import { socket } from "../utils/socket";

const Home = () => {
  const [open, setOpen] = useState(false);
  const [registerOpen, setResgisterOpen] = useState(false);
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  //Page Redirection Component
  const navigate = useNavigate();


  const handleSocketStatus = (response) => {
    console.log(response);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    socket.emit("login", formData);
    socket.emit("joinLobbyRoom")

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

  const handleUsers = (event) => {
    event.preventDefault();

    axios
      .get(`/getUSERS`)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  };


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
        <button onClick={handleUsers}></button>
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
        <BasicModal open={open} setOpen={setOpen}></BasicModal>
      </div>
    </>
  );
};

export default Home;
