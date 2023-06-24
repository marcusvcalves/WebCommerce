import './produtoCard.css';


export const ProdutoCard = ({id, name, description, price}) => {

    return (
        <div className='produtoCard' key={id}>
            <div>
                <h1>{name}</h1>
                <p>{description}</p>
                <p>{price}</p>
            </div>
        </div>
    )

}
