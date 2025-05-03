import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

import config from "../config.js";
import Loader from "../components/Loader.jsx";


export default function HallDetailsPage() {
    const { id } = useParams();
    const [hall, setHall] = useState({});
    const [isLoading, setIsLoading] = useState(true);

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
                                <input className="input" type="date" id="booking-date" />
                            </div>
                        </div>


                        <div className="field">
                            <label className="label">Доступные слоты на 15.05.2023</label>
                            <div className="time-slots">
                                <div className="time-slot">09:00-10:00</div>
                                <div className="time-slot booked">10:00-11:00</div>
                                <div className="time-slot">11:00-12:00</div>
                                <div className="time-slot selected">12:00-13:00</div>
                                <div className="time-slot">13:00-14:00</div>
                                <div className="time-slot">14:00-15:00</div>
                                <div className="time-slot booked">15:00-16:00</div>
                                <div className="time-slot">16:00-17:00</div>
                                <div className="time-slot">17:00-18:00</div>
                            </div>
                        </div>

                        <div className="field">
                            <label className="label">Цель бронирования</label>
                            <div className="control">
                                <textarea className="textarea" placeholder="Опишите цель использования зала (совещание, презентация и т.д.)"></textarea>
                            </div>
                        </div>

                        <div className="field">
                            <label className="label">Дополнительное оборудование</label>
                            <div className="equipment-checkboxes">
                                <label className="checkbox">
                                    <input type="checkbox" />
                                    Ноутбук
                                </label>
                                <label className="checkbox">
                                    <input type="checkbox" />
                                    Дополнительный микрофон
                                </label>
                                <label className="checkbox">
                                    <input type="checkbox" />
                                    Видеокамера
                                </label>
                                <label className="checkbox">
                                    <input type="checkbox" />
                                    Док-станция
                                </label>
                                <label className="checkbox">
                                    <input type="checkbox" />
                                    Флипчарт (дополнительный)
                                </label>
                                <label className="checkbox">
                                    <input type="checkbox" />
                                    Внешние колонки
                                </label>
                            </div>
                        </div>

                        <div className="field">
                            <div className="control">
                                <button className="button is-primary is-fullwidth is-medium">
                                    <span className="icon">
                                        <i className="fas fa-calendar-check"></i>
                                    </span>
                                    <span>Забронировать</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div className="box mt-5">
                        <h3 className="title is-5">График занятости</h3>
                        <div className="content">
                            <p>Зал занят в следующие периоды:</p>
                            <ul>
                                <li>15.05.2023: 10:00-11:00</li>
                                <li>15.05.2023: 15:00-16:00</li>
                                <li>16.05.2023: 14:00-17:00</li>
                            </ul>
                        </div>
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
