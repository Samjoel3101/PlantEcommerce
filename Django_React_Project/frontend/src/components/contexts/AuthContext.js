import React , {createContext, useContext, useEffect, useState} from 'react'
import {djangoFetch} from '../djangoUtils/djangoFetch' 

const AuthContext = createContext()

export  function AuthProvider ({children}) {
    
    const loggedIn = localStorage.getItem('loggedIn') === 'false' ? false : true
    const [validUser, setValidUser] = useState(loggedIn)
    const [loading, setLoading] = useState(!loggedIn)
    const [isLoggedIn, setIsLoggedIn] = useState(loggedIn) 
    
    useEffect(async ()=> {
        if (!isLoggedIn){

            if (validUser){
                setLoading(false)
                setIsLoggedIn(true)
                localStorage.setItem('loggedIn', validUser)  
            }

            if (!validUser){
                var key = localStorage.getItem('key')
                var token = key === 'null' || key === 'undefined' ? false : key
                
                if (!token){
                    setLoading(false)
                }
                if (token){
                    const checkEndpoint = '/api/accounts/check-user/'
                    const data = {'token': token}

                    var result = await djangoFetch({urlEndpoint:checkEndpoint, urlMethod: 'POST', sendData:data, 
                        response_function: (response, status_code) => {
                            if (status_code === 200 && response.valid_user === 'true'){
                                localStorage.setItem('userType', response.user_type)
                                return true
                            }
                        }})            
                    setValidUser(result)
                }

            }
    }else {
        if (validUser){
            setLoading(true)
            djangoFetch({urlEndpoint: '/api/accounts/user-type/', urlMethod: 'GET', sendData: null,
                response_function: (response, status_code) => {
                    if (status_code === 200){
                        localStorage.setItem('userType', response.user_type)
                        setLoading(false)
                    }
                }
            })
            }
    }
        
    }, [validUser])

    if (!loading){
    return (
        <AuthContext.Provider value = {[isLoggedIn, setIsLoggedIn]}>
            {children}
        </AuthContext.Provider>
    )}else{
        return null 
    }
}

export function authContext(){
    return useContext(AuthContext)
}
