import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function PrivacyPolicyPage() {
  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', display: 'flex', alignItems: 'center' }}>
      <Container>
        <Row className="justify-content-center align-items-center">
          {/* Columna del texto de política de privacidad */}
          <Col xs={12} md={6} lg={4} className="mb-4">
            <Card style={{ padding: '20px', borderRadius: '10px' }}>
              <h2 className="text-center mb-4" style={{ color: '#316c72' }}>Política de Privacidad</h2>
              <p>
                Tu privacidad es importante para nosotros. En esta política de privacidad, explicamos cómo recopilamos, utilizamos y protegemos tu información personal.
              </p>
              <p>
                <strong>Recopilación de datos:</strong> Recopilamos información que nos proporcionas al registrarte en nuestro sitio, incluyendo nombre, correo electrónico y teléfono.
              </p>
              <p>
                <strong>Uso de datos:</strong> Utilizamos tu información para mejorar nuestros servicios y ofrecerte una experiencia personalizada.
              </p>
            </Card>
          </Col>

          {/* Columna de la imagen con el enlace al home */}
          <Col xs={12} md={6} lg={4} className="text-center">
            <Link to="/">
              <img
                src="/Logobrand.png"
                alt="Logo SEIFER"
                style={{ width: '100%', maxWidth: '400px' }}
              />
            </Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default PrivacyPolicyPage;
