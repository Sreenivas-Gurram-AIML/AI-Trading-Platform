import React from 'react';

function StockData({ data }) {
  return (
    <div>
      <h1>Stock Data</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default StockData;
