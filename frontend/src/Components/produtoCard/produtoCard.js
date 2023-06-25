import './produtoCard.css';
import Button from '@mui/material/Button';

export const ProdutoCard = ({id, name, image, description, price}) => {
    return (
            <div className='produtoCard' key={id}>
                <div className='produto'>
                    <img src={image} alt="produto" width='100%' height='200vh'></img>
                    <h2 className='produto-text'>{name}</h2>
                    <p className='produto-text produto-price'>R$ {price}</p>
                    <div className='produto-footer'>
                        <Button className='comprar-button' variant="contained">Comprar</Button>
                    </div>
                </div>
            </div>
    )

}
