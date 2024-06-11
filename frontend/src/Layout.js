// src/Layout.js
import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';  // Assurez-vous d'avoir un fichier CSS personnalisé
import { useAuth } from './components/AuthContext';    // Importez useAuth pour accéder au contexte


function Layout({ children }) {
    const { user, logout } = useAuth();   // Utilisez user pour obtenir les informations de l'utilisateur
    return (
        <div>
            <header>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <a className="navbar-brand" href="#">Edumath224</a>
                    
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ml-auto">
                            <li className="nav-item active">
                                <Link className="nav-link" to="/">Accueil <span className="sr-only">(current)</span></Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/cours">Cours</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/about"  >À propos</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/contact">Contact</Link>
                            </li>

                            {user ? (
                        <>
                            <li className="nav-item">
                                <span className="nav-link">Bonjour, {user.username}</span>
                            </li>
                            <li className="nav-item">
                                <button className="nav-link btn" onClick={logout}>Déconnexion</button>
                            </li>
                        </>
                    ) : (
                        <>
                            <li className="nav-item">
                                <Link className="nav-link" to="/login">Connexion</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/register">Inscription</Link>
                            </li>
                        </>
                    )}


                        </ul>
                    </div>
                </nav>
            </header>

            <main role="main" className="container">
                {children}
            </main>

            <footer className="footer bg-light py-3">
                <div className="container">
                    <span className="text-muted">&copy; 2024 Mon Site. Tous droits réservés.</span>
                    <ul className="list-inline">
                        <li className="list-inline-item"><a href="#">Politique de confidentialité</a></li>
                        <li className="list-inline-item"><a href="#">Termes et conditions</a></li>
                        <li className="list-inline-item"><a href="#">Contact</a></li>
                    </ul>
                </div>
            </footer>
        </div>
    );
}

export default Layout;
