import React, { Component } from 'react';
import './App.css';
import Alerts from './Alerts';
import Header from './Header';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Alerts />>
      </div>
    );
  }
}

export default App;
