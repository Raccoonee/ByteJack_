import * as React from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Modal from "@mui/material/Modal";
import axios from "axios";
import { useState } from "react";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid darkred",
  boxShadow: 24,
  p: 4,
};

const textStyle = {
  textAlign: "center",
  fontWeight: "bold",
  color: "darkred",
};

export default function RegisterModal({ registerOpen, setRegisterOpen }) {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const handleSubmit = (event) => {
    event.preventDefault();

    axios
      .post(
        `http://backend:8080/register/${formData.username}/${formData.password}`
      )
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <div>
      <Modal
        open={registerOpen}
        onClose={() => {
          setRegisterOpen(false);
        }}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
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
              <span class="button-82-front text">sign-up</span>
            </button>
          </form>
        </Box>
      </Modal>
    </div>
  );
}
