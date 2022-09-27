const express = require('express');
const router = express.Router();


//Importing Controllers
const mainController = require('../controller/main');

router.get('/',mainController.home);

router.get('/getUpdatedIP',mainController.getNewIP);

module.exports = router;