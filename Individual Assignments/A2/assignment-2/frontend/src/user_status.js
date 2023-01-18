import {useEffect, useState} from "react";
import axios from "axios";
import {Button} from "react-bootstrap";

export default function User_status() {

    const [user, setUser] = useState(null)

    const url = "https://user-status-fikbaei5vq-uw.a.run.app";

    function onClick(e) {
        e.preventDefault()
        axios.post(url + "/logout", {current_user: localStorage.getItem("user")}).then((res) => {
            localStorage.removeItem("user")
            alert("Logout successful!")
        }).catch((err) => {
            console.log(err)
            alert(err.response.data.error)
        })
    }

    useEffect(() => {
        axios.post(url + "/user_status", {current_user: localStorage.getItem("user")}).then((res) => {
            //localStorage.setItem("user",res)
            //alert("Login successful!")
            console.log(res)
            setUser(res.data)
        }).catch((err) => {
            console.log(err)
            alert(err.response.data.error)
        })

    }, [])
    if (!user) {
        return null
    }
    return (
        <div className={"m-4"}>
            <div>
                <b>CURRENT USER(S):</b>
            </div>
            <div className={"mb-2"}>
                {user.currentUser.name}
            </div>
            <div>
                <b>OTHER(S):</b>
            </div>
            <div>
                {user.others.map((ele) => <div>{ele.name}</div>)}
            </div>
            <Button className={"mt-4"} type="submit" onClick={
                onClick
            }>
                Log out
            </Button>
        </div>


    )
}