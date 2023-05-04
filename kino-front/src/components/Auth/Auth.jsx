import React, {useState} from 'react';
import s from './Auth.module.scss';

const Auth = () => {

    let [login, setLogin] = useState("");
    let [password, setPassword] = useState("");

    let handleSubmit = () => {

    };

    return (
        <form className={s.auth}>
            <input type="text" placeholder={"login"} onChange={(e) => {setLogin(e.currentTarget.value)}}/>
            <input type="password" placeholder={"password"} onChange={(e) => {setPassword(e.currentTarget.value)}}/>
            <button>auth</button>
        </form>
    );
};

export default Auth;