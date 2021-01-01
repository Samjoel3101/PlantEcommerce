import React, {useRef} from 'react'
import {Form, Button} from 'react-bootstrap' 
import {useHistory} from 'react-router-dom'

import {formGroup} from '../utils/formUtils'
import useForm from '../Hooks/useForm' 
import axios from 'axios'
import {cookie} from '../Cookie' 

export default function addPlants() {
    const userType = localStorage.getItem('userType')
    const formValues = {name: '', price: ''}
    const imageRef = useRef()

    const history = useHistory() 
    const [inputValues, inputChange] = useForm(formValues)
    const createEndpoint = '/api/nursery/plant/create/'

    const submitHandler = (e) =>{
        e.preventDefault() 

        var data = new FormData() 
        data.append('image', imageRef.current.files[0])
        data.append('name', inputValues.name)
        data.append('price', inputValues.price)
        
        axios.post(createEndpoint, data, 
            {headers: {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
            'X-CSRFToken': cookie.get('csrftoken')}})    
        .then(res => {
            if (res.status == 201){
                alert('Plant Created Successfully')
                history.push('/nursery')
            }
        })
    }
     
    if (userType === 'nursery_admin'){
    return (
        <div>
            <Form onSubmit = {submitHandler} encType = 'multipart/form-data'>

                <Form.Group>
                    <Form.File ref = {imageRef} label = "Plant's image"/>
                </Form.Group>

                {formGroup('text', 'name', 'Plant Name', inputValues.name, inputChange, null)}
                {formGroup('number', 'price', 'Price', inputValues.price, inputChange, null)}

                <Button variant = 'primary' type = 'submit'>
                    Add Plant
                </Button>

            </Form>           
        </div>
    )}else{
        return null 
    }

}
