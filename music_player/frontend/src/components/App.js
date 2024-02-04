import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";



//Setting up a class (main component) in react. This is our entry point component App.js is usually where the entry point is.
export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (<div className="center">
            <HomePage/>
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv); 