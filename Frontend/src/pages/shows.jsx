import { Button, Col, Container, Form } from "react-bootstrap"
import NavBar from "../components/navbar"
import { useEffect, useState } from "react"
import { getAllShows, getMovieByGenre, getMovieByPerson, getMovieByRating, getShowsByEndYear, getShowsByRelYear, getShowsByTitle } from "../utils/apis";
import Row from 'react-bootstrap/Row';
import BasicCard from "../components/cards";

function Shows() {

    const [adult, setAdult] = useState(false);
    const [allShows, setAllShows] = useState([]);
    useEffect(() => {
        let mounted = true;
        if (mounted) {
            getAllShows(adult).then((res) => {
                setAllShows(res.data.movies)
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
            end: data.endYear.value,
            cast: data.cast.value,
            genres: data.genre.value,
            rating: data.rating.value
        };
        document.getElementById("filter-form").reset();
        if (clicked === "title" && vals.title != "") {
            getShowsByTitle(vals.title, adult).then((res) => {
                setAllShows(res.data.movies);
            })
        }
        if (clicked === "rel" && vals.rel != "") {
            getShowsByRelYear(vals.rel, adult).then((res) => {
                setAllShows(res.data.movies);
            })
        }
        if (clicked === "end" && vals.end != "") {
            getShowsByEndYear(vals.end, adult).then((res) => {
                setAllShows(res.data.movies);
            })
        }
        if (clicked === "cast" && vals.cast != "") {
            getMovieByPerson(vals.cast, adult).then((res) => {
                setAllShows(res.data.movies);
            })
        }
        if (clicked === "genres" && vals.genres != "") {
            getMovieByGenre(vals.genres, adult).then((res) => {
                setAllShows(res.data.movies);
            })
        }
        if (clicked === "rating" && vals.rating != "") {
            getMovieByRating(vals.rating, adult).then((res) => {
                setAllShows(res.data.movies);
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
                    All Shows
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <div className="d-flex">
                    <div style={{ maxWidth: "500px" }}>
                        <Form onSubmit={submitHandler} id="filter-form">
                            <h3 className="mx-3 my-3 text-white">
                                Filters
                            </h3>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }} >
                                    Title:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Title" className="w-50 mx-3 my-1" name="title"></Form.Control>
                                <Button variant="primary" type="submit" className="m-2" onClick={() => setClicked("title")}>
                                    Go
                                </Button>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Release Year:
                                </h5>
                                <Form.Control type="number" placeholder="Search By Release Year" className="w-50 mx-3 my-1" name="relYear"></Form.Control>
                                <Button variant="primary" type="submit" className="m-2" onClick={() => setClicked("rel")}>
                                    Go
                                </Button>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    End Year:
                                </h5>
                                <Form.Control type="number" placeholder="Search By End Year" className="w-50 mx-3 my-1" name="endYear"></Form.Control>
                                <Button variant="primary" type="submit" className="m-2" onClick={() => setClicked("end")}>
                                    Go
                                </Button>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Cast:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Cast" className="w-50 mx-3 my-1" name="cast"></Form.Control>
                                <Button variant="primary" type="submit" className="m-2" onClick={() => setClicked("cast")}>
                                    Go
                                </Button>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Genre:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Genre" className="w-50 mx-3 my-1" name="genre"></Form.Control>
                                <Button variant="primary" type="submit" className="m-2" onClick={() => setClicked("genres")}>
                                    Go
                                </Button>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Rating:
                                </h5>
                                <Form.Control type="number" placeholder="Search By Rating" className="w-50 mx-3 my-1" name="rating" step=".1"></Form.Control>
                                <Button variant="primary" type="submit" className="m-2" onClick={() => setClicked("rating")}>
                                    Go
                                </Button>
                            </div>
                        </Form>
                    </div>
                    <div style={{
                        maxWidth: "950px"
                    }}>
                        <h3 className="mx-3 my-3 text-white">
                            Shows
                        </h3>
                        {allShows ?
                            <Container>
                                <Row lg={allShows.length > 3 ? 3 : allShows.length} >
                                    {
                                        allShows.map((movie) => {
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


export default Shows