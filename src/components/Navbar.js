import React from 'react';
import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap';
import { FaSearch, FaUser, FaShoppingCart } from 'react-icons/fa'; // Importamos los íconos necesarios
import './Navbar.css'; // Archivo CSS para ajustes adicionales

function CustomNavbar() {
  return (
    <Navbar  expand="lg" fixed="top" className="rounded-navbar">
      <Navbar.Brand href="#home">
        <img
          src={`${process.env.PUBLIC_URL}/Logo.png`} // Ruta del logo
          width="40"
          height="40"
          className="d-inline-block align-top"
          alt="Seifer Logo"
        />{' '}
        SEIFER
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav" className="justify-content-between">
        <Nav className="mr-auto">
          <Nav.Link href="#jabon">Jabones</Nav.Link>
          <Nav.Link href="#ofertas">Ofertas</Nav.Link>
        </Nav>
        <Form inline className="search-form">
          <FormControl type="text" placeholder="Buscar" className="mr-sm-2" />
          <Button variant="outline-info">
            <FaSearch /> {/* Reemplaza el botón de texto por el ícono de lupa */}
          </Button>
        </Form>
        <Nav className="ml-auto nav-icons"> {/* Este div controla los íconos */}
          <Nav.Link href="#user">
            <FaUser size={20} /> {/* Ícono de usuario */}
          </Nav.Link>
          <Nav.Link href="#cart">
            <FaShoppingCart size={20} /> {/* Ícono de carrito de compras */}
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default CustomNavbar;
