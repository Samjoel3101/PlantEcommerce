import React from 'react'
import {useHistory, Link} from 'react-router-dom' 
import {Card} from 'react-bootstrap'

const USERTYPES = {'Nursery Admin': '/nursery-admin-signup', 'Individual': '/user-signup'}

function ToggleRegister() {
    const history = useHistory() 
    const userTypeSelectCards = []
    
    for (var [key, value] of Object.entries(USERTYPES)){
        userTypeSelectCards.push(
            <Link to = {value} key = {key}>
                <Card style = {{width: '18rem'}} >
                    <Card.Body>
                        <Card.Title>{key}</Card.Title>
                    </Card.Body>
                </Card>
            </Link>
        )
    }

    return (
        <div>
            {userTypeSelectCards}      
        </div>
    )
}

export default ToggleRegister
