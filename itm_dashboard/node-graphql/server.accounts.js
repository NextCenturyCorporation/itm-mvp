const { ApolloServer } = require('apollo-server');
const { makeExecutableSchema } = require('@graphql-tools/schema');
const { mergeTypeDefs, mergeResolvers } = require('@graphql-tools/merge');
const { AccountsModule } = require('@accounts/graphql-api');
const { accountsServer } = require('./server.mongo');
const { typeDefs, resolvers } = require('./server.schema');
const { GRAPHQL_PORT } = require('./config');

// Generate the accounts-js GraphQL module
const accountsGraphQL = AccountsModule.forRoot({ accountsServer });

// Merge our schema and the accounts-js schema
const schema = makeExecutableSchema({
    typeDefs: mergeTypeDefs([typeDefs, accountsGraphQL.typeDefs]),
    resolvers: mergeResolvers([accountsGraphQL.resolvers, resolvers]),
    schemaDirectives: {
        ...accountsGraphQL.schemaDirectives,
    }
});

const server = new ApolloServer({ schema, context: accountsGraphQL.context});

// The `listen` method launches a web server
server.listen(GRAPHQL_PORT).then(({ url }) => {
    console.log(`🚀  Server ready at ${url}`);
});