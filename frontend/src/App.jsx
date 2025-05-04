import './App.css'
import { Routes, Route } from 'react-router-dom';
import { ToastContainer } from "react-toastify";

// components
import Header from "./components/Header.jsx";
import Footer from "./components/Footer.jsx";

// pages
import MainPage from "./pages/MainPage.jsx";
import HallListPage from "./pages/HallListPage.jsx";
import HallDetailsPage from "./pages/HallDetailsPage.jsx";
import MyBookingsPage from "./pages/MyBookingsPage.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import PageNotFound from "./pages/PageNotFound.jsx";


export default function App() {
  return (
    <>
        <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/halls" element={<HallListPage />} />
            <Route path="/halls/:id" element={<HallDetailsPage />} />
            <Route path="/my-bookings" element={<MyBookingsPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="*" element={<PageNotFound />} />
        </Routes>
        <Header />
        <Footer />
        <ToastContainer />
    </>
  )
}
