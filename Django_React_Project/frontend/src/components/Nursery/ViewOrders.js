import React, {useState, useEffect} from 'react'
import { Card, Button } from "react-bootstrap"
import {Link} from 'react-router-dom'

import {djangoFetch} from '../djangoUtils/djangoFetch'

export default function ViewOrders() {
    const [orders, setOrders] = useState(null)
    const endpoint = '/api/nursery/view-orders/'

    useEffect(() => {
        if (orders === null){
        djangoFetch({urlEndpoint: endpoint, sendData: null, urlMethod: 'GET', 
                    response_function: (response, status_code) => {
                        if (status_code === 200){
                            setOrders(response)
                        }else if (status_code === 303){
                            setOrders('empty')
                        }
                    }            
                })
            }
    }, [orders])
    
    if (orders !== null && orders !== 'empty') {
        const orderComponents = orders.map((item) => {
            return (<Card key = {item.id}>
                <Card.Body>
                    <Card.Title>Plant Name: {item.name}</Card.Title>
                    <Card.Text>
                        Price: {item.price}<br/>
                        Count: {item.order_count}
                    </Card.Text>
                </Card.Body>
            </Card>)
        })
        
    return (
        <div style = {{display: 'flex'}}>
            {orderComponents}
        </div>
    )
    }else if (orders === 'empty'){
        return (
            <div>
                <h1>Oops seems like you have no orders</h1>
                <Link to = '/user/feed'>
                    <Button>
                        Start Purchasing
                    </Button>
                </Link>
            </div>
        )
    }else {
        return null 
    }
}
