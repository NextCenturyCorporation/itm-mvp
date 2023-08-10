var host = process.env.ITM_HOSTNAME; 
if (!host || host === "") host = "localhost";

const RESET_PASSWORD_URL = "https://" + host + ":3000/reset-password";
const GRAPHQL_PORT = 9100;
const MONGO_DB = 'dashboard';

module.exports = {RESET_PASSWORD_URL, GRAPHQL_PORT, MONGO_DB};