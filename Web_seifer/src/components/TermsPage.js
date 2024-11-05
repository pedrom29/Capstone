import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function TermsPage() {
  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', display: 'flex', alignItems: 'center' }}>
      <Container>
        <Row className="justify-content-center align-items-center">
          {/* Columna del texto de condiciones */}
          <Col xs={12} md={6} lg={4} className="mb-4">
            <Card style={{ padding: '20px', borderRadius: '10px' }}>
              <h2 className="text-center mb-4" style={{ color: '#316c72' }}>Condiciones</h2>
              <p>
                Bienvenido a nuestra página de condiciones. Aquí encontrarás los términos y condiciones de uso de nuestro sitio web. Asegúrate de leer y comprender nuestras políticas antes de usar nuestros servicios.
              </p>
              <p>
                <strong>Condiciones de uso:</strong> Al usar nuestro sitio web, aceptas cumplir con nuestras condiciones y políticas. Estas incluyen el uso responsable y respetuoso de nuestra plataforma y el cumplimiento de las normativas aplicables.
              </p>
              <p>
                <strong>Modificaciones:</strong> Nos reservamos el derecho de modificar estas condiciones en cualquier momento, por lo que te recomendamos revisarlas periódicamente.
              </p>
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

export default TermsPage;
