import React from 'react';
import './App.css';
import StockData from './StockData';

function App() {
  const sampleData = {
    ticker: 'AAPL',
    date: '2020-01-01 to 2021-01-01',
    description: 'Sample fetched data'
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hello, React!</h1>
        <StockData data={sampleData} />
      </header>
    </div>
  );
}

export default App;
