import React from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import CustomNavbar from './components/Navbar';
import Banner from './components/Banner';
import ProductList from './components/ProductList';
import Footer from './components/Footer';
import LoginPage from './components/LoginPage';
import RegisterPage from './components/RegisterPage';
import JabonesPage from './components/JabonesPage';
import BlogPage from './components/BlogPage.js';
import TermsPage from './components/TermsPage';
import PrivacyPolicyPage from './components/PrivacyPolicyPage';
import CookiesPolicyPage from './components/CookiesPolicyPage';
import { Container, Row, Col } from 'react-bootstrap';

function HomePage() {
  return (
    <Container fluid style={{ paddingTop: '0px', maxWidth: '95%' }}>
      {/* Sección de Banner */}
      <Row className="justify-content-center" style={{ marginTop: '0px' }}>
        <Col xs={12} md={11} lg={10}>
          <Banner />
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
        <Route path="/jabones" element={<JabonesPage />} />
        <Route path="/blog" element={<BlogPage />} />
        <Route path="/condiciones" element={<TermsPage />} />
        <Route path="/privacidad" element={<PrivacyPolicyPage />} />
        <Route path="/cookies" element={<CookiesPolicyPage />} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
