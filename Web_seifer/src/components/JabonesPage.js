import React, { useState } from 'react';
import { Container, Row, Col, Card, Dropdown, ButtonGroup, Button } from 'react-bootstrap';
import CustomNavbar from './Navbar'; // Importa el navbar

const products = Array.from({ length: 30 }, (_, index) => ({
  id: index + 1,
  name: `Jabón en barra Verbena ${index + 1}`,
  price: Math.floor(Math.random() * 10000) + 5000,
  imageUrl: 'https://via.placeholder.com/150', // Imagen de muestra, reemplazar con URL real si es necesario
  rating: Math.floor(Math.random() * 5) + 1,
  reviews: Math.floor(Math.random() * 100) + 1,
  discount: index % 3 === 0 ? `${Math.floor(Math.random() * 50) + 10}%` : null,
}));

function JabonesPage() {
  const [sortOption, setSortOption] = useState('Recomendados');

  const handleSort = (option) => {
    setSortOption(option);
    if (option === 'Precio: menor a mayor') {
      products.sort((a, b) => a.price - b.price);
    } else if (option === 'Precio: mayor a menor') {
      products.sort((a, b) => b.price - a.price);
    } else if (option === 'Ofertas') {
      products.sort((b, a) => (b.discount ? -1 : 1)); // Coloca productos con descuento primero
    }
  };

  return (
    <div style={{ backgroundColor: '#d9d9d9', minHeight: '100vh' }}>
      <CustomNavbar /> {/* Añade el navbar aquí */}

      <Container className="mt-4">
        <Row className="justify-content-between align-items-center mb-3">
          <Col xs={12} md={6}>
            <h4>Ordenar por:</h4>
            <Dropdown as={ButtonGroup} onSelect={handleSort}>
              <Dropdown.Toggle variant="light" id="dropdown-sort">
                {sortOption}
              </Dropdown.Toggle>
              <Dropdown.Menu>
                <Dropdown.Item eventKey="Precio: menor a mayor">Precio: menor a mayor</Dropdown.Item>
                <Dropdown.Item eventKey="Precio: mayor a menor">Precio: mayor a menor</Dropdown.Item>
                <Dropdown.Item eventKey="Recomendados">Recomendados</Dropdown.Item>
                <Dropdown.Item eventKey="Ofertas">Ofertas</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          </Col>
        </Row>

        <Row>
          {products.map((product) => (
            <Col key={product.id} xs={12} sm={6} md={4} lg={3} className="mb-4">
              <Card className="h-100 shadow-sm position-relative">
                {/* Marca de oferta */}
                {product.discount && (
                  <div style={{
                    position: 'absolute',
                    top: '10px',
                    left: '10px',
                    backgroundColor: 'red',
                    color: 'white',
                    padding: '5px 10px',
                    borderRadius: '5px',
                    fontSize: '0.8rem',
                    fontWeight: 'bold',
                  }}>
                    Oferta
                  </div>
                )}
                <Card.Img variant="top" src={product.imageUrl} alt={product.name} />
                <Card.Body className="d-flex flex-column">
                  <Card.Title className="text-center">{product.name}</Card.Title>
                  <Card.Text className="text-center">
                    <strong>${product.price.toLocaleString()}</strong>{' '}
                    {product.discount && (
                      <span className="text-danger ms-2">
                        {product.discount}
                      </span>
                    )}
                  </Card.Text>
                  <div className="text-center mb-2">
                    <span className="text-warning">
                      {'★'.repeat(product.rating)}
                      {'☆'.repeat(5 - product.rating)}
                    </span>
                    <small className="text-muted"> ({product.reviews} reseñas)</small>
                  </div>
                  <div className="mt-auto">
                    <Button variant="primary" style={{ width: '100%', backgroundColor: '#316c72', borderColor: '#316c72' }}>
                      Comprar
                    </Button>
                  </div>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </div>
  );
}

export default JabonesPage;
