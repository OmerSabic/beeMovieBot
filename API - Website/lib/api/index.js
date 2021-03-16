const { response } = require("express");
const express = require("express");
const fetch = require('node-fetch')
const {Client} = require('discord.js')


var app = (module.exports = express());
var firebase = require("firebase");
require("firebase/firestore");

const fbApp = firebase.initializeApp({
    projectId: process.env.PROJECTID
});

const increment = firebase.firestore.FieldValue.increment(1);

var db = firebase.firestore();

app.set("views", __dirname);
app.set("view engine", "ejs");

app.get("/api", (req, res) => {
    res.status(200).send({
        content: "API is online!",
    });
});

app.get("/api/user/:id", async (req, res) => {

    const hisRef = db.collection('history').doc(req.params.id);
    const doc = await hisRef.get();

    db.collection("history")
        .doc(req.params.id)
        .get()
        .then((data) => {
            if(!data.exists) {
                res.status(400).send("The user's ID you entered hasn't used bee movie bot yet.")
            }
            res.send(data.data());
        }).catch(err => console.log(err));
})

app.put("/api/user/increment/:id/:script/:secret", async (req, res) => {
    if(req.params.secret != process.env.API_SECRET) {
        res.status(403).send('The secret code is incorrect')
        return
    }
    var script = req.params.script
    var update = {}
    update[script] = increment

    const hisRef = db.collection('history').doc(req.params.id);
    const doc = await hisRef.get();

    if(!doc.exists) {
        db.collection("history").doc(req.params.id).set({
            "shrek2":0,
            "bee":0,
            "lotr":0,
            "communistManifesto":0,
            "kampf":0
        })
    }

    db.collection("history")
        .doc(req.params.id)
        .update(update).then(resp => {
            res.send("updated " + script + " value for " + req.params.id)
        }).catch(err => {
            if(err.code == "not-found") {
                res.status(400).send("The user ID you entered is not valid")
            }
            else {
                res.send("Bad error, no no")
            }
            return
        })

    
})


app.get("/api/user/discord/:id", (req, res) => {
    const token = process.env.DISCORD_TOKEN
    
    const client = new Client()
    client.token = token

    const fetchUser = async id => await client.users.fetch(id).then((data) => {
        if(data) {
            res.send(data)
        }
    }).catch(err => res.status(400).send("The user ID you entered is invalid"))

    fetchUser(req.params.id)
})