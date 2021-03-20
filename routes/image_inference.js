var express = require('express');
var router = express.Router();



/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('image_inference', { 
    title: 'ImageInference' 
  });
});

module.exports = router;
