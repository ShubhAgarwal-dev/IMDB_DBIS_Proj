import { Button, Form } from "react-bootstrap"
import NavBar from "../components/navbar"

function People() {
    return (
        <>
            <NavBar />
            <div className="bg-dark min-vh-100 pt-3">
                <h1 className="mx-3 my-3 text-white">
                    All People
                </h1>
                <hr style={{ border: "solid 3px white", margin: 10 }}></hr>
                <h3 className="mx-3 my-3 text-white">
                    Filters
                </h3>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 190 }}>
                        Name:
                    </h5>
                    <Form.Control type="text" placeholder="Search By Name" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 190 }}>
                        Born Year:
                    </h5>
                    <Form.Control type="number" placeholder="Search By Born Year" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 190 }}>
                        Age:
                    </h5>
                    <Form.Control type="text" placeholder="Search By Age" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="d-flex justify-content-center">
                    <h5 className="mx-3 my-3 text-white" style={{ width: 190 }}>
                        Movies:
                    </h5>
                    <Form.Control type="text" placeholder="Search By Movies" className="w-50 mx-3 my-1"></Form.Control>
                </div>
                <div className="my-3 d-flex justify-content-center">
                    <Button>Go</Button>
                </div>
                <h3 className="mx-3 my-3 text-white">
                    People
                </h3>
            </div >
        </>
    )
}


export default People