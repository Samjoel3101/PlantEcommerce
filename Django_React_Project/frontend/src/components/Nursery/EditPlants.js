import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom' 
import {Row, Col, Image} from 'react-bootstrap' 

import { djangoFetch } from '../djangoUtils/djangoFetch'

export function PlantDetail(props){
    const id = props.id
    const baseEndpoint = props.baseEndpoint 
    const userType = localStorage.getItem('userType')
    
    const [plantDetail, setPlantDetail] = useState(null)
    
    useEffect(() => {
        if (plantDetail === null){
        djangoFetch({urlEndpoint:`/${baseEndpoint}/${id}/`, sendData:null, urlMethod: 'GET',
                    response_function: (response, status_code) => {
                        if (status_code === 200){
                            setPlantDetail(response)
                        }else{
                            console.log(response)
                        }
                    }, stringify: false})
        }
    }, [plantDetail])
    
    if (plantDetail !== null){
        // console.log(plantDetail)
        return (
            <div>
                <Row> 
                    <Col xs = {6} md = {4} style = {{width: '15rem'}}>
                        <Image src = {plantDetail.image} thumbnail/>
                    </Col>
                    <Col>
                        <h1>Plant Name: {plantDetail.name}</h1>
                        <h3>Price: {plantDetail.price}</h3>
                        {userType === 'user' ? 
                            <div>
                                <h3>Seller: {plantDetail.nursery.owner.username}</h3>
                                <h3>Units Ordered: {plantDetail.units_ordered} </h3>
                            </div>: 
                            null}     
                    </Col>
                </Row>
                
            </div>
        )
    }else {
        return null
    }
}

export default function EditPlants() {
    const { id } = useParams()
    const endpoint = 'api/nursery/plant/detail' 
    return PlantDetail({id: id, baseEndpoint: endpoint})    
}
