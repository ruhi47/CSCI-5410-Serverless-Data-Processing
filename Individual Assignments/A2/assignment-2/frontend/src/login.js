import {Button, Form} from "react-bootstrap";
import axios from "axios";

export default function Login() {
    function onClick(e) {
        e.preventDefault()
        const email = document.getElementById("formBasicEmail").value
        const password = document.getElementById("formBasicPassword").value
        axios.post("https://login-fikbaei5vq-uw.a.run.app/login", {email, password}).then((res) => {
            localStorage.setItem("user", res.data.current_user)
            alert("Login successful!")
        }).catch((err) => {
            console.log(err)
            alert(err.response.data.error)
        })
    }

    return (<Form>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control type="email" placeholder="Enter email"/>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" placeholder="Password"/>
            </Form.Group>
            <Button variant="primary" type="submit" onClick={
                onClick
            }>
                Submit
            </Button>
        </Form>

    )
}


