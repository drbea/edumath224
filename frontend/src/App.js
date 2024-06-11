// import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Layout from './Layout';
import About from './components/About';
import HelloWorld from './helloWorld';
import Home from './components/Home';
import Register from './components/Register';
import Login from './components/Login';
import Course from './components/Course';
import { AuthProvider } from './components/AuthContext';
function App() {
  return (
  <Router>
    <AuthProvider>

      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cours" element={<Course />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/about" element={<About />} />
          <Route path="/helloWorld" element={<HelloWorld />} />
        </Routes>
      </Layout>
      </AuthProvider>
  </Router>
    // <div className="App">
    //   <HelloWorld />
    // </div>
  );
}

export default App;
