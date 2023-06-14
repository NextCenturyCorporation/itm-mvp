const { gql } = require('apollo-server');
const { dashboardDB } = require('./server.mongo');
// const mongoDb = require("mongodb");
// const { MONGO_DB } = require('./config');
const { GraphQLScalarType, Kind } = require("graphql");

const typeDefs = gql`
  scalar JSON

  scalar StringOrFloat

  extend input CreateUserInput {
    admin: Boolean
  }

  extend type User {
    admin: Boolean
  }

  type Player {
    firstName: String,
    lastName: String
  }

  type Scenario {
    id: ID
    name: String
    description: String
    startTime: String
    environment: JSON
    patients: [Patient]
    medical_supplies: [MedicalSupply]
    triage_categories: [TriageCategory]
  }

  type ScenarioState {
    id: ID
    name: String
    elapsedTime: Float
    scenario_complete: Boolean
    patients: [Patient]
    medical_supplies: [MedicalSupply]
  }

  type Probe {
    id: ID
    question: String
    patient_ids: [String]
  }

  type Patient {
    id: ID
    name: String
    age: Int
    sex: Sex
    injuries: [Injury]
    vitals: Vitals
    mental_status: MentalStatus
    assessed: Boolean
    tag: TriageTag
  }

  type Injury {
    name: String
    location: String
  }

  type Vitals {
    heart_rate: Int
    blood_pressure: String
    respiratory_rate: Int
    oxygen_level: Int
  }

  type TriageCategory {
    tagLabel: TriageTag
    description: String
    criteria: String
  }

  type MedicalSupply {
    name: String
    description: String
    quantity: Int
  }

  enum Sex {
    male
    female
    unknown
  }

  enum MentalStatus {
    calm
    confused
    upset
    agony
    unresponsive
  }

  enum TriageTag {
    none
    minimal
    delayed
    immediate
    expectant
    deceased
  }

  type Query {
    getUsers: JSON
    getHistory(id: ID): JSON
    getAllHistory(id: ID): [JSON]
    getScenario(id: ID): Scenario
    getAllScenarios: [Scenario]
    getScenarioState(id: ID): ScenarioState
    getAllScenarioStates: [ScenarioState]
    getProbe(id: ID): Probe
    getAllProbes: [Probe]
    getPatient(id: ID): Patient
    getAllPatients: [Patient]
    getInjury(id: ID): Injury
    getAllInjuries: [Injury]
    getVitals(id: ID): Vitals
    getAllVitals: [Vitals]
    getTriageCategory(id: ID): TriageCategory
    getAllTriageCategories: [TriageCategory]
    getMedicalSupply(id: ID): MedicalSupply
    getAllMedicalSupplies: [MedicalSupply]
  }

  type Mutation {
    updateAdminUser(username: String, isAdmin: Boolean): JSON
  }
`;

const resolvers = {
    Query: {
      getHistory: async (obj, args, context, infow) => {
        return await dashboardDB.db.collection('test').findOne(args).then(result => { return result; });
      },
      getAllHistory: async (obj, args, context, infow) => {
        return await dashboardDB.db.collection('test').find().toArray().then(result => { return result; });
      },
      getScenario: async (obj, args, context, infow) => {
        return await dashboardDB.db.collection('scenarios').findOne(args).then(result => { return result; });
      },
      getAllScenarios: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('scenarios').find().toArray().then(result => { return result; });
      },
      getScenarioState: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('scenarioStates').findOne(args).then(result => { return result; });
      },
      getAllScenarioStates: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('scenarioStates').find().toArray().then(result => { return result; });
      },
      getProbe: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('probes').findOne(args).then(result => { return result; });
      },
      getAllProbes: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('probes').find().toArray().then(result => { return result; });
      },
      getPatient: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('patients').findOne(args).then(result => { return result; });
      },
      getAllPatients: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('patients').find().toArray().then(result => { return result; });
      },
      getInjury: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('injuries').findOne(args).then(result => { return result; });
      },
      getAllInjuries: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('injuries').find().toArray().then(result => { return result; });
      },
      getVitals: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('vitals').findOne(args).then(result => { return result; });
      },
      getAllVitals: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('vitals').find().toArray().then(result => { return result; });
      },
      getTriageCategory: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('triageCategories').findOne(args).then(result => { return result; });
      },
      getAllTriageCategories: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('triageCategories').find().toArray().then(result => { return result; });
      },
      getMedicalSupply: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('medicalSupplies').findOne(args).then(result => { return result; });
      },
      getAllMedicalSupplies: async (obj, args, context, infow) => {
          return await dashboardDB.db.collection('medicalSupplies').find().toArray().then(result => { return result; });
      }
    },
    Mutation: {
        updateAdminUser: async(obj, args, context, infow) => { 
            return await dashboardDB.db.collection('users').update(
                {"username": args["username"]}, 
                {$set: {"admin": args["isAdmin"]}}
            );
        }
    },
    StringOrFloat: new GraphQLScalarType({
        name: "StringOrFloat",
        description: "A String or a Float union type",
        serialize(value) {
          if (typeof value !== "string" && typeof value !== "number" && typeof value !== "boolean") {
            throw new Error("Value must be either a String, Boolean, or an Int");
          }
    
          return value;
        },
        parseValue(value) {
          if (typeof value !== "string" && typeof value !== "number" && typeof value !== "boolean") {
            throw new Error("Value must be either a String, Boolean, or an Int");
          }

          return value;
        },
        parseLiteral(ast) {
          switch (ast.kind) {
            case Kind.FLOAT: return parseFloat(ast.value);
            case Kind.STRING: return ast.value;
            case Kind.BOOLEAN: return ast.value;
            default:
              throw new Error("Value must be either a String, Boolean, or a Float");
          }
        }
    })
};

module.exports = {
    typeDefs,
    resolvers
};
