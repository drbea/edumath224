import React from 'react';
import HelloWorld from '../helloWorld';

function Home() {

    return (
        <div className="container">
            <div className="row">
                <div className="col">
                    <h1 className="mt-4">Acceuil</h1>
                </div>
            </div>
            <div className="row">
                <div className="col">
                    <p> Ceci est la page d'accueil.</p>
                </div>
                <HelloWorld />
            </div>
        </div>
    );
}

export default Home;