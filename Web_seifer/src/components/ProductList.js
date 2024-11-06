import React from 'react';
import { Card, Button, Row, Col, Container } from 'react-bootstrap';
import { FaStar, FaStarHalfAlt, FaRegStar } from 'react-icons/fa';
import './ProductList.css';

const products = [
  { id: 1, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Nerolí 300grs', price: '$11.900', rating: 4.5, onSale: false, imageUrl: '/images/product001.webp' },
  { id: 2, title: 'ELITE PROFESIONAL', description: 'Jabón en barra Verbena Godric 300grs', price: '$8.990', rating: 4, onSale: true, imageUrl: '/images/product002.webp' },
  { id: 3, title: 'CERAVE', description: 'Jabón en barra Verbena Artorias 300grs', price: '$9.500', rating: 3, onSale: false, imageUrl: '/images/product003.webp' },
  { id: 4, title: 'CERAVE', description: 'Jabón en barra Verbena Artorias 500grs', price: '$12.000', rating: 5, onSale: true, imageUrl: '/images/product004.webp' },
  { id: 5, title: 'CERAVE', description: 'Jabón en barra Verbena Messmer 500grs', price: '$12.500', rating: 4.5, onSale: false, imageUrl: '/images/product005.webp' },
  { id: 6, title: 'ELITE PROFESIONAL', description: 'Jabón en barra Verbena Godric 500grs', price: '$11.000', rating: 3.5, onSale: true, imageUrl: '/images/product006.webp' },
  { id: 7, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Nerolí 500grs', price: '$10.900', rating: 5, onSale: false, imageUrl: '/images/product007.webp' },
  { id: 8, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Artorias 600grs', price: '$13.000', rating: 4, onSale: true, imageUrl: '/images/product008.webp' },
  { id: 9, title: 'CERAVE', description: 'Jabón en barra Verbena Messmer 300grs', price: '$12.500', rating: 4.5, onSale: true, imageUrl: '/images/product009.webp' },
  { id: 10, title: 'ELITE PROFESIONAL', description: 'Jabón en barra Verbena Godric 200grs', price: '$7.000', rating: 3, onSale: false, imageUrl: '/images/product010.webp' },
  // Añadir más productos según sea necesario
];

// Función para renderizar estrellas según la calificación
function renderStars(rating) {
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 !== 0;

  return (
    <>
      {[...Array(fullStars)].map((_, i) => <FaStar key={`full-${i}`} style={{ color: '#FFD700' }} />)}
      {hasHalfStar && <FaStarHalfAlt style={{ color: '#FFD700' }} />}
      {[...Array(5 - fullStars - (hasHalfStar ? 1 : 0))].map((_, i) => <FaRegStar key={`empty-${i}`} style={{ color: '#FFD700' }} />)}
    </>
  );
}

function ProductList() {
  return (
    <Container fluid="md" className="my-4">
      <Row className="g-4">
        {products.map(product => (
          <Col key={product.id} xs={12} sm={6} md={4} lg={3} className="d-flex">
            <Card className="w-100 h-100 product-card shadow-sm">
              <Card.Img variant="top" src={process.env.PUBLIC_URL + product.imageUrl} alt={product.title} />
              <Card.Body className="d-flex flex-column">
                <Card.Title className="text-center" style={{ fontSize: '1rem', fontWeight: 'bold', whiteSpace: 'normal' }}>
                  {product.title}
                </Card.Title>
                <Card.Text className="text-center text-muted" style={{ fontSize: '0.9rem', whiteSpace: 'normal' }}>
                  {product.description}
                </Card.Text>
                <Card.Text className="text-center" style={{ fontSize: '1.1rem', fontWeight: 'bold', color: '#316c72' }}>
                  {product.price}
                </Card.Text>

                {/* Estrellas de puntuación */}
                <div className="text-center mb-2">
                  {renderStars(product.rating)}
                </div>

                {/* Indicador de oferta */}
                {product.onSale && (
                  <div className="text-center">
                    <span className="badge bg-danger">Oferta</span>
                  </div>
                )}

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
  );
}

export default ProductList;
