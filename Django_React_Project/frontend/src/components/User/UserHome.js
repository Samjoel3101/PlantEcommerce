import React from 'react'
import {Link} from 'react-router-dom' 
import {Button} from 'react-bootstrap' 

import {homePage} from '../Nursery/NurseryHome'

export default function UserHome() {
    return (
        <div>
            <Link to = '/user/cart'>
                <Button variant = 'primary'>Cart</Button> 
            </Link>

            {homePage({endpoint: '/api/user/feed/'})}
        </div>
        )
}
