import axios from "axios";
import { toast } from "react-toastify";
import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import config from "../config.js";
import SingleBooking from "../components/SingleBooking.jsx";
import Loader from "../components/Loader.jsx";


export default function MyBookingsPage({ userId }) {
    const [bookings, setBookings] = useState([]);
    const [initialBookings, setInitialBookings] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [selectedBookingStatus, setSelectedBookingStatus] = useState("all");

    useEffect(() => {
        const fetchBookings = async () => {
            try {
                const response = await axios.get(
                    `${config.baseUrl}/bookings/user-bookings?user_id=1`
                );
                setBookings(response.data);
                setInitialBookings(response.data);
            } catch (error) {
                console.log(error);
                alert("Error");
            } finally {
                setIsLoading(false);
            }
        };

        fetchBookings();
    }, []);

    const handleDeleteBooking = async (id) => {
        try {
            const response = await axios.delete(
                `${config.baseUrl}/bookings/${id}`
            );
            toast.success("Бронирование отменено");
            setBookings(bookings.filter((booking) => booking.id !== id));
        } catch (error) {
            console.log(error);
            alert("Error");
        }
    };

    const getBookingDateObject = (bookingDate) => {
        return new Date(bookingDate).setHours(
            0, 0, 0, 0
        );
    }

    const filterBookingsByStatus = (status) => {
        if (status === selectedBookingStatus) return;

        setSelectedBookingStatus(status);
        const currentDate = new Date().setHours(0, 0, 0, 0);        

        if (status === "all") {
            setBookings(initialBookings);
        } else if (status === "complete") {
            setBookings(initialBookings.filter(booking => {
                return getBookingDateObject(booking.booking_date) < currentDate;
            }));
        } else if (status === 'upcoming') {
            setBookings(initialBookings.filter(booking => {
                return getBookingDateObject(booking.booking_date) >= currentDate;
            }));
        }
    }

    const renderBookings = () => {
        if (bookings.length > 0) {
            return (
                <div className="bookings-list">
                    {bookings.map((booking) => (
                        <SingleBooking
                            booking={booking}
                            handleDeleteBooking={handleDeleteBooking}
                        />
                    ))}
                </div>
            )
        } else {
            return (
                <div className="no-bookings">
                    <span className="icon is-large has-text-grey-light mb-4">
                        <i className="fas fa-calendar-times fa-3x"></i>
                    </span>
                    <h3 className="title is-4 has-text-grey">Нет активных бронирований</h3>
                    <p className="subtitle is-6 has-text-grey">У вас пока нет предстоящих бронирований конференц-залов</p>
                    <Link to="/halls" className="button is-primary mt-3">
                        <span className="icon">
                            <i className="fas fa-plus"></i>
                        </span>
                        <span>Забронировать зал</span>
                    </Link>
                </div>
            )
        }
    }

    return (
    <section className="section">
        <div className="container">
            <nav className="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">
                <ul>
                    <li><a href="/">Главная</a></li>
                    <li className="is-active"><a href="#" aria-current="page">Мои бронирования</a></li>
                </ul>
            </nav>

            <div className="columns is-vcentered mb-5">
                <div className="column">
                    <h1 className="title is-2">Мои бронирования</h1>
                </div>
                <div className="column is-narrow">
                    <Link to="/halls" className="button is-primary">
                        <span className="icon">
                            <i className="fas fa-plus"></i>
                        </span>
                        <span>Новое бронирование</span>
                    </Link>
                </div>
            </div>

            <div className="filter-tabs">
                <div className="tabs is-boxed">
                    <ul>
                        <li onClick={() => filterBookingsByStatus("all")} className={selectedBookingStatus === "all" ? "is-active" : ""} value="all"><a>Все</a></li>
                        <li onClick={() => filterBookingsByStatus("upcoming")} className={selectedBookingStatus === "upcoming" ? "is-active" : ""} value="upcoming"><a>Предстоящие</a></li>
                        <li onClick={() => filterBookingsByStatus("complete")} className={selectedBookingStatus === "complete" ? "is-active" : ""} value="complete"><a>Завершенные</a></li>
                    </ul>
                </div>
            </div>

            {isLoading ? <Loader /> : renderBookings()}
        </div>
    </section>
    );
}
