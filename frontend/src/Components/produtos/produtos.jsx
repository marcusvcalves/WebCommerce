import './produtos.css';
import { ProdutoCard } from '../produtoCard/produtoCard';
import React, { useEffect, useState } from 'react';
import { loadProducts } from '../../utils/loadProducts/loadProducts'

const Produto = () => {
  const [produtos, setProdutos] = useState([]);
  const serverUrl = 'http://localhost:8000';

  useEffect(() => {
    async function fetchData() {
      const productsJson = await loadProducts();
      setProdutos(productsJson);
    }
    fetchData();
  }, []);


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

