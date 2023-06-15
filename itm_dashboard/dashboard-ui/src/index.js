import React from "react";
import ReactDOM from "react-dom";
import {App} from "./components/App";

import {ApolloProvider} from 'react-apollo';
import {apolloClient} from './services/accountsService';

ReactDOM.render(
  <ApolloProvider client={apolloClient}><App client={apolloClient}/></ApolloProvider>,
  document.getElementById("root")
);