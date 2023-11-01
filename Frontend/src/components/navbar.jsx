import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { useState } from 'react';
import { Link, Navigate } from 'react-router-dom';
import BasicView from '../pages/basicView';

function NavBar() {
    return (
        <Navbar expand="lg" bg="light">
            < Container fluid >
                <Navbar.Brand >
                    <Link to={`/`} className='text-dark' style={{ textDecoration: "none" }}>
                        IMDB Clone
                    </Link>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarScroll" />
                <Navbar.Collapse id="navbarScroll">
                    <Nav
                        className="ms-3 my-2 my-lg-0"
                        style={{ maxHeight: '100px' }}
                        navbarScroll
                    >
                        <NavDropdown title="Menu" id="navbarScrollingDropdown">
                            <NavDropdown.Item>
                                <Link to={`/movies`} className='text-dark' style={{ textDecoration: "none" }}>
                                    List All Movies
                                </Link>
                            </NavDropdown.Item>
                            <NavDropdown.Item>
                                <Link to={`/shows`} className='text-dark' style={{ textDecoration: "none" }}>
                                    List All TV Shows
                                </Link>
                            </NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                    <Nav.Link
                        className="ms-3 my-2 my-lg-0"
                        style={{ maxHeight: '100px' }}
                        navbarScroll
                    >
                        <Link to={`/advanced`} className='text-dark' style={{ textDecoration: "none" }}>
                            Advanced Search
                        </Link>
                    </Nav.Link>
                </Navbar.Collapse>
            </Container >
        </Navbar >
    );
}

export default NavBar;