const express = require('express')
var app = express()
var admin = require('firebase-admin');

var api = require('./lib/api')
var website = require('./lib/website')

app.use(api);
app.use(website);

app.listen(process.env.PORT || 5000, () => {
    console.log('server started')
})