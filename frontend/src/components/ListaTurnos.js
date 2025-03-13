import React, { useEffect, useState } from "react";
import { getTurnos } from "../services/api";

const ListaTurnos = () => {
  const [turnos, setTurnos] = useState([]);

  useEffect(() => {
    const fetchTurnos = async () => {
      const data = await getTurnos();
      setTurnos(data);
    };
    fetchTurnos();
  }, []);

  return (
    <div>
      <h2>Turnos Reservados</h2>
      <ul>
        {turnos.length > 0 ? (
          turnos.map((turno) => (
            <li key={turno.id}>
              Cliente: {turno.cliente} - Fecha: {turno.fecha} - Hora: {turno.hora}
            </li>
          ))
        ) : (
          <p>No hay turnos reservados aún.</p>
        )}
      </ul>
    </div>
  );
};

export default ListaTurnos;
