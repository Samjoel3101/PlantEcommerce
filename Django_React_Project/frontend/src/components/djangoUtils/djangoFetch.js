import React, {useState} from 'react'
import {cookie} from '../Cookie' 

export async function djangoFetch({urlEndpoint, sendData, urlMethod = 'GET', 
                            csrf = true, response_function = null, 
                            contentType = 'application/json', stringify = true, auth = false}) {
    
    var status_code = null 
    const lookUpOptions = {
        method : urlMethod, 
        headers : {
            'Content-Type': contentType, 
        }, 
    }
    if (sendData !== null && stringify){
        lookUpOptions.body = JSON.stringify(sendData)
    }else if (sendData !== null && !stringify) {
        lookUpOptions.body = sendData
    }

    if (auth){
        lookUpOptions.headers['Authorisation'] = `Bearer ${localStorage.getItem(key)}`
    }

    if (csrf){
        lookUpOptions.headers['X-CSRFToken'] = cookie.get('csrftoken')
    }
    
    return await fetch(urlEndpoint, lookUpOptions).then(response => {
        status_code = response.status
        return response.json() 
    }).then(
        response =>  {
            var result = response_function(response, status_code)
            return result 
        }
    )
}
