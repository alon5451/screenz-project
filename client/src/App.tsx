import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

const App = () => {
  const [serverMes, setServerMes] = useState({'message':''})

  useEffect(() => {
    fetch('/api').then(res => res.json()).then(data => {
      console.log(data)
      setServerMes(data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        UP! - {serverMes.message}
      </header>
    </div>
  );
}

export default App;
