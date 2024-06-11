import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
  const [hello, setHello] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/hello/')
      .then(response => {
        setHello(response.data.hello);
      })
      .catch(error => {
        console.log('There was an error: ', error);
      });
  }, []);

  return (
    <div>
      {/* <h1>Hello, World!</h1> */}
      <p>Message: {hello}</p>
    </div>
  );
}
// const hello = hello

export default HelloWorld;