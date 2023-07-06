const mongoose = require('mongoose');
const { Mongo } = require('@accounts/mongo');
const { AccountsServer } = require('@accounts/server');
const { AccountsPassword } = require('@accounts/password');
const nodemailer = require("nodemailer");
const { RESET_PASSWORD_URL} = require('./config');
const { MONGO_CONFIGS, AWS_CONFIGS } = require('./account-configs');
let AWS = require('aws-sdk');

// AWS.config.update({
//   accessKeyId: AWS_CONFIGS.ACCESS_KEY,
//   secretAccessKey: AWS_CONFIGS.SECRET_ACCESS_KEY,
//   region: AWS_CONFIGS.REGION
// });
// 
// let transporter = nodemailer.createTransport({
//   SES: new AWS.SES({
//     apiVersion: '2010-12-01'
//   })
// });

// We connect mongoose to our local mongodb database
const connection = mongoose.connect('mongodb://dashboard-mongo:27017/dashboard', {
        useNewUrlParser: true,
        useUnifiedTopology: true,
        useCreateIndex: true,
        user: MONGO_CONFIGS.MONGO_USER,
        pass: MONGO_CONFIGS.MONGO_PASSWORD
    })
    .then(res => console.log( 'Database Connected' ))
    .catch(err => console.log( err.message, err ));

const dashboardDB = new Mongo(mongoose.connection);

const accountsPassword = new AccountsPassword({});

const accountsServer = new AccountsServer(
  {
    db: dashboardDB,
    tokenSecret: 'dashboardPassword',
    sendMail: ({ from, subject, to, text, html }) => {
      from = "patronus.engineering@gmail.com";
      transporter.sendMail({
        from,
        to,
        subject,
        text,
        html,
      }, (err, info) => {
        console.log(err);
        console.log(info);
      });
    },
    emailTemplates: {
      resetPassword: {
        subject: (user) => `Verify your account email ${user.username}`,
        text: function (user, url) {
          let token = url.substring(url.lastIndexOf('/'));
          let new_url = RESET_PASSWORD_URL + token;

          return `To verify your account email please click on this link: ${new_url}`;
        },
        html: function(user, url) {
          let token = url.substring(url.lastIndexOf('/'));
          let new_url = RESET_PASSWORD_URL + token;

          return `<p>To verify your account email please click on this link: <a href="${new_url}">Reset Password Here</a><p>`;
        }
      }
    }
  },
  {
    password: accountsPassword,
  }
);

module.exports = {
    dashboardDB,
    accountsServer
};