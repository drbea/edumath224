// LoginComponent.js
import React, { useState } from 'react';
import axios from 'axios';
import { Redirect, Navigate } from 'react-router-dom';

function LoginComponent() {
    const [formData, setFormData] = useState({
        username: '',
        password: ''
    });

    const [redirect, setRedirect] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/login/', formData)
            .then(response => {
                console.log(response.data);
                // Rediriger l'utilisateur vers une autre page après la connexion réussie
                setRedirect(true);
            })
            .catch(error => {
                console.error(error);
            });
    };

    if (redirect) {
        return <Navigate to="/" />; // Rediriger vers la page d'accueil
    }

    return (
        <div>
            <h2>Connexion</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nom d'utilisateur:</label>
                    <input type="text" name="username" value={formData.username} onChange={handleChange} />
                </div>
                <div>
                    <label>Mot de passe:</label>
                    <input type="password" name="password" value={formData.password} onChange={handleChange} />
                </div>
                <button type="submit">Se connecter</button>
            </form>
        </div>
    );
}

export default LoginComponent;
