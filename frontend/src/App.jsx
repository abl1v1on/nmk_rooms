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
import {useEffect, useState} from "react";
import axios from "axios";
import config from "./config.js";


export default function App() {
    const [userId, setUserId] = useState(null);
    const [isTWA, setIsTWA] = useState(true);

    useEffect(() => {
        const fetchUserId = async () => {
            const tg = window.Telegram.WebApp;
            tg.ready();

            if (typeof window.Telegram.WebApp.initDataUnsafe?.user?.id === "undefined") {
              setIsTWA(false);
            }

            const initData = tg.initData;
            const initDataUnsafe = tg.initDataUnsafe;

            const response = await axios.get(
                `${config.baseUrl}/users/token?tg_id=${initDataUnsafe.user.id}`
            );
            setUserId(response.data.user_id);
        }

        fetchUserId();
    }, []);

    // if (!isTWA) {
    //     return <div
    //         style={{textAlign: "center", fontSize: "24px"}}>
    //         ⚠️ Доступ только через Telegram
    //     </div>;
    // }

  return (
    <>
        <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/halls" element={<HallListPage />} />
            <Route path="/halls/:id" element={<HallDetailsPage userId={userId}/>} />
            <Route path="/my-bookings" element={<MyBookingsPage userId={userId}/>} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="*" element={<PageNotFound />} />
        </Routes>
        <Header />
        <Footer />
        <ToastContainer />
    </>
  )
}
