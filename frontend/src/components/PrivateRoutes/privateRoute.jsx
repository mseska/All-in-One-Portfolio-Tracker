import { Outlet, Navigate } from 'react-router-dom'

const PrivateRoutes = () => {
    const isAuthenticated = localStorage.getItem('userToken') ? true : false;
    return(
        isAuthenticated ?  <Outlet/> : <Navigate to="/"/>
    )
}

export default PrivateRoutes