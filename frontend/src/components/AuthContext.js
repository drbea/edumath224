import React, { createContext, useState, useContext, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Vérifiez si l'utilisateur est déjà connecté
        const storedUser = localStorage.getItem('username');
        if (storedUser) {
            setUser({ username: storedUser });
        }
    }, []);

    const login = (username) => {
        localStorage.setItem('username', username);
        setUser({ username });
    };

    const logout = () => {
        localStorage.removeItem('username');
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);
