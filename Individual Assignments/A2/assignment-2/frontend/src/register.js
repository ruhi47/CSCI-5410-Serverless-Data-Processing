import {Button, Form} from "react-bootstrap";
import axios from "axios";

export default function Register() {
    function onClick(e) {
        e.preventDefault()
        const name = document.getElementById("formBasicName").value
        const email = document.getElementById("formBasicEmail").value
        const password = document.getElementById("formBasicPassword").value
        const location = document.getElementById("formBasicLocation").value
        axios.post("https://registration-fikbaei5vq-uw.a.run.app/register", {
            name,
            email,
            password,
            location
        }).then(() => {
            console.log("success")
            alert("User registered!")
        }).catch((err) => {
            console.log(err)
            alert(err.response.data.error)
        })
    }

    return (<Form>
        <Form.Group className="mb-3" controlId="formBasicName">
            <Form.Label>Name</Form.Label>
            <Form.Control type="text" placeholder="Name"/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter email"/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password"/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicLocation">
            <Form.Label>Location</Form.Label>
            <Form.Control type="text" placeholder="Location"/>
        </Form.Group>

        <Button variant="primary" type="submit" onClick={
            onClick
        }>
            Submit
        </Button>
    </Form>)
}