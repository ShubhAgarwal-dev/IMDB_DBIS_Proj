import { Button, Col, Container, Form } from "react-bootstrap"
import NavBar from "../components/navbar"
import { useEffect, useState } from "react"
import { getAdvancedSearch, getAllMovies, getMovieByGenre, getMovieByPerson, getMovieByRating, getMovieByRelYear, getMovieByTitle } from "../utils/apis";
import Row from 'react-bootstrap/Row';
import BasicCard from "../components/cards";

function AdvancedSearch() {
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



    const submitHandler = (e) => {
        e.preventDefault();
        const data = e.target;
        console.log(data);
        const vals = {
            title: data.title.value,
            start_year: data.relYear.value,
            end_year: data.endYear.value,
            actor_name: data.actor.value,
            director_name: data.director.value,
            writer_name: data.writer.value,
            person_name: data.person.value,
            rating: data.imdbr.value,
            urating: data.urate.value,
            language: data.lang.value,
            is_original_title: true,
        };
        getAdvancedSearch(vals, adult).then((res) => {
            setAllMovies(res.data.movies);
        });
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
                    Advanced Search
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <div className="d-flex">
                    <div style={{ maxWidth: "500px" }}>
                        <Form onSubmit={submitHandler} id="filter-form">
                            <h3 className="mx-3 my-3 text-white">
                                Filters
                            </h3>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Title:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Title" className="w-50 mx-3 my-1" name="title" defaultValue={""}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Release Year:
                                </h5>
                                <Form.Control type="number" placeholder="Search By Release Year" className="w-50 mx-3 my-1" name="relYear" defaultValue={0}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    End Year:
                                </h5>
                                <Form.Control type="number" placeholder="Search By Release Year" className="w-50 mx-3 my-1" name="endYear" defaultValue={0}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Actor Name:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Cast" className="w-50 mx-3 my-1" name="actor" defaultValue={""}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Director Name:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Cast" className="w-50 mx-3 my-1" name="director" defaultValue={""}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Writer Name:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Cast" className="w-50 mx-3 my-1" name="writer" defaultValue={""}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Person Name:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Cast" className="w-50 mx-3 my-1" name="person" defaultValue={""}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    Language:
                                </h5>
                                <Form.Control type="text" placeholder="Search By Language" className="w-50 mx-3 my-1" name="lang" defaultValue={""}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    IMDB Rating:
                                </h5>
                                <Form.Control type="number" placeholder="Search By Rating" className="w-50 mx-3 my-1" name="imdbr" step=".1" defaultValue={1}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center">
                                <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                                    User Rating:
                                </h5>
                                <Form.Control type="number" placeholder="Search By User Rating" className="w-50 mx-3 my-1" name="urate" step=".1" defaultValue={1}></Form.Control>
                            </div>
                            <div className="d-flex justify-content-center mt-3">
                                <Button type="submit">Submit</Button>
                            </div>
                        </Form>
                    </div>
                    <div style={{
                        maxWidth: "950px"
                    }}>
                        <h3 className="mx-3 my-3 text-white">
                            Items
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


export default AdvancedSearch