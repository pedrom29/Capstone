import React from 'react';
import { Card, Button, Row, Col } from 'react-bootstrap';
import './ProductList.css'; // Asegúrate de que este archivo CSS esté vinculado

const products = [
  { id: 1, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Nerolí 300grs', price: '$11.900' },
  { id: 2, title: 'ELITE PROFESIONAL', description: 'Jabón en barra Verbena Godric 300grs', price: '$8.990' },
  { id: 3, title: 'CERAVE', description: 'Jabón en barra Verbena Artorias 300grs', price: '$9.500' },
  { id: 4, title: 'CERAVE', description: 'Jabón en barra Verbena Artorias 500grs', price: '$12.000' },
  { id: 5, title: 'CERAVE', description: 'Jabón en barra Verbena Messmer 500grs', price: '$12.500' },
  { id: 6, title: 'ELITE PROFESIONAL', description: 'Jabón en barra Verbena Godric 500grs', price: '$11.000' },
  { id: 7, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Nerolí 500grs', price: '$10.900' },
  { id: 8, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Artorias 600grs', price: '$13.000' },
  { id: 9, title: 'CERAVE', description: 'Jabón en barra Verbena Messmer 500grs', price: '$12.500' },
  { id: 10, title: 'ELITE PROFESIONAL', description: 'Jabón en barra Verbena Godric 500grs', price: '$11.000' },
  { id: 11, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Nerolí 500grs', price: '$10.900' },
  { id: 12, title: 'BE FELOSCOPHY', description: 'Jabón en barra de Verbena Artorias 600grs', price: '$13.000' },
];

function ProductList() {
  return (
    <Row>
      {products.map(product => (
        <Col key={product.id} xs={12} sm={6} md={4} lg={3} xl={2} className="mb-4"> {/* Cambia xl a 2 columnas por tarjeta */}
          <Card className="product-card">
            <Card.Img variant="top" src={`${process.env.PUBLIC_URL}/product.png`} />
            <Card.Body>
              <Card.Title>{product.title}</Card.Title>
              <Card.Text>{product.description}</Card.Text>
              <Card.Text><strong>{product.price}</strong></Card.Text>
              <Button variant="primary">Comprar</Button>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
}

export default ProductList;
