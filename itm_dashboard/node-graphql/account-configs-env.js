const MONGO_CONFIGS = {
    MONGO_DATABASE: process.env.MONGO_DATABASE, 
    MONGO_USER: process.env.MONGO_USER,
    MONGO_PASSWORD: process.env.MONGO_PASSWORD
};

const AWS_CONFIGS = {
    ACCESS_KEY: "",
    SECRET_ACCESS_KEY: "",
    REGION: "us-east-1"
}

module.exports = {MONGO_CONFIGS, AWS_CONFIGS};