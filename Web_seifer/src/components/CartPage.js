import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import NavbarComponent from './Navbar'; // Asegúrate de importar el Navbar
import './CartPage.css'; // Archivo CSS para personalización (opcional)

function CartPage() {
  return (
    <>
      {/* Navbar */}
      <NavbarComponent />

      {/* Contenido del carrito */}
      <Container
        className="d-flex flex-column align-items-center justify-content-center"
        style={{ minHeight: '80vh', paddingTop: '56px' }} // Ajusta el margen para no solapar con el navbar fijo
      >
        <Row className="text-center">
          <Col>
            <img
              src={`${process.env.PUBLIC_URL}/empty-cart.png`}
              alt="Carro vacío"
              style={{
                width: '300px', // Ajusta el tamaño aquí
                marginBottom: '20px',
              }}
            />
            <h3 style={{ fontWeight: 'bold', marginBottom: '10px' }}>Tu Carro está vacío</h3>
            <p style={{ color: '#555' }}>Inicia sesión para ver los productos que habías guardado en tu Carro.</p>
            <Button
              as={Link}
              to="/login"
              style={{
                backgroundColor: '#316c72', // Color estándar de la página
                borderColor: '#316c72',
                color: '#fff',
                padding: '10px 20px',
                fontSize: '1rem',
                marginBottom: '10px',
              }}
            >
              Iniciar sesión
            </Button>
            <p>
              ¿No tienes cuenta?{' '}
              <Link to="/register" style={{ color: '#316c72', textDecoration: 'underline' }}>
                Regístrate
              </Link>
            </p>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default CartPage;
