import React from 'react'
import SignUp from './SignUp'

function UserSignUp() {
    return (
        <div>
            {SignUp({registerEndpoint: '/api/accounts/register/'})}
        </div>
    )
}

export default UserSignUp
