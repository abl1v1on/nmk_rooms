import './App.css'
import { Routes, Route } from 'react-router-dom';

import Header from "./components/Header.jsx";
import MainPage from "./pages/MainPage.jsx";


export default function App() {
  return (
    <>
        <Routes>
            <Route path="/" element={<MainPage />} />
        </Routes>
        <Header/>
    </>
  )
}
