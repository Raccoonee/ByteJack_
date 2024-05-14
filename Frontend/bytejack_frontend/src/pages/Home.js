import "./Home.css";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import BasicModal from "../components/BasicModal";

const Home = () => {
  const userData = {
    Players: ["Jeremiah", "Desmond"],
    Passwords: ["1234", "4321"],
  };

  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  //Page Redirection Component
  const navigate = useNavigate();

  //Modal Component
  const [open, setOpen] = React.useState(false);

  const validateUser = (userInfo, logInfo) => {
    for (let i = 0; i < userInfo.Players.length; i++) {
      if (logInfo.username === userInfo.Players[i]) {
        if (logInfo.password === userInfo.Passwords[i]) {
          navigate("/lobby");
        } else {
          console.log("Couldn't find user");

          console.log(open);
        }
      }
    }

    setOpen(true);
  };

  const handleRegistration = () => {

  }

  const handleSubmit = (event) => {
    event.preventDefault();

    validateUser(userData, formData);
    console.log("Form submitted with data:", formData);
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
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

          <button class="button-82-register">
            <span class="button-82-shadow"></span>
            <span class="button-82-edge"></span>
            <span class="button-82-front text">Register</span>
          </button>
        </p>

        {/* <BasicModal open={open} setOpen={setOpen}></BasicModal> */}
      </div>
    </>
  );
};

export default Home;
