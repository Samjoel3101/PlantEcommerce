import React from 'react'
import {Link} from 'react-router-dom' 
import {authContext} from '../contexts/AuthContext'

function HomePage() {
    const userType = localStorage.getItem('userType')
    var components = null 
    const [isLoggedIn, setIsLoggedIn] = authContext() 

    if (isLoggedIn && userType === 'nursery_admin'){
        components = (
            <Link to = '/nursery'>Check Nursery</Link>
        )    
    }else if (isLoggedIn && userType === 'user'){
        components = (
            <Link to = '/user/feed'>Start Buying</Link>
        )
    }

    return (<div>
        <h1>Plant Ecommerce Website</h1>
        <p> Browse the best plants from the best nurseries in the country </p>
        {components}
    </div>)
}
export default HomePage;
