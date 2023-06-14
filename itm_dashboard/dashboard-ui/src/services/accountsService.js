import { AccountsClient } from '@accounts/client';
import { AccountsClientPassword } from '@accounts/client-password';
import GraphQLClient from '@accounts/graphql-client';
import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import {GRAPHQL_URL} from './config'
import gql from 'graphql-tag';

console.log("uri", GRAPHQL_URL, "1002");

const httpLink = createHttpLink({
  uri: GRAPHQL_URL
});

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
});

const accountsGraphQL = new GraphQLClient({
  graphQLClient: apolloClient,
  userFieldsFragment: gql`
    fragment userFields on User {
      id
      emails {
        address
        verified
      }
      username
      admin
    }
  `,
});

const accountsClient = new AccountsClient({}, accountsGraphQL);
const accountsPassword = new AccountsClientPassword(accountsClient);

export { accountsClient, accountsGraphQL, accountsPassword, apolloClient };