import './produtoCard.css';


export const ProdutoCard = ({id, name, image, description, price}) => {
    return (
            <div className='produtoCard' key={id}>
                <div className='produto'>
                    <img src={image} width='100px' height='100px'></img>
                    <h1>{name}</h1>
                    <p>{description}</p>
                    <p>{price}</p>
                </div>
            </div>
    )

}
