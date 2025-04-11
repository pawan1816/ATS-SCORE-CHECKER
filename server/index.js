const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json()); // for parsing application/json

app.get('/', (req, res) => {
  res.send('Backend server is running 🚀');
});

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
  console.log(`Hello world`);
});
