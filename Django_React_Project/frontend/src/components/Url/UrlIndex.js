// Keep the urls and its corresponding Components in this file 

const UrlComponents = {}; 

UrlComponents['/'] = require('../Home/HomePage').default;

// Login Routes 
UrlComponents['/login'] = require('../AuthComponents/UserLogin').default;

// Signup Routes 
UrlComponents['/signup'] = require('../AuthComponents/ToggleRegister').default;
UrlComponents['/nursery-admin-signup'] = require('../AuthComponents/NurseryAdminSignUp').default;
UrlComponents['/user-signup'] = require('../AuthComponents/UserSignUp').default;

// Logout Routes
UrlComponents['/logout'] = require('../AuthComponents/UserLogout').default; 

// Nursery Routes
UrlComponents['/nursery'] = require('../Nursery/NurseryHome').default; 
UrlComponents['/nursery/plant/add'] = require('../Nursery/AddPlants').default; 
UrlComponents['/nursery/plant/edit/:id'] = require('../Nursery/EditPlants').default;
export default UrlComponents; 