import React, {useEffect, useState} from 'react'
import {Link} from 'react-router-dom'
import {Card, Button} from 'react-bootstrap' 

import {djangoFetch} from '../djangoUtils/djangoFetch' 

export default function homePage() {
    const dataEndpoint = '/api/nursery/plant/list/'
    const [plants, setPlants] = useState(null) 
    
    const userType = localStorage.getItem('userType')
    const buttonType = (plantId) => {
        if (userType == 'nursery_admin'){
            return (
            <Link to = {`/nursery/plant/edit/${plantId}`}>
                <Button variant = 'primary'>Edit</Button>
            </Link>)
        }else {
            return (
                <Link>
                    <Button>Buy</Button>
                </Link>
            )
        }
    }

    useEffect(()=> {
        if (plants === null){
        djangoFetch({urlEndpoint: dataEndpoint, urlMethod: 'GET', 
                    response_function: (response, status_code) => {
                        if (status_code === 200){
                            setPlants(response)
                        }else if (status_code === 303){
                            setPlants('empty')
                        }
                    }})
                }
    }, [plants])

    if (plants !== null && plants !== 'empty'){
    var plantComponents = plants.map((item) => {
        
        return (<Card key = {item.id} style = {{width: '18rem'}}>
            {console.log(item.image)}
            {item.image === null ? null: <Card.Img variant = 'top' src= {item.image}/>}
            <Card.Body>
                <Card.Title style = {{display: 'flex'}}>Plant Name: {item.name}</Card.Title>
                <Card.Text>
                    Price(in INR): {item.price}
                </Card.Text>
                {buttonType(item.id)}
            </Card.Body>
        </Card>)
    })
 
    return (
        <div>
            <Link to = '/nursery/plant/add'>Add Plant</Link>  
            {plantComponents}          
        </div>
    )
    }else if (plants === 'empty'){
        return (
            <div>
                <h1>Oops seems like you have no plants in your nursery.</h1>
                <Link to = '/nursery/plant/add'>Start adding plants</Link>
            </div>
        )
    }else {return null}
}
