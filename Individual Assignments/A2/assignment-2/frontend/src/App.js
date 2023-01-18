import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Register from "./register";
import Login from "./login";
import User_status from "./user_status";


function App() {
  return (
      <BrowserRouter>
        <Switch>
          <Route path="/register" >
              <Register/>
          </Route>
            <Route path="/login" >
                <Login/>
            </Route>
            <Route path="/user_status" >
                <User_status/>
            </Route>
        </Switch>
      </BrowserRouter>
  );
}

export default App;
