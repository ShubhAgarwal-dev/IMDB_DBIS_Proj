import { Button, Col, Container, Form } from "react-bootstrap"
import NavBar from "../components/navbar"
import { useEffect, useState } from "react"
import { getAllMovies, getMovieByGenre, getMovieByPerson, getMovieByRating, getMovieByRelYear, getMovieByTitle } from "../utils/apis";
import Row from 'react-bootstrap/Row';
import BasicCard from "../components/cards";

function BasicView(props) {
    const { sel, name } = props;
    const [adult, setAdult] = useState(false);
    const [allMovies, setAllMovies] = useState([]);
    useEffect(() => {
        let mounted = true;
        if (mounted) {
            getAllMovies(adult).then((res) => {
                setAllMovies(res.data.movies)
            })
        }
        return () => {
            mounted = false;
        }
    }, [adult])

    const [clicked, setClicked] = useState(null);


    const submitHandler = (e) => {
        e.preventDefault();
        const data = e.target;
        const vals = {
            title: data.title.value,
            rel: data.relYear.value,
            cast: data.cast.value,
            genres: data.genre.value,
            rating: data.rating.value
        };
        document.getElementById("filter-form").reset();
        if (clicked === "title" && vals.title != "") {
            getMovieByTitle(vals.title, adult).then((res) => {
                setAllMovies(res.data.movies);
            })
        }
        if (clicked === "rel" && vals.rel != "") {
            getMovieByRelYear(vals.rel, adult).then((res) => {
                setAllMovies(res.data.movies);
            })
        }
        if (clicked === "cast" && vals.cast != "") {
            getMovieByPerson(vals.cast, adult).then((res) => {
                setAllMovies(res.data.movies);
            })
        }
        if (clicked === "genres" && vals.genres != "") {
            getMovieByGenre(vals.genres, adult).then((res) => {
                setAllMovies(res.data.movies);
            })
        }
        if (clicked === "rating" && vals.rating != "") {
            getMovieByRating(vals.rating, adult).then((res) => {
                setAllMovies(res.data.movies);
            })
        }
    }

    return (
        <>
            <NavBar />
            <div className="bg-dark min-vh-100 p-3">
                <div className="form-check form-switch d-flex" style={{ justifyContent: "center" }}>
                    <input className="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" onClick={(e) => {
                        setAdult((adult) => {
                            return !adult;
                        })
                    }} style={{ marginRight: "5px" }} /><span className="iconify form-check-label text-white" data-icon="uil:18-plus" style={{ fontSize: "larger" }} />
                </div>
                <hr style={{ border: "solid 3px white", margin: 10 }} />
                <h1 className="mx-3 my-3 text-white">
                    All Movies
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <div className="d-flex">
                    <div style={{ maxWidth: "500px" }}>
                    </div>
                    <div style={{
                        maxWidth: "950px"
                    }}>
                        <h3 className="mx-3 my-3 text-white">
                            Movies
                        </h3>
                        {allMovies ?
                            <Container>
                                <Row lg={allMovies.length > 3 ? 3 : allMovies.length} >
                                    {
                                        allMovies.map((movie) => {
                                            return (
                                                <Col className="text-white mt-3">
                                                    <BasicCard movie={movie} />
                                                </Col>
                                            )
                                        })
                                    }
                                </Row>
                            </Container>
                            : <></>}
                    </div>
                </div>
            </div >
        </>
    )
}


export default BasicView