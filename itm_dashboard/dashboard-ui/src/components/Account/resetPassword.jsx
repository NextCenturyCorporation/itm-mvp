import React from 'react';
import {accountsPassword} from '../../services/accountsService';
import {withRouter} from 'react-router-dom';
import $ from 'jquery';

import brandImage from '../../img/logo.png';

class ResetPassPage extends React.Component {

    constructor(props) {
        let resetToken = null;
        if(props && props.match && props.match.params) {
            resetToken = props.match.params.token;
        }

        super(props);
        this.state = {
            password: "",
            resetTokenPass: resetToken,
            error: null
        };

        this.changePassword = this.changePassword.bind(this);
    }

    changePassword = async() => {
        try {
            await accountsPassword.resetPassword(this.state.resetTokenPass, this.state.password);

            $("#change-password-panel").addClass("display-none");
            $("#change-success-panel").removeClass("display-none");
        } catch (err) {
            $("#sign-in-feedback").addClass("feedback-display");
            this.setState({ error: err.message });
        }
    }

    onChangePassword = ({target}) => {
        this.setState({password: target.value});
    }

    gotoLogin = (evt) => {
        this.props.history.push('/login');
        
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
                            <div className="login-tab-content">
                                <div className="" id="change-password-panel">
                                    <div className="sign-in-instructions">
                                        <div className="sign-in-header">Forgot Password?</div>
                                        <div>Enter a new password.</div>
                                    </div>
                                    <form>
                                        <div className="form-group">
                                            <div className="input-login-header">Password</div>
                                            <input className="form-control form-control-lg" placeholder="Password" type="password" id="password" value={this.state.password} onChange={this.onChangePassword}/>
                                        </div>
                                        <div className="form-group">
                                            <button className="btn btn-primary btn-lg btn-block" onClick={this.changePassword} type="button">Change Password</button>
                                        </div>
                                        <div className="invalid-feedback" id="sign-in-feedback">
                                            {this.state.error}
                                        </div>
                                    </form>
                                </div>
                                <div className="display-none" id="change-success-panel">
                                    <div className="sign-in-instructions">
                                        <div className="sign-in-header">Success!</div>
                                        <div>Your password has been updated!  <a href="#passchanged" onClick={this.gotoLogin}>Click here to sign in.</a></div>
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

export default withRouter(ResetPassPage);