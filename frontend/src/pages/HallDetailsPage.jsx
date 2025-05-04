import axios from "axios";
import { toast } from "react-toastify";
import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

import config from "../config.js";
import Loader from "../components/Loader.jsx";


export default function HallDetailsPage() {
    const { id } = useParams();
    const [hall, setHall] = useState({});
    const [isLoading, setIsLoading] = useState(true);
    const [selectedBookingDate, setSelectedBookingDate] = useState(null);
    const [availableSlots, setAvailableSlots] = useState([]);
    const [selectedSlot, setSelectedSlot] = useState(null);

    const navigate = useNavigate();

    useEffect(() => {
        const handleHall = async () => {
            try {
                const response = await axios.get(
                    `${config.baseUrl}/rooms/${id}`
                );
                console.log(response.data)
                setHall(response.data);
            } catch (error) {
                alert("Error");
                console.log(error);
            } finally {
                setIsLoading(false);
            }
        }

        handleHall();
    }, [id]);

    const handleChangeBookingDate = async (e) => {
        const bookingDate = e.target.value;
        setSelectedBookingDate(bookingDate);

        try {
            const response = await axios.get(
                `${config.baseUrl}/bookings/busy?room_id=${hall.id}&booking_date=${bookingDate}`,
            )
            setAvailableSlots(response.data);
        } catch (error) {
            console.log(error);
            alert('Error');
        }
    }

    const handleClickToSlot = (index) => {
        setSelectedSlot(index);
    }

    const bookHall = async () => {
        try {
            const data = {
                room_id: hall.id,
                user_id: 1, // TODO: после добавления авторизации изменить user_id
                booking_date: selectedBookingDate,
                booking_time: selectedSlot
            };
            const response = await axios.post(
                `${config.baseUrl}/bookings`, data
            );

            if (response.status === 200) {
                toast.success("Вы успешно забронировали зал");
                navigate("/my-bookings");
            }
        } catch (error) {
            console.log(error);
            toast.error("При попытке бронирования произошла ошибка");
        }
    }

    const renderPage = () => {
        if (isLoading) {
            return <Loader />;
        }
        return (
            <div className="columns">
                <div className="column is-7">
                    <div className="hall-header">
                        <h1 className="title is-2">Конференц-зал №{hall.number}</h1>
                        <p className="subtitle is-5 has-text-grey">{hall.location.address}</p>

                        <div className="tags are-medium mt-3">
                            <span className="tag is-primary">Вместимость: {hall.capacity} чел.</span>
                            <span className="tag is-success">Доступен</span>
                        </div>
                    </div>

                    <div className="hall-gallery">
                        <div className="hall-main-image">
                            <img src={hall.image ? hall.image : `no-image.webp`} alt="зал" className="image" />
                        </div>
                    </div>

                    <div className="content">
                        <h3 className="title is-4">Описание</h3>
                        <p>{hall.description}.</p>

                        <h3 className="title is-4 mt-5">Оснащение</h3>
                        <ul className="hall-features-list">
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Проектор</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Экран 120"</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Конференц-система</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Wi-Fi</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Флипчарт</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Микрофоны (2 шт.)</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Кондиционер</li>
                            <li><span className="icon has-text-primary"><i className="fas fa-check"></i></span> Кофе-машина</li>
                        </ul>
                    </div>
                </div>

                <div className="column is-5">
                    <div className="booking-form-box">
                        <h2 className="title is-3 booking-form-title">Бронирование</h2>

                        <div className="field">
                            <label className="label">Дата бронирования</label>
                            <div className="control">
                                <input onChange={handleChangeBookingDate} className="input" type="date" id="booking-date" />
                            </div>
                        </div>

                        {selectedBookingDate && (
                        <div className="field">
                            <label className="label">Доступные слоты на {selectedBookingDate}</label>
                            <div className="time-slots">
                                {availableSlots.map((slot, index) => (
                                    <div
                                        onClick={() => handleClickToSlot(slot)}
                                        className={`time-slot ${selectedSlot === slot ? 'selected' : ''}`}>
                                        {slot}
                                    </div>
                                ))}
                                {availableSlots.length === 0 && (
                                    <div style={{color: "red"}}>На {selectedBookingDate} нет доступных слотов</div>
                                )}
                            </div>
                        </div>
                        )}

                        {/*<div className="field">*/}
                        {/*    <label className="label">Цель бронирования</label>*/}
                        {/*    <div className="control">*/}
                        {/*        <textarea className="textarea" placeholder="Опишите цель использования зала (совещание, презентация и т.д.)"></textarea>*/}
                        {/*    </div>*/}
                        {/*</div>*/}

                        {selectedSlot && (
                        <div className="field">
                            <div className="control">
                                <button onClick={bookHall} className="button is-primary is-fullwidth is-medium">
                                    <span className="icon">
                                        <i className="fas fa-calendar-check"></i>
                                    </span>
                                    <span>Забронировать</span>
                                </button>
                            </div>
                        </div>
                        )}
                    </div>
                </div>
            </div>
        )
    }

    return (
        <>
        <section className="section hall-booking-section">
            <div className="container">
                <nav className="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">
                    <ul>
                        <li><a href="/">Главная</a></li>
                        <li><a href="/halls">Все залы</a></li>
                        <li className="is-active"><a href="#" aria-current="page">Конференц-зал</a></li>
                    </ul>
                </nav>
                {renderPage()}
            </div>
        </section>
        </>
    )
}
