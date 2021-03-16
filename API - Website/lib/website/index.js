const { response } = require('express');
const express = require('express');
var app = module.exports = express();
const request = require('request')
const ejs = require('ejs')

app.set('views', __dirname+'/views');
app.use(express.static(__dirname + '/public'));
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.render('index')
})

app.get('/info', (req, res) => {
    res.status(400).redirect("/error/Please insert a Discord user ID")
})

app.get('/info/:id', (req, res, next) => {

    var fullUrl = req.protocol + '://' + req.get('host');
    request(fullUrl + "/api/user/discord/" + req.params.id, (err, response, body) => {
        if(err) {
            res.send(err)
        }
        if(response.statusCode === 400) {
            res.status(400).redirect('/error/The user ID you entered is invalid')
            return
        }
        request(fullUrl + "/api/user/" + req.params.id, (err1, response1, body1) => {
            if(err1) {
                res.send(err1)

            }
            if(response1.statusCode === 400) {
                res.status(400).redirect("/error/The user's ID you've entered hasn't used Bee Movie Bot yet. TEACH THEM THE WAY!")
                return
            }
            res.render("info", {userData: JSON.parse(body), historyData: JSON.parse(body1)})
        })  
    })  
})


app.get('/error/:message', (req, res) => {
    res.render('error', {errorMessage: req.params.message})
})

app.get('/404', (req, res) => {
    res.status(404).render('404')
})