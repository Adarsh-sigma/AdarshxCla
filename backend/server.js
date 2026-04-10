const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.json());

// Database connection
dbURI = 'mongodb://localhost:27017/bugbounty'; // Change this to your DB URI
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Routes
app.post('/scan', (req, res) => {
    // Logic for scanning repositories
    const repo = req.body.repo;
    res.json({ message: `Scanning ${repo}` });
});

app.get('/results/:id', (req, res) => {
    // Logic for getting bug detection results
    const id = req.params.id;
    res.json({ message: `Results for scan ID: ${id}` });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
