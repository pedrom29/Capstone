import React from 'react';
import { Link } from 'react-router-dom';
import CustomButton from './CustomButton';
import { Container, Form, Row, Col, Card } from 'react-bootstrap';

function LoginPage() {
  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', fontFamily: 'Roboto, sans-serif' }}>
      <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: '80vh' }}>
        <Row className="justify-content-center w-100">
          <Col xs={12} md={6} lg={4}>
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

                {/* Texto de registro debajo del campo de contraseña */}
                <p className="text-center mt-3">
                  ¿No tienes cuenta? <Link to="/register" style={{ color: '#316c72', textDecoration: 'underline' }}>Crea una Aquí</Link>
                </p>

                <div className="d-grid">
                  <CustomButton type="submit">Ingresar</CustomButton>
                </div>
              </Form>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default LoginPage;
