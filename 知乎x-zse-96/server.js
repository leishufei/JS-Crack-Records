const {get_signature} = require("./webpack.js")
const express = require('express')
const bodyParser = require("body-parser")
const app = express()
app.use(bodyParser());

app.post('/get_signature', function (req, res) {
        let body = req.body
        let data = body.data

        signature = get_signature(data)
        res.send(signature)
    })

var port = 3002;
app.listen(port, () => {
    console.log('开启服务，端口：' + port)
})