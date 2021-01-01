import React from 'react'
import SignUp from './SignUp'

function NurseryAdminSignUp() {
    return (
        <div>
            {SignUp({registerEndpoint: '/api/accounts/nursery-admin-register/'})}
        </div>
    )
}

export default NurseryAdminSignUp
