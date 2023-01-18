const express = require('express');
const port = process.env.PORT || 8080; //The port we'll listen on
const cors = require('cors');
const {Firestore} = require("@google-cloud/firestore");
const bodyparser = require("express");
const app = express(); // Created a ExpressJS app

app.use(cors());

app.use(bodyparser.json());

app.use(bodyparser.urlencoded({extended: true}));

const database = new Firestore({
    projectId: "assignment2-csci5409",
    keyFilename: "./assignment2-csci5409-37f848f9e5f9.json"
});

app.get('/', (req, res) => {
    res.send('User Status')
})

app.post('/user_status', async (req, res) => {
    if (!req.body) {
        return res.status(400).send({
            message: "The user details cannot be empty. Try again!"
        })
    }

    const userCred = {
        current_user: req.body?.current_user
    }
    const document = await database.collection("registration-data").get();

    let isUserExists;
    document.forEach((doc) => {
        if (doc.id === userCred.current_user) {
            isUserExists = true;
        }
    });
    if (!isUserExists) {
        return res.status(400).send({"error": "User does not exist"});
    }
    let apiResponse = {};
    let others = [];
    const collection = await database.collection('state').get();
    collection.forEach((state) => {
        const online = state.get("online");
        document.forEach((doc) => {
            if (online.includes(doc.id)) {
                if (doc.id === userCred.current_user) {
                    apiResponse.name = doc.get("name");
                } else {
                    others.push({name: doc.get("name")});
                }
            }
        });
    });
    return res.send({currentUser: apiResponse, others})
})

app.post('/logout', async (req, res) => {
    if (!req.body) {
        return res.status(400).send({
            message: "The user details cannot be empty. Try again!"
        })
    }

    const userCred = {
        current_user: req.body?.current_user
    }
    const document = await database.collection("registration-data").get();

    let isUserExists;
    document.forEach((doc) => {
        if (doc.id === userCred.current_user) {
            isUserExists = true;
        }
    });
    if (!isUserExists) {
        return res.status(400).send({"error": "User does not exist"});
    }
    const collection = await database.collection("state").get();
    let online_latest = [];
    collection.forEach((state) => {
        let online = state.get("online");
        online_latest = online.filter((ele) => ele !== userCred.current_user);
    });
    const document2 = database.collection("state").doc("current-user");
    await document2.update({online: online_latest});
    res.send({"success": "log out success"});
})


app.listen(port, () => {
    console.log(`Server Started and listening on http://localhost:${port}`)
})






