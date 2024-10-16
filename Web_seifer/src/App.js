import React from 'react';
import CustomNavbar from './components/Navbar';
import Banner from './components/Banner';
import ProductList from './components/ProductList';
import Footer from './components/Footer'; // Importamos el componente Footer
import { Container } from 'react-bootstrap';

function App() {
  return (
    <div>
      <CustomNavbar />
      <div style={{ marginTop: '100px' }}> {/* Ajusta el margen superior aquí si es necesario */}
        <Banner />
        <Container className="mt-4">
          <ProductList />
        </Container>
      </div>
      <Footer /> {/* Añadimos el footer aquí */}
    </div>
  );
}

export default App;
