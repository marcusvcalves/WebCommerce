import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Produtos from './Components/produtos/produtos';
import Navbar from './Components/navbar/navbar.tsx';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Navbar />
    <Produtos />
  </React.StrictMode>
);
