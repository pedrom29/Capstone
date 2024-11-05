import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import CustomNavbar from './Navbar'; // Importa el navbar

const blogPosts = [
  {
    id: 1,
    title: "Compras éticas",
    description: "Del origen a tu piel y más allá: Nuestra postura frente a las compras éticas. Nos enorgullecemos de nuestra creatividad, y esto no acaba con nuestros productos.",
    imageUrl: `${process.env.PUBLIC_URL}/blog01.png`, // Cambia con la URL de imagen correcta
  },
  {
    id: 2,
    title: "Productos hechos a mano",
    description: "Crear productos con nuestras manos ha sido parte de quienes somos desde nuestros humildes comienzos. Está presente en casi todos los aspectos de nuestro negocio.",
    imageUrl: `${process.env.PUBLIC_URL}/blog01.png`, // Cambia con la URL de imagen correcta
  },
  {
    id: 3,
    title: "100% Vegetariano",
    description: "Todos nuestros productos son 100% vegetarianos y el 95% de ellos son completamente veganos. Ser vegetariano es algo en lo que siempre hemos sido apasionados.",
    imageUrl: `${process.env.PUBLIC_URL}/blog01.png`, // Cambia con la URL de imagen correcta
  },
  {
    id: 4,
    title: "Impacto Social",
    description: "Nos dedicamos a tener un impacto positivo en nuestras comunidades. Trabajamos junto a socios que comparten nuestra visión de un mundo más justo.",
    imageUrl: `${process.env.PUBLIC_URL}/blog01.png`, // Cambia con la URL de imagen correcta
  },
  {
    id: 5,
    title: "Ingredientes Naturales",
    description: "Creemos en el poder de los ingredientes naturales. Elegimos los mejores ingredientes de origen ético y natural para todos nuestros productos.",
    imageUrl: `${process.env.PUBLIC_URL}/blog01.png`, // Cambia con la URL de imagen correcta
  },
  {
    id: 6,
    title: "Innovación Sostenible",
    description: "Estamos comprometidos con la sostenibilidad y la innovación en nuestros procesos para reducir el impacto ambiental de nuestros productos.",
    imageUrl: `${process.env.PUBLIC_URL}/blog01.png`, // Cambia con la URL de imagen correcta
  },
];

function BlogPage() {
  return (
    <div style={{ backgroundColor: '#f8f9fa', minHeight: '100vh' }}>
      <CustomNavbar /> {/* Navbar en la parte superior */}
      <Container className="mt-4">
        <Row>
          {blogPosts.map((post) => (
            <Col key={post.id} xs={12} md={6} lg={4} className="mb-4">
              <Card className="h-100">
                <Card.Img variant="top" src={post.imageUrl} alt={post.title} />
                <Card.Body>
                  <Card.Title>{post.title}</Card.Title>
                  <Card.Text>{post.description}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </div>
  );
}

export default BlogPage;
