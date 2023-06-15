import React from 'react';
import {accountsPassword} from '../../services/accountsService';
import {withRouter} from 'react-router-dom';
import $ from 'jquery';

import brandImage from '../../img/logo.png';

class LoginApp extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            userName: "",
            password: "",
            error: null,
            createUserName: "",
            createPassword: "",
            createEmail: "",
            forgotEmail: ""
        };

        this.login = this.login.bind(this);
        this.createAccount = this.createAccount.bind(this);
    }

    createAccount = async() => {
        $("#create-account-feedback").removeClass("feedback-display");
        try {
            let results = await accountsPassword.createUser({
                username: this.state.createUserName,
                password: this.state.createPassword,
                email: this.state.createEmail
            });

            results = await accountsPassword.login({
                password: this.state.createPassword,
                user: {
                    email: this.state.createEmail,
                }
            });

            this.props.history.push('/');
            this.props.userLoginHandler(results.user);
        } catch (err) {
            $("#create-account-feedback").addClass("feedback-display");

            this.setState({ error: err.message });
        }
    }

    login = async() => {
        $("#sign-in-feedback").removeClass("feedback-display");
        try {
            let results;
            if(this.state.userName.indexOf('@') > -1) {
                results = await accountsPassword.login({
                    password: this.state.password,
                    user: {
                        email: this.state.userName,
                    }
                });
            } else {
                results = await accountsPassword.login({
                    password: this.state.password,
                    user: {
                        username: this.state.userName,
                    }
                });
            }

            this.props.history.push('/');
            this.props.userLoginHandler(results.user);
        } catch (err) {
            $("#sign-in-feedback").addClass("feedback-display");
            this.setState({ error: err.message });
        }
    }

    resetPassword = async() => {
        try {
            await accountsPassword.requestPasswordReset(this.state.forgotEmail);

            $("#send-forgot-email-pane").addClass("display-none");
            $("#success-forgot-email-pane").removeClass("display-none");
        } catch (err) {
            $("#reset-password-feedback").addClass("feedback-display");
            this.setState({ error: err.message });
        }
    }

    onChangeUserName = ({target}) => {
        this.setState({userName: target.value});
    }

    onChangePassword = ({target}) => {
        this.setState({password: target.value});
    }

    onChangeCreateUserName = ({target}) => {
        this.setState({createUserName: target.value});
    }

    onChangeCreateEmail = ({target}) => {
        this.setState({createEmail: target.value});
    }

    onChangeCreatePassword = ({target}) => {
        this.setState({createPassword: target.value});
    }

    onChangeForgotEmail = ({target}) => {
        this.setState({forgotEmail: target.value});
    }

    showSignIn = (evt) => {
        $("#sign-in-pane").removeClass("display-none");
        $("#forgot-password-pane").addClass("display-none");
    };

    forgotPasswordLink = (evt) => {
        $("#sign-in-pane").addClass("display-none");
        $("#forgot-password-pane").removeClass("display-none");
    };

    render() {
        return (
            <div className="container-fluid vertical-height-100">
                <div className="row justify-content-center align-items-center h-100 center-container">
                    <div className="col col-md-4 login-container">
                        <div className="login-header-logo">
                            <div className="d-flex justify-content-center"><img className="nav-brand" src={brandImage} alt=""/></div>
                            <div className="d-flex justify-content-center login-header-text">Dashboard</div>
                        </div>
                        <div>
                            <ul className="nav nav-tabs" id="myTab" role="tablist">
                                <li className="nav-item">
                                    <a className="nav-link" id="create-tab" data-toggle="tab" href="#create" role="tab" aria-controls="create" aria-selected="false">Create Account</a>
                                </li>
                                <li className="nav-item">
                                    <a className="nav-link active" id="login-tab" data-toggle="tab" href="#login" role="tab" aria-controls="login" aria-selected="true" onClick={this.showSignIn}>Sign In</a>
                                </li>
                            </ul>
                            <div className="tab-content login-tab-content" id="myTabContent">
                                <div className="tab-pane fade" id="create" role="tabpanel" aria-labelledby="create-tab">
                                    <div className="sign-in-instructions">
                                        <div className="sign-in-header">Create Account</div>
                                        <div>Create an account to save, share and comment on queries.</div>
                                    </div>
                                    <form>
                                        <div className="form-group">
                                            <div className="input-login-header">Email Address</div>
                                            <input className="form-control form-control-lg" placeholder="Email" type="text" id="createEmail" value={this.state.createEmail} onChange={this.onChangeCreateEmail}/>
                                        </div>
                                        <div className="form-group">
                                            <div className="input-login-header">Username</div>
                                            <input className="form-control form-control-lg" placeholder="Username" type="text" id="createUserName" value={this.state.createUserName} onChange={this.onChangeCreateUserName}/>
                                        </div>
                                        <div className="form-group">
                                            <div className="input-login-header">Password</div>
                                            <input className="form-control form-control-lg" placeholder="Password" type="password" id="createPassword" value={this.state.createPassword} onChange={this.onChangeCreatePassword}/>
                                        </div>
                                        <div className="form-group">
                                            <button className="btn btn-primary btn-lg btn-block" onClick={this.createAccount} type="button">Create Account</button>
                                        </div>
                                        <div className="invalid-feedback" id="create-account-feedback">
                                            {this.state.error}
                                        </div>
                                    </form>
                                </div>
                                <div className="tab-pane fade show active" id="login" role="tabpanel" aria-labelledby="login-tab">
                                    <div id="sign-in-pane">
                                        <div className="sign-in-instructions">
                                            <div className="sign-in-header">Sign in</div>
                                            <div>Sign in using your username or email address.</div>
                                        </div>
                                        <form>
                                            <div className="form-group">
                                                <div className="input-login-header">Email Address or Username</div>
                                                <input className="form-control form-control-lg" placeholder="Email / Username" type="text" id="userName" value={this.state.userName} onChange={this.onChangeUserName}/>
                                            </div>
                                            <div className="form-group">
                                                <div className="input-login-header">Password</div>
                                                <input className="form-control form-control-lg" placeholder="Password" type="password" id="password" value={this.state.password} onChange={this.onChangePassword}/>
                                            </div>
                                            <div className="form-group">
                                                <div className="forgot-password">
                                                    <a className="" id="forgot-pass-tab" href="#forgot" onClick={this.forgotPasswordLink}>Forgot Password?</a>
                                                </div>
                                            </div>
                                            <div className="form-group">
                                                <button className="btn btn-primary btn-lg btn-block" onClick={this.login} type="button">Sign In</button>
                                            </div>
                                            <div className="invalid-feedback" id="sign-in-feedback">
                                                {this.state.error}
                                            </div>
                                        </form>
                                    </div>
                                    <div id="forgot-password-pane" className="display-none">
                                        <div id="send-forgot-email-pane">
                                            <div className="sign-in-instructions">
                                                <div className="sign-in-header">Forgot Password</div>
                                                <div>Enter your email address to reset password.</div>
                                            </div>
                                            <form>
                                                <div className="form-group">
                                                    <div className="input-login-header">Email Address</div>
                                                    <input className="form-control form-control-lg" placeholder="Email" type="text" id="forgotEmail" value={this.state.forgotEmail} onChange={this.onChangeForgotEmail}/>
                                                </div>
                                                <div className="form-group">
                                                    <button className="btn btn-primary btn-lg btn-block" onClick={this.resetPassword} type="button">Send Reset Email</button>
                                                </div>
                                                <div className="invalid-feedback" id="reset-password-feedback">
                                                    {this.state.error}
                                                </div>
                                            </form>
                                        </div>
                                        <div id="success-forgot-email-pane" className="display-none">
                                            <div className="sign-in-instructions">
                                                <div className="sign-in-header">Email sent!</div>
                                                <div>Check your email for a link to reset your password.</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default withRouter(LoginApp);