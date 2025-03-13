import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();
  const username = localStorage.getItem("username");

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("username");
    navigate("/login"); // Redirigir al login después de cerrar sesión
  };

  return (
    <nav style={{ display: "flex", justifyContent: "space-between", padding: "10px", background: "#eee" }}>
      <div>
        <Link to="/">Inicio</Link> | <Link to="/turnos">Turnos</Link>
      </div>
      <div>
        {username ? (
          <>
            <span>Bienvenido, {username} </span>
            <button onClick={handleLogout} style={{ marginLeft: "10px" }}>Cerrar Sesión</button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link> | <Link to="/register">Registro</Link>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
