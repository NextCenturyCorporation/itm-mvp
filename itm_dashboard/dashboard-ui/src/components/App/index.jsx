import React from 'react';
import queryString from 'query-string';
import HomePage from '../Home/home';
import ScoreChart from '../ScoreChart/scoreChart';
import ScenarioPage from '../ScenarioPage/scenarioPage';
import {Router, Switch, Route, Link} from 'react-router-dom';
import LoginApp from '../Account/login';
import ResetPassPage from '../Account/resetPassword';
import MyAccountPage from '../Account/myAccount';
import AdminPage from '../Account/adminPage';
import {accountsClient, accountsGraphQL} from '../../services/accountsService';
import NavDropdown from 'react-bootstrap/NavDropdown';
import {createBrowserHistory} from 'history';

// CSS and Image Stuff 
import '../../css/app.css';
import 'rc-slider/assets/index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import 'jquery/dist/jquery.min.js';
import 'material-design-icons/iconfont/material-icons.css';
import 'react-dropdown/style.css';
import 'react-dual-listbox/lib/react-dual-listbox.css';

import brandImage from '../../img/itm-cross.png';
import userImage from '../../img/account_icon.png';

const history = createBrowserHistory();

function Home({newState}) {
    if(newState.currentUser == null) {
        history.push('/login');
    }

    return <HomePage/>;
}

function Scores() {
    return <ScoreChart/>;
}

function Scenarios() {
    return <ScenarioPage/>;
}

function Login({newState, userLoginHandler, updateHandler}) {
    if(newState.currentUser !== null) {
        return <Home newState={newState}/>;
    } else {
        return <LoginApp userLoginHandler={userLoginHandler}/>;
    }
}

function MyAccount({newState, userLoginHandler}) {
    if(newState.currentUser == null) {
        history.push("/login");
    }

    return <MyAccountPage currentUser={newState.currentUser} updateUserHandler={userLoginHandler}/>
}

function Admin({newState, userLoginHandler}) {
    if(newState.currentUser == null) {
        history.push("/login");
    }

    // Do not let users who aren't admins somehow go to the admin page
    if(newState.currentUser !== null && newState.currentUser.admin === true) {
        return <AdminPage currentUser={newState.currentUser} updateUserHandler={userLoginHandler}/>
    } else {
        return <Home newState={newState}/>;
    } 
}

export class App extends React.Component {

    constructor(props) {
        super(props);

        this.state = queryString.parse(window.location.search);
        this.state.currentUser = null;
    
        this.logout = this.logout.bind(this);
        this.userLoginHandler = this.userLoginHandler.bind(this);
    }

    async componentDidMount() {
        //refresh the session to get a new accessToken if expired
        const tokens = await accountsClient.refreshSession();

        if(window.location.href.indexOf("reset-password") > -1) {
            return;
        }

        if (!tokens) {
          history.push('/login');
          return;
        }

        const user = await accountsGraphQL.getUser(
          tokens ? tokens.accessToken : ''
        );

        this.setState({ currentUser: user});
    }

    async logout() {
        await accountsClient.logout();
        history.push('/login');
        this.setState({currentUser: null});
    }

    userLoginHandler(userObject) {
        this.setState({ currentUser: userObject });
    }

    render() {
        const {currentUser} = this.state;
        return (
            <Router history={history}>
                <div className="itm-app">
                    {currentUser && 
                        <nav className="navbar navbar-expand-lg navbar-light bg-light itm-navbar">
                            <a className="navbar-brand" href="/">
                                <img className="nav-brand-itm" src={brandImage} alt=""/>
                            </a>
                            <ul className="navbar-nav custom-nav">
                                <li className="nav-item">
                                    <Link className="nav-link-home" to="/">Home</Link>
                                </li>
                                <li className="nav-item">
                                    <Link className="nav-link-home" to="/scores">Scores</Link>
                                </li>
                                <li className="nav-item">
                                    <Link className="nav-link-home" to="/scenarios">Scenarios</Link>
                                </li>
                            </ul>
                            <ul className="navbar-nav ml-auto">
                                <li className="login-user">
                                    <div className="login-user-content">
                                        <img className="nav-login-icon" src={userImage} alt=""/>
                                        <NavDropdown
                                        title={currentUser.emails[0].address}
                                        id="basic-nav-dropdown"
                                        show={this.state.menuIsOpened}
                                        onToggle={this.handleToggle}
                                        >
                                        <Link className="dropdown-item" to="/myaccount" onClick={this.handleToggle}>
                                            My Account
                                        </Link>
                                        {this.state.currentUser.admin === true && (
                                            <Link className="dropdown-item" to="/admin" onClick={this.handleToggle}>
                                            Administrator
                                            </Link>
                                        )}
                                        <Link className="dropdown-item" to={{}} onClick={this.logout}>
                                            Logout
                                        </Link>
                                        </NavDropdown>
                                    </div>
                                </li>
                            </ul>
                        </nav>
                    }

                    <Switch>
                        <Route exact path="/">
                            <Home newState={this.state}/>
                        </Route>
                        <Route exact path="/scores">
                            <Scores/>
                        </Route>
                        <Route exact path="/scenarios">
                            <Scenarios/>
                        </Route>
                        <Route path="/login">
                            <Login newState={this.state} userLoginHandler={this.userLoginHandler}/>
                        </Route>
                        <Route path="/reset-password/:token" component={ResetPassPage}/>
                        <Route path="/myaccount">
                            <MyAccount newState={this.state} userLoginHandler={this.userLoginHandler}/>
                        </Route>
                        <Route path="/admin">
                            <Admin newState={this.state} userLoginHandler={this.userLoginHandler}/>
                        </Route>
                    </Switch>
                </div>
            </Router>
        );
    }
}