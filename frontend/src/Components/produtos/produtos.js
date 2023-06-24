import { Component } from 'react';
import './produtos.css';
import { ProdutoCard } from '../produtoCard/produtoCard';

class Produto extends Component {
state = {
  produtos: []
};

componentDidMount() {
  this.loadProducts();
}
loadProducts = async () => {
  const productsResponse =  fetch('http://127.0.0.1:8000/api/mostrar-produtos/');

  const [products] = await Promise.all([productsResponse]);

  const productsJson = await products.json();

  this.setState({ produtos: productsJson });
}


render() {
  const { produtos } = this.state;
  const serverUrl = 'http://localhost:8000';

  return (
    <div className='container'>
      {produtos.map(produto => (
        <ProdutoCard
        key = {produto.id}
        id = {produto.id}
        name = {produto.name}
        image={produto.image ? serverUrl + produto.image : null}
        description = {produto.description}
        price = {produto.price}
        />
      ))}
    </div>
  );
}
}

export default Produto;