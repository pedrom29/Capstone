import React from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import CustomNavbar from './components/Navbar';
import Banner from './components/Banner';
import ProductList from './components/ProductList';
import Footer from './components/Footer';
import LoginPage from './components/LoginPage';
import RegisterPage from './components/RegisterPage';
import { Container, Button, Row, Col } from 'react-bootstrap';

function HomePage() {
  return (
    <Container fluid style={{ paddingTop: '0px', maxWidth: '95%' }}>
      {/* Sección de Banner */}
      <Row className="justify-content-center" style={{ marginTop: '0px' }}>
        <Col xs={12} md={11} lg={10}>
          <Banner />
        </Col>
      </Row>

      {/* Botones de Jabones y Blog centrados y responsivos */}
      <Row className="justify-content-center mt-2 mb-3">
        <Col xs="auto">
          <Button variant="primary" className="mx-1">Jabones</Button>
        </Col>
        <Col xs="auto">
          <Button variant="secondary" className="mx-1">Blog</Button>
        </Col>
      </Row>

      {/* Lista de Productos centrada y responsiva */}
      <Row className="justify-content-center">
        <Col xs={12} md={11} lg={10}>
          <ProductList />
        </Col>
      </Row>
    </Container>
  );
}

function App() {
  const location = useLocation();

  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh', fontFamily: 'Roboto, sans-serif' }}>
      {/* Mostrar CustomNavbar solo en la página principal */}
      {location.pathname === '/' && <CustomNavbar />}

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
