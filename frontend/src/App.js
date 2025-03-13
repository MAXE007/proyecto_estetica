import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ReservaTurno from "./components/ReservaTurno";
import ListaTurnos from "./components/ListaTurnos";
import Register from "./components/Register";
import Login from "./components/Login";
import ProtectedRoute from "./routes/ProtectedRoute";
import Navbar from "./components/Navbar";



function App() {
  return (
    <Router>
      <Navbar />
      <div>
        <h1>Reserva de Turnos</h1>
        <Routes>
          {/* Rutas públicas */}
          <Route path='/register' element={<Register />} />
          <Route path='/login' element={<Login />} />

          {/* Rutas privadas (protegidas) */}
          <Route element={<ProtectedRoute />}>
            <Route path='/' element={<ReservaTurno />} />
            <Route path='/turnos' element={<ListaTurnos />} />
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
