//ENV FILE IMPORTED
require('dotenv').config({path : './.env'})

//Modules
const axios = require('axios');

exports.home = (req,res,next) => {
    res.status(200).json({
        message : "Server Started Working! 🚀"
    })
}

exports.getNewIP = async(req,res,next) => {
    try{
     const getIP = await axios.get(process.env.URL);
     if(getIP===null)
     {
        res.status(400).json({
            status : false,
            message : "Check the Given URL",
        })
      }
     else
     {
        res.status(200).json({
            status : true,
            message : "Got the Data",
            ip : getIP.data
        })
     }
    }
    catch(err)
    {
        console.log(err)
        res.status(500).json({
            status : false,
            message : "Some Error Caused While Fetching New IP.",
            err : err
        })
    }
}