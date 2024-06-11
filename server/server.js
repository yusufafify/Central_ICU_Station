const express = require('express');
const fs = require('fs');
const app = express();
app.use(express.json());

// Initialize an empty object to store the data
let dataStore = {};

// Load existing data from JSON file
if (fs.existsSync('dataStore.json')) {
    let rawData = fs.readFileSync('dataStore.json');
    dataStore = JSON.parse(rawData);
}

app.post('/data', (req, res) => {
    // Check if the patient id already exists in the dataStore
    console.log(req.body);
    if (dataStore[req.body.patientId]) {
        // If it does, push the new heart rate to the existing array
        dataStore[req.body.patientId].push(req.body.heartRate);
    } else {
        // If it doesn't, create a new array with the heart rate
        dataStore[req.body.patientId] = [req.body.heartRate];
    }
    // Write the updated dataStore to the JSON file
    fs.writeFileSync('dataStore.json', JSON.stringify(dataStore));
    console.log(dataStore);
    res.status(200).send('Success');
});

app.get('/data/:patientId', (req, res) => {
    // Retrieve the patient id from the request parameters
    const patientId = req.params.patientId;
    // Check if the patient id exists in the dataStore
    if (dataStore[patientId]) {
        // If it does, send the heart rate data for that patient
        res.status(200).json(dataStore[patientId]);
    } else {
        // If it doesn't, send an error message
        res.status(404).send('Patient not found');
    }
});

app.get('/data', (req, res) => {
    // Send the entire dataStore object
    res.status(200).json(dataStore);
});

app.listen(5000, () => {
    console.log('Server is running on port 5000');
});
