import React from 'react';
import { Carousel } from 'react-bootstrap';
import './Banner.css';

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
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100 carousel-image"
            src={`${process.env.PUBLIC_URL}/imagen2.png`}
            alt="Second slide"
          />
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100 carousel-image"
            src={`${process.env.PUBLIC_URL}/imagen3.png`}
            alt="Third slide"
          />
        </Carousel.Item>
      </Carousel>
    </div>
  );
}

export default Banner;
