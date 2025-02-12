const express = require('express');

const app = express();
const port = 3214;

app.use(express.json());
app.use((req, res, next) => {
    console.log(`${req.method} request for '${req.url}'`);
    next();
});

app.post('/data', (req, res) => {
    const receivedData = req.body;
    console.log('Received data:', receivedData);
    res.send('Data received');
});

app.listen(port, function() {
    console.log('The port is connected to 3214');
});
