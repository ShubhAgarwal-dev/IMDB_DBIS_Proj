import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';

function BasicCard(props) {
    return (
        <Card style={{ width: '100%', padding: '5px', borderColor: "white" }} className='bg-dark text-white'>
            <Card.Img variant="top" src={props.movie.image_link} />
            <Card.Body>
                <Card.Title>
                    <h1 class="display-6">{props.movie.original_title}</h1>
                </Card.Title>
                <Card.Text>
                    <p class="lead">
                        {props.movie.start_year}
                    </p>
                    <p class="lead">
                        {props.movie.genres}
                    </p>
                </Card.Text>
                <Link to={"/view/" + props.movie.t_const} style={{ textDecoration: "none", color: "white" }}>
                    <Button variant="primary">Know More</Button>
                </Link>
            </Card.Body>
        </Card >
    );
}

export default BasicCard;