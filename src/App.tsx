import { useState } from 'react'
import './App.scss'
import LoginPage from "./Pages/Login/LoginPage.tsx";
import Main from "./Pages/MainPage/Main.tsx";


function App() {

    // function setIsLogged(isLogged: boolean) {
    //     isLogged = true;
    // }

    return(
        isLogged ? <Main/> : <LoginPage/>
    )
}

export default App
