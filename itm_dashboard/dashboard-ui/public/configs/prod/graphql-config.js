var host = window.location.hostname; 
const RESET_PASSWORD_URL = "https://" + host + ":3000/reset-password";
const GRAPHQL_PORT = 9100;
const MONGO_DB = 'dashboard';

module.exports = {RESET_PASSWORD_URL, GRAPHQL_PORT, MONGO_DB};