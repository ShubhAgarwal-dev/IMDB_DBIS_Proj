import { useEffect, useState, useSyncExternalStore } from "react";
import { useParams } from "react-router-dom";
import { getMovieActors, getMovieData, getMovieDirector, getMovieOtherTitles, sendReview } from "../utils/apis";
import { Row, Col, Container, Form, Modal } from "react-bootstrap";
import { Link } from "react-router-dom";
import NavBar from "../components/navbar";
import Button from 'react-bootstrap/Button';
import { BACKEND_URL } from "../constant/variables";

export default function View() {
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const { id } = useParams();
    const [movieActors, setMovieActors] = useState(null);
    const [movieDirectors, setMovieDirectors] = useState(null);
    const [movieData, setMovieData] = useState(null);
    const [otherTitles, setOtherTitles] = useState(null);
    useEffect(() => {
        let mounted = true;
        if (mounted) {
            try {
                getMovieActors(id).then((res) => {
                    setMovieActors(res.data.persons);
                })
                getMovieData(id).then((res) => {
                    setMovieData(res.data.movies);
                })
                getMovieDirector(id).then((res) => {
                    setMovieDirectors(res.data.persons);
                })
                getMovieOtherTitles(id).then((res) => {
                    setOtherTitles(res.data.movies);
                })
                console.log({
                    movieData: movieData,
                });
            } catch (err) {
                let mute = err;
            }
        }
        return (() => { mounted = false })
    }, [id])

    const submitHandler = (e) => {
        e.preventDefault();
        e=e.target;
        const url = `${BACKEND_URL}user/rate?tconst=${id}&rating=${e.rating.value}&review=${e.review.value}`
        const uname = e.username.value;
        const password = e.password.value;
        sendReview({
            "username": uname,
            "password": password
        }, url).then((res) => handleClose());
    }

    function GiveRating() {
        return (
            <>
                <Modal show={show} onHide={handleClose}>
                    <Modal.Header closeButton className="bg-dark text-white">
                        <Modal.Title>Give Rating</Modal.Title>
                    </Modal.Header>
                    <Modal.Body className="bg-dark text-white"><h1>Rate</h1>
                        <Form onSubmit={submitHandler}>
                            <h5 className="mx-3 my-3 text-white" >
                                UserName:
                            </h5>
                            <Form.Control type="text" placeholder="Enter username" className="w-50 mx-3 my-1" name="username"></Form.Control>
                            <h5 className="mx-3 my-3 text-white"  >
                                Password:
                            </h5>
                            <Form.Control type="password" placeholder="Enter password" className="w-50 mx-3 my-1" name="password"></Form.Control>
                            <h5 className="mx-3 my-3 text-white" >
                                Rating:
                            </h5>
                            <Form.Control type="number" placeholder="Enter Rating" className="w-50 mx-3 my-1" name="rating" step={0.1}></Form.Control>
                            <h5 className="mx-3 my-3 text-white" >
                                Review:
                            </h5>
                            <Form.Control type="text" placeholder="Enter Review" className="w-50 mx-3 my-1" name="review"></Form.Control>
                                <Button variant="primary" type="submit" className="mt-3">
                                    Save Changes
                                </Button>
                        </Form>
                    </Modal.Body>
                    <Modal.Footer className="bg-dark color-white">
                        <Button variant="secondary" onClick={handleClose}>
                            Close
                        </Button>
                    </Modal.Footer>
                </Modal>
            </>
        );
    }

    return (
        <div className="bg-dark text-white" style={{ minHeight: "100vh" }}>
            <GiveRating />
            <NavBar />
            <Container className="pt-3">
                <Row>
                    <Col>
                        {movieData ? <img src={movieData[0].image_link} width="100%" style={{ maxHeight: "fit-content" }} /> : <></>}
                    </Col>
                    <Col>
                        {movieData ? <>
                            <h1>{movieData[0].original_title}</h1>
                            <p className="lead">User Rating: {movieData[0].urating}</p>
                            <p className="lead">IMDB Rating: {movieData[0].rating}</p>
                            {otherTitles ?
                                otherTitles.map((ele) => {
                                    if (ele.is_original_title === true) {
                                        return (
                                            <div>
                                                <p className="lead">Language: {ele.language}</p>
                                                <p className="lead">Region: {ele.region}</p>
                                                <p className="lead">Type: {ele.types}</p>
                                            </div>
                                        )
                                    }
                                })
                                : <></>}
                            <hr style={{ border: "solid 3px white" }} />
                        </> : <></>}
                        {otherTitles ? <>
                            <h3>Also Know As</h3>
                            {
                                otherTitles.map((ele) => {
                                    if (ele.is_original_title === false) {
                                        return (
                                            <div>
                                                <h1 className="display-4">{ele.local_title}</h1>
                                                <p className="lead">Language: {ele.language}</p>
                                                <p className="lead">Region: {ele.region}</p>
                                                <p className="lead">Type: {ele.types}</p>
                                            </div>
                                        )
                                    }
                                })
                            }
                            <hr style={{ border: "solid 3px white" }} />
                        </> : <></>}
                        {movieDirectors ? <>
                            <h2>People</h2>
                            <h3 className="display-5">Directors</h3>
                            {
                                movieDirectors.map((ele) => {
                                    return (
                                        <div style={{ marginLeft: "10px" }}>
                                            <Link to={"/person/" + ele.nconst} style={{ textDecoration: "none", color: "white" }}>
                                                <h1 className="display-6">{ele.name}</h1>
                                            </Link>
                                            <p className="lead">Born: {ele.birth_year}</p>
                                            <p className="lead">Death: {ele.death_year ? ele.death_year : '-'}</p>
                                        </div>
                                    )
                                })
                            }</> : <><h2>Director</h2><h3 className="display-5">No Data Present</h3></>}
                        {movieActors ? <>
                            <h3 className="display-5">Movie Actors</h3>
                            {
                                movieActors.map((ele) => {
                                    return (
                                        <div style={{ marginLeft: "10px" }}>
                                            <Link to={"/person/" + ele.nconst} style={{ textDecoration: "none", color: "white" }}>
                                                <h1 className="display-6">{ele.name}</h1>
                                            </Link>
                                            <p className="lead">Born: {ele.birth_year}</p>
                                            <p className="lead">Death: {ele.death_year ? ele.death_year : '-'}</p>
                                        </div>
                                    )
                                })
                            }
                        </> : <><h2>Actor</h2><h3 className="display-5">No Data Present</h3></>}
                    </Col>
                    <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                </Row>
            </Container>
            <Button style={{ position: "sticky", bottom: "10px", left: "10px" }} onClick={(e) => setShow(true)}> Rating</Button>
        </div >
    );
}