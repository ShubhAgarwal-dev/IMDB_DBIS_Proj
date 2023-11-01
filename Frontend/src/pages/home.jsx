import { useEffect, useState } from "react"
import { Carousel } from "react-bootstrap"
import { getAllAction, getAllMovies, getAllPerson } from "../utils/apis"
import NavBar from "../components/navbar";


function HomePage() {
    const [allMovies, setAllMovies] = useState([]);
    const [allAction, setAllAction] = useState([]);
    const [allPeople, setAllPeople] = useState([]);
    const [adult, setAdult] = useState(false);
    useEffect(() => {
        let mounted = 1;
        if (mounted) {
            console.log(adult);
            getAllMovies(adult).then((res) => {
                let data = res.data.movies;
                data.sort((a, b) => {
                    return a.start_year - b.start_year;
                }).reverse();
                setAllMovies(data);
            });
            getAllAction(adult).then((res) => {
                let data = res.data.movies;
                data.sort((a, b) => {
                    return a.rating - b.rating;
                }).reverse();
                setAllAction(data);
            });
            getAllPerson().then((res) => {
                let data = res.data.persons;
                data.sort((a, b) => {
                    return a.birth_year - b.birth_year;
                }).reverse();
                setAllPeople(data);
            });
        }
        return () => {
            mounted = 0;
        }
    }, [adult]);
    console.log(allMovies);
    return (
        <>
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
                    Recently Released
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <div className="d-flex" style={{
                    justifyContent: "center",
                    alignContent: "center",
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

                <h2 className="mx-3 my-3 text-white">
                    Top Action
                </h2>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <div className="d-flex" style={{
                    justifyContent: "center",
                    alignContent: "center",
                }}>
                    {allAction ?
                        <Carousel className="d-block w-50 bg-dark">
                            {allAction.slice(0, 5).map((ele) => {
                                // console.log(ele)
                                return (
                                    <Carousel.Item>
                                        <div className="d-flex justify-content-center">
                                            <img src="img1.jpg" className="d-block w-50 h-50"></img>
                                            <div>
                                                <p className="text-white mx-2">Title: {ele.original_title}</p>
                                                <p className="text-white mx-2">Release: {ele.start_year}</p>
                                                <p className="text-white mx-2">Rating: {ele.rating}</p>
                                                <p className="text-white mx-2">Genres: {ele.genres}</p>
                                            </div>
                                        </div>
                                    </Carousel.Item>
                                )
                            })}
                        </Carousel> : <></>}
                </div>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>

                <h2 className="mx-3 my-3 text-white">
                    Top People
                </h2>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>

                <div className="d-flex" style={{
                    justifyContent: "center",
                    alignContent: "center",
                }}>
                    {allPeople ?
                        <Carousel className="d-block w-50 bg-dark">
                            {allPeople.slice(0, 5).map((ele) => {
                                console.log(ele)
                                return (
                                    <Carousel.Item>
                                        <div className="d-flex justify-content-center">
                                            <img src="img1.jpg" className="d-block w-50 h-50"></img>
                                            <div>
                                                <p className="text-white mx-2">Name: {ele.name}</p>
                                                <p className="text-white mx-2">Birth Year: {ele.birth_year}</p>
                                                <p className="text-white mx-2">Primary Profession: {ele.primary_profession[0]}</p>
                                                <p className="text-white mx-2">Age: {ele.death_year ? ele.death_year - ele.birth_year : 2023 - ele.birth_year}</p>
                                            </div>
                                        </div>
                                    </Carousel.Item>
                                )
                            })}
                        </Carousel> : <></>}
                </div>
            </div >
        </>
    )
}


export default HomePage