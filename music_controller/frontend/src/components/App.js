import React from 'react';
import ReactDOM from 'react-dom';

function App() {
  return (
    <h1>Test</h1>
    // <div className="center">
    //   <HomePage />
    // </div>
  );
}

const appDiv = document.getElementById("app");
ReactDOM.render(<App />, appDiv);