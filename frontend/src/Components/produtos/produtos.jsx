import './produtos.css';
import { ProdutoCard } from '../produtoCard/produtoCard';
import React, { useEffect, useState } from 'react';

const Produto = () => {
  const [produtos, setProdutos] = useState([]);
  const serverUrl = 'http://localhost:8000';

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    const productsResponse = await fetch('http://127.0.0.1:8000/api/mostrar-produtos/');
    const productsJson = await productsResponse.json();
    setProdutos(productsJson);
  }

  return (
    <div className='container'>
      {produtos.map(produto => (
        <ProdutoCard
          key={produto.id}
          id={produto.id}
          name={produto.name}
          image={produto.image ? serverUrl + produto.image : null}
          description={produto.description}
          price={produto.price}
        />
      ))}
    </div>
  );
}

export default Produto;

