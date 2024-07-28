const mongoose = require('mongoose');

const connectToMongo = async () => {
    try {
        const mongoURI = process.env.MONGO_URI;
        const con = await mongoose.connect(mongoURI);
        //("Mongo connected");
    }
    catch (error) {
        //(error);
        process.exit();
    }
}

module.exports = connectToMongo;