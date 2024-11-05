import React from 'react';
import { Navbar, Nav, Form, FormControl, Button, Container } from 'react-bootstrap';
import { FaShoppingCart, FaUser, FaSearch } from 'react-icons/fa';
import { Link } from 'react-router-dom';

function NavbarComponent() {
  return (
    <Navbar expand="lg" style={{ backgroundColor: '#316c72', fontFamily: 'Arial, sans-serif' }}>
      <Container className="align-items-center">
        {/* Logo y Nombre */}
        <Navbar.Brand as={Link} to="/" style={{ fontSize: '1.5rem', color: '#ffffff', display: 'flex', alignItems: 'center' }}>
          <img
            src="/logo.png"
            alt="Logo"
            style={{ width: '30px', height: '30px', marginRight: '10px' }}
          />
          SEIFER
        </Navbar.Brand>
        
        <Navbar.Toggle aria-controls="navbar-nav" />
        
        <Navbar.Collapse id="navbar-nav" className="justify-content-between">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/jabones" style={{ fontSize: '1.1rem', color: '#ffffff' }}>Jabones</Nav.Link>
            <Nav.Link as={Link} to="/ofertas" style={{ fontSize: '1.1rem', color: '#ffffff' }}>Ofertas</Nav.Link>
            <Nav.Link as={Link} to="/blog" style={{ fontSize: '1.1rem', color: '#ffffff' }}>Blog</Nav.Link>
          </Nav>
          
          {/* Barra de búsqueda ampliada */}
          <Form className="d-flex mx-auto" style={{ width: '60%' }}>
            <FormControl
              type="search"
              placeholder="Buscar productos..."
              className="me-2"
              aria-label="Buscar"
            />
            <Button variant="outline-light"><FaSearch /></Button>
          </Form>
          
          <Nav className="ms-auto">
            {/* Enlace al login */}
            <Nav.Link as={Link} to="/login" style={{ color: '#ffffff' }}>
              <FaUser />
            </Nav.Link>
            <Nav.Link as={Link} to="/cart" style={{ color: '#ffffff' }}>
              <FaShoppingCart />
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavbarComponent;
