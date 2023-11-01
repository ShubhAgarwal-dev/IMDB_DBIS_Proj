import { Button, Form } from "react-bootstrap"
import NavBar from "../components/navbar"

function Series() {
    return (
        <>
            <NavBar />
            <div className="bg-dark min-vh-100 pt-3">
                <h1 className="mx-3 my-3 text-white">
                    All Series
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <h3 className="mx-3 my-3 text-white">
                    Filters
                </h3>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                        Title:
                    </h5>
                    <Form.Control type="text" placeholder="Search By Title" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                        Release Year:
                    </h5>
                    <Form.Control type="number" placeholder="Search By Release Year" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                        End Year:
                    </h5>
                    <Form.Control type="number" placeholder="Search By Release Year" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                        Cast:
                    </h5>
                    <Form.Control type="text" placeholder="Search By Cast" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                        Genre:
                    </h5>
                    <Form.Control type="text" placeholder="Search By Genre" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 150 }}>
                        Rating:
                    </h5>
                    <Form.Control type="number" placeholder="Search By Rating" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="my-3 d-flex justify-content-center">
                    <Button>Go</Button>
                </div>
                <h3 className="mx-3 my-3 text-white">
                    Series
                </h3>
            </div >
        </>
    )
}


export default Series