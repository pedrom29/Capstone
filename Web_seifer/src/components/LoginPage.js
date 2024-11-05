import React from 'react';
import { Container, Row, Col, Form, Card, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function LoginPage() {
  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', display: 'flex', alignItems: 'center' }}>
      <Container>
        <Row className="justify-content-center align-items-center">
          {/* Columna del formulario de inicio de sesión */}
          <Col xs={12} md={6} lg={4} className="mb-4">
            <Card style={{ padding: '20px', borderRadius: '10px' }}>
              <h2 className="text-center mb-4" style={{ color: '#316c72' }}>Iniciar Sesión</h2>
              <Form>
                <Form.Group controlId="formBasicEmail" className="mb-3">
                  <Form.Label>Correo Electrónico</Form.Label>
                  <Form.Control type="email" placeholder="Ingrese su correo" />
                </Form.Group>

                <Form.Group controlId="formBasicPassword" className="mb-3">
                  <Form.Label>Contraseña</Form.Label>
                  <Form.Control type="password" placeholder="Ingrese su contraseña" />
                </Form.Group>

                <p className="text-center mt-3" style={{ fontSize: '0.85rem', color: '#555' }}>
                  ¿No tienes cuenta? <Link to="/register" style={{ color: '#316c72', textDecoration: 'underline' }}>Crea una Aquí</Link>
                </p>

                <div className="d-grid">
                  <Button type="submit" variant="primary" style={{ backgroundColor: '#316c72', borderColor: '#316c72' }}>
                    Ingresar
                  </Button>
                </div>
              </Form>
            </Card>
          </Col>

          {/* Columna de la imagen con el enlace al home */}
          <Col xs={12} md={6} lg={4} className="text-center">
            <Link to="/">
              <img
                src="/Logobrand.png" // Ruta de la imagen
                alt="Logo SEIFER"
                style={{ width: '100%', maxWidth: '400px' }} // Tamaño aumentado
              />
            </Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default LoginPage;
