import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter} from 'react-router-dom'
import './index.css';
import App from './App';
import HeaderComponent from "./components/partials/HeaderComponent";

ReactDOM.render(
    <BrowserRouter>
        <HeaderComponent/>
        <App/>
    </BrowserRouter>
    , document.getElementById('root'));
