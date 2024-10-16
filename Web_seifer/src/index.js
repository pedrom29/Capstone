import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Si tienes un archivo CSS adicional
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css'; // Asegúrate de que esta línea esté aquí

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
