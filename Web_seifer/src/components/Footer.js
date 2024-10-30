import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import './Footer.css'; // Archivo CSS para estilizar el footer

function Footer() {
  return (
    <footer className="footer bg-dark text-white py-4">
      <Container>
        <Row>
          <Col md={4}>
            <h5>Sobre Nosotros</h5>
            <p>Somos una tienda comprometida con el medio ambiente, ofreciendo productos ecológicos y sostenibles.</p>
          </Col>
          <Col md={4}>
            <h5>Enlaces Rápidos</h5>
            <ul className="list-unstyled">
              <li><a href="#home" className="text-white">Inicio</a></li>
              <li><a href="#jabon" className="text-white">Jabones</a></li>
              <li><a href="#blog" className="text-white">Blog</a></li>
              <li><a href="#contacto" className="text-white">Contacto</a></li>
            </ul>
          </Col>
          <Col md={4}>
            <h5>Síguenos</h5>
            <ul className="list-unstyled">
              <li><a href="https://www.facebook.com" target="_blank" rel="noreferrer" className="text-white">Facebook</a></li>
              <li><a href="https://www.instagram.com" target="_blank" rel="noreferrer" className="text-white">Instagram</a></li>
              <li><a href="https://www.twitter.com" target="_blank" rel="noreferrer" className="text-white">Twitter</a></li>
            </ul>
          </Col>
        </Row>
        <Row className="text-center mt-4">
          <Col>
            <p>&copy; 2024 Seifer. Todos los derechos reservados.</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
