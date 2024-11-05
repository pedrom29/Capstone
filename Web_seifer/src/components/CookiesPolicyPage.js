import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function CookiesPolicyPage() {
  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', display: 'flex', alignItems: 'center' }}>
      <Container>
        <Row className="justify-content-center align-items-center">
          {/* Columna del texto de política de cookies */}
          <Col xs={12} md={6} lg={4} className="mb-4">
            <Card style={{ padding: '20px', borderRadius: '10px' }}>
              <h2 className="text-center mb-4" style={{ color: '#316c72' }}>Política de Cookies</h2>
              <p>
                Utilizamos cookies para mejorar tu experiencia en nuestro sitio web. En esta política, te explicamos cómo y por qué utilizamos cookies.
              </p>
              <p>
                <strong>Qué son las cookies:</strong> Las cookies son pequeños archivos de texto que se almacenan en tu dispositivo al visitar nuestro sitio web.
              </p>
              <p>
                <strong>Tipos de cookies:</strong> Utilizamos cookies necesarias para el funcionamiento del sitio y cookies analíticas para mejorar el rendimiento.
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

export default CookiesPolicyPage;
