import React from 'react';
import { Container, Form, Row, Col, Card } from 'react-bootstrap';
import CustomButton from './CustomButton';

function RegisterPage() {
  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', fontFamily: 'Roboto, sans-serif' }}>
      <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: '80vh' }}>
        <Row className="justify-content-center w-100">
          <Col xs={12} md={6} lg={4}>
            <Card style={{ padding: '20px', borderRadius: '10px' }}>
              <h2 className="text-center mb-4" style={{ color: '#316c72' }}>Crear Cuenta</h2>
              <Form>
                <Form.Group controlId="formFirstName" className="mb-3">
                  <Form.Label>Nombre</Form.Label>
                  <Form.Control type="text" placeholder="Ingrese su nombre" />
                </Form.Group>

                <Form.Group controlId="formLastName" className="mb-3">
                  <Form.Label>Apellido</Form.Label>
                  <Form.Control type="text" placeholder="Ingrese su apellido" />
                </Form.Group>

                <Form.Group controlId="formPhone" className="mb-3">
                  <Form.Label>Teléfono</Form.Label>
                  <Form.Control type="tel" placeholder="Ingrese su número de teléfono" />
                </Form.Group>

                <Form.Group controlId="formEmail" className="mb-3">
                  <Form.Label>Correo Electrónico</Form.Label>
                  <Form.Control type="email" placeholder="Ingrese su correo electrónico" />
                </Form.Group>

                {/* Texto de términos y condiciones */}
                <p className="text-center mt-3" style={{ fontSize: '0.85rem', color: '#555' }}>
                  Al hacer clic en "Registrarse", aceptas nuestras <a href="#" style={{ color: '#316c72' }}>Condiciones</a>, la <a href="#" style={{ color: '#316c72' }}>Política de privacidad</a> y la <a href="#" style={{ color: '#316c72' }}>Política de cookies</a>. Es posible que te enviemos notificaciones por SMS, que puedes desactivar cuando quieras.
                </p>

                <div className="d-grid">
                  <CustomButton type="submit">Registrarse</CustomButton>
                </div>
              </Form>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default RegisterPage;
