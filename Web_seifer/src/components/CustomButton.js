import React from 'react';
import { Button } from 'react-bootstrap';

function CustomButton({ children, ...props }) {
  return (
    <Button
      {...props}
      style={{
        backgroundColor: '#316c72',
        borderColor: '#316c72',
        color: '#ffffff',
      }}
      className="mx-1"
    >
      {children}
    </Button>
  );
}

export default CustomButton;
