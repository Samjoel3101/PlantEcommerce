import React from 'react'
import {Link} from 'react-router-dom' 

function HomePage() {
    const userType = localStorage.getItem('userType')
    var components = null 

    if (userType === 'nursery_admin'){
        components = (
            <Link to = '/nursery'>Check Nursery</Link>
        )    
    }

    return (<div>
        <h1>Plant Ecommerce Website</h1>
        <p> Browse the best plants from the best nurseries in the country </p>
        {components}
    </div>)
}
export default HomePage;
