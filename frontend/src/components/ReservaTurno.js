import React, { useState } from "react";
import axios from "axios";

const ReservaTurno = () => {
  const [fecha, setFecha] = useState("");
  const [hora, setHora] = useState("");
  const [mensaje, setMensaje] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const nuevoTurno = {
      cliente: 1, // Reemplaza con el ID del cliente autenticado
      fecha,
      hora,
      estado: "pendiente",
    };

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/turnos/", nuevoTurno);
      setMensaje(`Turno reservado con éxito para el dia ${response.data.fecha} a las ${response.data.hora} `);
      setFecha("");
      setHora("");
    } catch (error) {
      console.error("Error al reservar turno:", error);
      setMensaje("Hubo un error al reservar el turno.");
    }
  };

  return (
    <div>
      <h2>Reservar Turno</h2>
      {mensaje && <p>{mensaje}</p>}
      <form onSubmit={handleSubmit}>
        <label>Fecha:</label>
        <input type="date" value={fecha} onChange={(e) => setFecha(e.target.value)} required />
        <label>Hora:</label>
        <input type="time" value={hora} onChange={(e) => setHora(e.target.value)} required />
        <button type="submit">Reservar</button>
      </form>
    </div>
  );
};

export default ReservaTurno;
