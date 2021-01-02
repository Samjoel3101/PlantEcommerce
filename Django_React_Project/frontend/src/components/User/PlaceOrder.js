import React from 'react'
import {useParams} from 'react-router-dom'
import {Button} from 'react-bootstrap'
import {useHistory} from 'react-router-dom'

import {PlantDetail} from '../Nursery/EditPlants' 
import {djangoFetch} from '../djangoUtils/djangoFetch'

export default function PlaceOrder() {
    const {plantId} = useParams()
    const history = useHistory() 
    const baseEndpoint = 'api/user/plant-detail'

    const buyPlant = (e) => {
        e.preventDefault()
        djangoFetch({urlEndpoint: '/api/user/place-order/', urlMethod: 'POST', 
                    sendData: {plant: plantId}, 
                    response_function: (response, status_code) => {
                        if (status_code === 201){
                            alert('Order Placed')
                            history.push('/user/feed')                        
                        }
                    }, stringify: true 
                })

    }

    return (
        <div>
            <PlantDetail id = {plantId} baseEndpoint = {baseEndpoint}/>
            <Button variant = 'primary' onClick = {buyPlant}>
                Place Order 
            </Button> 
        </div>   
    )
}
