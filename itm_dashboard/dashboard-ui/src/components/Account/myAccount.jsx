import React from 'react';
import {withRouter} from 'react-router-dom';
import { accountsPassword } from '../../services/accountsService';
import $ from 'jquery';
import '../../css/my-account.css';

class MyAccountPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            userName: "",
            email: "",
            currentPassword: "",
            newPassword: "",
            confirmNewPassword: "",
            error: null
        };

        if(this.props.currentUser != null) {
            this.state.userName = this.props.currentUser.username;
            this.state.email = this.props.currentUser.emails[0].address;
        }
    }

    isFormValid() {
        let hasValidationError = false;
        let validationError = "";

        if(this.state.currentPassword === "") {
            hasValidationError = true;
            validationError += "'Current Password' cannot be blank.\n";
        }

        if(this.state.newPassword !== this.state.confirmNewPassword) {
            hasValidationError = true;
            validationError += "'New Password' and 'Confirm New Password' must match.\n";
        } else if(this.state.newPassword === "") {
            hasValidationError = true;
            validationError += "'New Password' cannot be blank.\n";
        }

        if(hasValidationError) {
            $("#pwd-change-feedback").addClass("feedback-display");
            $("#success-pwd-change").addClass("display-none");
        }

        this.setState({ error: validationError });

        return !hasValidationError;
    }

    updatePassword = async() => {
        if(this.isFormValid()) {
            try {
                await accountsPassword.changePassword(this.state.currentPassword, this.state.newPassword);
                $("#pwd-change-feedback").removeClass("feedback-display");
                $("#success-pwd-change").removeClass("display-none");

                this.setState({currentPassword: ""});
                this.setState({newPassword: ""});
                this.setState({confirmNewPassword: ""});
            } catch (err) {
                $("#pwd-change-feedback").addClass("feedback-display");
                $("#success-pwd-change").addClass("display-none")
                this.setState({ error: err.message });
            }
        }
    }

    onChangeCurrentPassword = ({target}) => {
        this.setState({currentPassword: target.value});
    }

    onChangeNewPassword = ({target}) => {
        this.setState({newPassword: target.value});
    }

    onChangeConfirmNewPassword = ({target}) => {
        this.setState({confirmNewPassword: target.value});
    }

    render() {
        return (
            <div className="my-account-container">
                <h3>My Account</h3>
                <div className="my-account-description">
                    Manage your account settings.
                </div>

                <form>
                    <div className="form-group">
                        <div className="input-header">Username</div>
                        <input className="form-control" placeholder={this.state.userName}
                        type="text" id="username"
                        disabled={true}/>
                    </div>
                </form>

                <form>
                    <div className="form-group">
                        <div className="input-header">Email Address</div>
                        <input className="form-control" placeholder={this.state.email}
                        type="text" id="email"
                        disabled={true}/>
                    </div>
                </form>

                <form>
                    <div className="my-account-update-password">
                        <div className="form-group">
                            <div className="input-header">Current Password</div>
                            <input className="form-control" placeholder="Current Password"
                            type="password" id="currentPassword" value={this.state.currentPassword}
                            onChange={this.onChangeCurrentPassword}/>
                        </div>
                        <div className="form-group">
                            <div className="input-header">New Password</div>
                            <input className="form-control" placeholder="New Password"
                            type="password" id="newPassword" value={this.state.newPassword}
                            onChange={this.onChangeNewPassword}/>
                        </div>
                        <div className="form-group">
                            <div className="input-header">Confirm New Password</div>
                            <input className="form-control" placeholder="Confirm New Password"
                            type="password" id="confirmNewPassword" value={this.state.confirmNewPassword}
                            onChange={this.onChangeConfirmNewPassword}/>
                        </div>
                        <div className="form-group">
                            <button className="btn btn-secondary" onClick={this.updatePassword} type="button">
                                Change Password
                            </button>
                        </div>
                    </div>
                    <div className="invalid-feedback pre-line" id="pwd-change-feedback">
                        {this.state.error}
                    </div>
                </form>

                <div id="success-pwd-change" className="display-none">
                    <div>Password updated successfully!</div>
                </div>
            </div>
        );
    }
}

export default withRouter(MyAccountPage);