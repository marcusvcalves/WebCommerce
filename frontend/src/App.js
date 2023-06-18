import './App.css';
import { Component } from 'react';


class App extends Component {
state = {
  produtos: []
};

componentDidMount() {
  fetch('http://127.0.0.1:8000/api/mostrar-produtos/')
    .then(response => response.json())
    .then(produtos => this.setState({ produtos }))
    .catch(err => console.log(err));
}



render() {
  const { produtos } = this.state;

  return (
  <div className="App">
    {produtos.map(produtos => (
      <div key={produtos.id}>
        <h1>{produtos.name}</h1>
        <p>{produtos.description}</p>
        <p>{produtos.price}</p>
      </div>)
    )}
  </div>
    );
  } 
}

export default App;
