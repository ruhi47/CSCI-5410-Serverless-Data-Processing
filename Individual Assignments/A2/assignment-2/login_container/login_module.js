const express = require('express');
const port = process.env.PORT || 8080; //The port we'll listen on
const cors = require('cors');
const {Firestore} = require("@google-cloud/firestore");
const app = express(); // Created a ExpressJS app
const bodyparser= require('body-parser')

const database = new Firestore({
    projectId: "assignment2-csci5409",
    keyFilename: "./assignment2-csci5409-37f848f9e5f9.json"
});
//Function to listen on the port
app.use(cors());
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({extended: false}));

//Route to home page
app.get('/', (req,res) =>{
    res.render('Hi, welcome to login page!')
})
//Send to login page in response
app.post('/login', async (req, res)=>{
    //Login code
    console.log("Request creds", req);

    //if fields are empty
    if(!req.body){
        return res.status(400).send({
            message: "The user details cannot be empty. Try again!"
        })
    }

    const userCred = {
        email: req.body?.email,
        password: req.body?.password
    }
    const document = await database.collection("registration-data").get();

    let currentUser;
    document.forEach((doc) => {
        if (doc.get("email") === userCred.email && doc.get("password") === userCred.password) {
            currentUser = doc.id;
        }
    });
if(!currentUser){
    return res.status(400).send({"error" : "invalid creds"});
}
    const collection = await database.collection("state").get();
    const document3 = database.collection("state").doc("current-user");
    if (!collection.size) {
        await document3.set({online: [currentUser]});
        res.send({"current_user": currentUser});
    }
    else{
        let online1 = [];
        collection.forEach((state) => {
            const tempOnline = state.get("online");
            let userExists = false;
            for (let i = 0; i < tempOnline.length; i++) {
                if (tempOnline[i] === currentUser) {
                    userExists = true;
                }
            }
            if (!userExists) {
                tempOnline.push(currentUser);
            }
            online1 = tempOnline;
        });
        await document3.update({online: online1});
        res.send({"current_user": currentUser});
    }

})


// Function to listen on the port
app.listen(port, () => console.log(`This app is listening on port ${port}`));