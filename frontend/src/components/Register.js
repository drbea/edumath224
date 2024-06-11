import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Register() {
    const [formData, setFormData] = useState({
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        password2: ''
    });
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate(); 

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/register/', formData)
            .then(response => {
                setMessage(response.data.message);
                setError('');
                setTimeout(() => {
                    navigate('/login');
                }, 3000); // Redirige après 3 secondes
            })
            .catch(error => {
                if (error.response && error.response.data) {
                    setError(error.response.data.error);
                } else {
                    setError('An error occurred. Please try again.');
                }
                setMessage('');
            });
    };

    return (
        <div>
            <h2>Inscription</h2>
            {message && <div className="alert alert-success">{message}</div>}
            {error && <div className="alert alert-danger">{error}</div>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nom d'utilisateur:</label>
                    <input type="text" name="username" value={formData.username} onChange={handleChange} required />
                </div>
                <div>
                    <label>Prénom:</label>
                    <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Nom:</label>
                    <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Adresse e-mail:</label>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <div>
                    <label>Mot de passe:</label>
                    <input type="password" name="password" value={formData.password} onChange={handleChange} required />
                </div>
                <div>
                    <label>Confirmer le mot de passe:</label>
                    <input type="password" name="password2" value={formData.password2} onChange={handleChange} required />
                </div>
                <button type="submit">S'inscrire</button>
            </form>
        </div>
    );
}

export default Register;
