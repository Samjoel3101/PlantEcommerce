import React from 'react';
import {render} from 'react-dom'; 
import UrlRouter from './Url/Route';
import {AuthProvider} from './contexts/AuthContext';


export default function App () {
    const key = typeof(localStorage.getItem('key'))
    const loggedIn = typeof(localStorage.getItem('loggedIn'))
    const userType = typeof(localStorage.getItem('userType'))
    
    if (key === loggedIn && userType === loggedIn && key !== "string"){
        localStorage.setItem('key', null)
        localStorage.setItem('loggedIn', false)
        localStorage.setItem('userType', null)
    }
    
    return (
        <AuthProvider >
            <div className = 'container'>             
                <UrlRouter />
            </div>
        </ AuthProvider>
    )
}

const AppComp = document.getElementById('app');
render(<App/>, AppComp);

 

