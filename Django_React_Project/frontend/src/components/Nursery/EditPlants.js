import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom' 

import { djangoFetch } from '../djangoUtils/djangoFetch'

export default function EditPlants() {
    const { id } = useParams()     
    console.log(id)
    const [plantDetail, setPlantDetail] = useState(null)
    
    useEffect(() => {
        djangoFetch({urlEndpoint:`/api/nursery/plant/detail/${id}`, sendData:null, urlMethod: 'GET',
                    response_function: (response, status_code) => {
                        if (status_code === 200){
                            setPlantDetail(response)
                        }else{
                            console.log(response)
                        }
                    }, stringify: false})
    }, [plantDetail])
    if (plantDetail !== null){
        return (
            <div>
                {plantDetail.id}
            </div>
        )
    }else {
        return null
    }
}
