const express = require('express');
const cors = require('cors');

app = express();

app.use(cors());
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const additionService = (req, res) => {
    const number1 = parseInt(req.body.number1);
    const number2 = parseInt(req.body.number2);

    const result = {
        'status': 'success',
        'result': number1 + number2
    };

    return res.status(200).send(result);
}

app.post('/addition', additionService);

const serverPort = process.env.ADDITION_SERVICE_PORT || 3000;
const serverAddress = process.env.ADDITION_SERVICE_ADDRESS || 'localhost';

app.listen(serverPort, () => {
    console.log(`listen on http://${serverAddress}:${serverPort}`);
});