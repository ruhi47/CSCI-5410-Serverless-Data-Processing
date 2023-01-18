const express = require('express');
const port = process.env.PORT || 8080; //The port we'll listen on
const cors = require('cors');
const {Firestore} = require("@google-cloud/firestore");
const bodyparser = require("express");
const app = express(); // Created a ExpressJS app

app.use(cors());

app.use(bodyparser.json());

app.use(bodyparser.urlencoded({extended:true}));

const database = new Firestore({
    projectId: "assignment2-csci5409",
    keyFilename: "./assignment2-csci5409-37f848f9e5f9.json"
});

app.get('/', (req, res) => {
    res.send('Welcome to registration.')
})

app.post('/register',async (req,res)=>{
    console.log("my request",req);

    if(!req.body){
        res.status(400).send({
            message: "The user details cannot be empty. Try again!"
        })
    }
    const user = {
        Name : req.body?.name,
        Email: req.body?.email,
        Password: req.body?.password,
        Location: req.body?.location
    }
    const document1 = await database.collection("registration-data").get();

    let currentUser;
    document1.forEach((doc) => {
        if (doc.get("email") === user.Email) {
            currentUser = doc.id;
        }
    });
    if(currentUser){
        return res.status(400).send({"error":"email exists!"})
    }

    const document = database.collection("registration-data").doc();
    await document.set({
        name : user.Name,
        email: user.Email,
        password: user.Password,
        location: user.Location
    })
    return res.send({"success": "user registered"});
})

app.listen(port, () => {
    console.log(`Server Started and listening on http://localhost:${port}`)
})