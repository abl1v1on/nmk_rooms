import './App.css'
import { Routes, Route } from 'react-router-dom';

// components
import Header from "./components/Header.jsx";
import Footer from "./components/Footer.jsx";

// pages
import MainPage from "./pages/MainPage.jsx";
import PageNotFound from "./pages/PageNotFound.jsx";


export default function App() {
  return (
    <>
        <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="*" element={<PageNotFound />} />
        </Routes>
        <Header />
        <Footer />
    </>
  )
}
