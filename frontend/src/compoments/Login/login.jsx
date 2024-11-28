/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState } from "react";
import './login.css';
import { FaUser, FaLock, FaEnvelope } from "react-icons/fa";

const Login = () =>{

    const [action, setAction] = useState('');

    const registerLink = ()=>{
        setAction(' active');
    };

    const loginLink = ()=>{
        setAction('')
    };

    return (
        <div className={`wapper${action}`}>
            <div className="form-box login">
                <form action="">
                    <h1>LogIn</h1>
                    <div className="iput-box">
                        <input type="text" placeholder="Username" required/>
                        <FaUser className="icon" />
                    </div>
                    <div className="iput-box">
                        <input type="password" placeholder="Password" required/>
                        <FaLock className="icon" />
                    </div>
                    <button type="submit">Login</button>
                    <div className="register-link">
                        <p>Don't have an account? <a href="#" onClick={registerLink}>Register</a></p>
                    </div>
                </form>
            </div>

            <div className="form-box registration">
                <form action="">
                    <h1>Registration</h1>
                    <div className="iput-box">
                        <input type="text" placeholder="Username" required/>
                        <FaUser className="icon" />
                    </div>
                    <div className="iput-box">
                        <input type="email" placeholder="Email" required/>
                        <FaEnvelope className="icon" />
                    </div>
                    <div className="iput-box">
                        <input type="password" placeholder="Password" required/>
                        <FaLock className="icon" />
                    </div>
                    <button type="submit">Register</button>
                    <div className="register-link">
                        <p>Already have an account? <a href="#" onClick={loginLink}>Login</a></p>
                    </div>
                </form>
            </div>
        </div>
    );
};
export default Login