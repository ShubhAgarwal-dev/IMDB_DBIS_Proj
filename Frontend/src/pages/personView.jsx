import { useEffect, useState } from "react"
import { Carousel } from "react-bootstrap"
import { getAllAction, getAllMovies, getAllPerson, getPersonAllMovies, getPersonDetails } from "../utils/apis"
import NavBar from "../components/navbar";
import { useParams } from "react-router-dom";


function PersonView() {
    const { id } = useParams();
    const [allMovies, setAllMovies] = useState([]);
    const [personDetails, setPersonDetails] = useState({});
    const [adult, setAdult] = useState(false);
    useEffect(() => {
        let mounted = 1;
        if (mounted) {
            console.log(adult);
            getPersonDetails(id).then((res) => {
                setPersonDetails(res.data.persons[0]);
            });
            getPersonAllMovies(id, adult).then((res) => {
                setAllMovies(res.data.movies);
            });
        }
        return () => {
            mounted = 0;
        }
    }, [adult]);
    console.log(allMovies);
    return (
        <div style={{ minHeight: "100vh" }} className="bg-dark">
            <NavBar />
            <div className="bg-dark pt-3">
                <div className="form-check form-switch d-flex" style={{ justifyContent: "center" }}>
                    <input className="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" onClick={(e) => {
                        setAdult((adult) => {
                            return !adult;
                        })
                    }} />
                    <label className="form-check-label text-white" for="flexSwitchCheckDefault">Adult</label>
                </div>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <h1 className="mx-3 my-3 text-white">
                    {personDetails ? personDetails.name : <></>}
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <h1 className="mx-3 my-3 text-white">
                    <h1 className="display-5">Details:</h1>
                    <p className="lead">Born: {personDetails.birth_year}</p>
                    <p className="lead">Death: {personDetails.death_year}</p>
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <div className="d-flex" style={{
                    justifyContent: "center",
                    alignContent: "center",
                    minHeight: "5vh"
                }}>
                    {allMovies ?
                        <Carousel className="d-block w-50 bg-dark">
                            {allMovies.slice(0, 5).map((ele) => {
                                // console.log(ele)
                                return (
                                    <Carousel.Item>
                                        <div className="d-flex justify-content-center">
                                            <img src="img1.jpg" className="d-block w-50 h-50"></img>
                                            <div>
                                                <p className="text-white mx-2">Title: {ele.original_title}</p>
                                                <p className="text-white mx-2">Release: {ele.start_year}</p>
                                            </div>
                                        </div>
                                    </Carousel.Item>
                                )
                            })}
                        </Carousel> : <></>}
                </div>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
            </div>
        </div>
    )
}


export default PersonView