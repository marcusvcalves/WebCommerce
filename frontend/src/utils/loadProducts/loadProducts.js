export const loadProducts = async () => {
    const productsResponse = await fetch('http://127.0.0.1:8000/api/mostrar-produtos/');
    const productsJson = await productsResponse.json();
    return productsJson;
  }
