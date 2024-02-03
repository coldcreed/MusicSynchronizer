import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import Room from './Room';
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            roomCode: null,
        };
        this.clearRoomCode = this.clearRoomCode.bind(this);
    }

    //If the user is in a room already and tries to return to the homepage, they are automatically redirected to the room
    //componentDidMount means that the component just rendered for the first time on the screen.
    //asynchronous operation. Means we don't need to wait for things in the function to finish before we do other operations in the program
    
    async componentDidMount() {
        fetch('/api/user-in-room')
        .then((response) => response.json())
        .then((data) => {
            this.setState({
                roomCode: data.code
            })
        });
    }


    renderHomePage() {
        return (
            <Grid container spacing={3}>
                <Grid item xs={12} align="center">
                    <Typography variant="h3" component="h3">
                        Vibing With Friends
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <ButtonGroup disableElevation variant="contained" color="primary">
                        <Button color="primary" to='/join' component={ Link }>
                            Join A Room
                        </Button>
                        <Button color="secondary" to='/create' component={ Link }>
                            Create A Room
                        </Button>
                    </ButtonGroup>
                </Grid>
            </Grid>
        );
    }

    clearRoomCode() {
        this.setState({
          roomCode: null,
        });
      }

    //When there is a semicolon such as :roomCode, this means that it is a parameter to be filled
    render() {
        return <Router>
            <Switch>
            <Route exact path="/" render={() => {
              return this.state.roomCode ? (
                <Redirect to={`/room/${this.state.roomCode}`} />
            ) : ( 
              this.renderHomePage() 
            );
          }}>
          </Route>
                <Route path='/join' component={RoomJoinPage} />
                <Route path='/create' component={CreateRoomPage} />
                <Route
                    path="/room/:roomCode"
                    render={(props) => {
                    return <Room {...props} leaveRoomCallback={this.clearRoomCode} />;
                    }}
                />
            </Switch>

        </Router>
    }
}
