import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/";

// Función para obtener todos los turnos
export const getTurnos = async () => {
  const token = localStorage.getItem('access_token');
  try {
    const response = await axios.get(`${API_URL}mis-turnos/`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error obteniendo los turnos:", error.response?.data || error.message);
    throw error;
  }
};

// Función para crear un nuevo turno
export const createTurno = async (turnoData) => {
  try {
    const response = await axios.post(`${API_URL}turnos/`, turnoData);
    return response.data;
  } catch (error) {
    console.error("Error creando el turno:", error);
    throw error;
  }
};


//Para registrar un usuario
export const registerUser = async (username, email, password) => {
  try {
    const response = await axios.post(`${API_URL}register/`, {
      username,
      email,
      password
    });
    console.log('Usuario registrado:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error al registrar usuario:', error.response?.data || error.message);
    throw error;
  }
};

//Para que el usuario registrado ingrese
export const loginUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}login/`, {
      username,
      password
    });
    localStorage.setItem('access_token', response.data.access); // Guardar token
    localStorage.setItem('username', username); // Guardar el nombre del usuario

    window.location.reload(); // Recargar la página automáticamente
    return response.data;
  } catch (error) {
    console.error('Error al iniciar sesión:', error.response?.data || error.message);
    throw error;
  }
};