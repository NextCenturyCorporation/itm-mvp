var host = window.location.hostname; 
const API_URL = 'https://'+host+':9100/api';
const GRAPHQL_URL = 'http://'+host+':9100/graphql';

module.exports = {API_URL, GRAPHQL_URL};
