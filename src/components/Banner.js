import React from 'react';
import { Carousel } from 'react-bootstrap';
import './Banner.css'; // Archivo CSS para ajustar el margen

function Banner() {
  return (
    <div className="banner-container"> {/* Usamos una clase para controlar el margen */}
      <Carousel>
        <Carousel.Item>
          <img
            className="d-block w-100 carousel-image"
            src={`${process.env.PUBLIC_URL}/imagen1.png`}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>Primera Imagen</h3>
            <p>Cuidamos el medio ambiente.</p>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100 carousel-image"
            src={`${process.env.PUBLIC_URL}/imagen2.png`}
            alt="Second slide"
          />
          <Carousel.Caption>
            <h3>Segunda Imagen</h3>
            <p>Productos eco-amigables.</p>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100 carousel-image"
            src={`${process.env.PUBLIC_URL}/imagen3.png`}
            alt="Third slide"
          />
          <Carousel.Caption>
            <h3>Tercera Imagen</h3>
            <p>La mejor calidad en productos.</p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </div>
  );
}

export default Banner;
