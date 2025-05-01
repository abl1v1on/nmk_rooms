export default function HallDetailsPage() {
    return (
        <>
        <section className="section hall-booking-section">
            <div className="container">
                <nav className="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">
                    <ul>
                        <li><a href="/">Главная</a></li>
                        <li><a href="/halls">Все залы</a></li>
                        <li className="is-active"><a href="#" aria-current="page">Конференц-зал "Нефтяник"</a></li>
                    </ul>
                </nav>

                <div className="columns">
                    <div className="column is-7">
                        <div className="hall-header">
                            <h1 className="title is-2">Конференц-зал "Нефтяник"</h1>
                            <p className="subtitle is-5 has-text-grey">Корпус А, 3 этаж, каб. 301</p>

                            <div className="tags are-medium mt-3">
                                <span className="tag is-primary">Вместимость: 20 чел.</span>
                                <span className="tag is-info">Площадь: 45 м²</span>
                                <span className="tag is-success">Доступен</span>
                            </div>
                        </div>

                        <div className="hall-gallery">
                            <div className="hall-main-image">
                                <img src="" alt="Конференц-зал Нефтяник" className="image" />
                            </div>
                            <div className="hall-thumbnails">
                                <div className="hall-thumbnail active">
                                    <img src="" alt="Фото 1" className="image" />
                                </div>
                                <div className="hall-thumbnail">
                                    <img src="" alt="Фото 2" className="image" />
                                </div>
                                <div className="hall-thumbnail">
                                    <img src="" alt="Фото 3" className="image" />
                                </div>
                                <div className="hall-thumbnail">
                                    <img src="" alt="Фото 4" className="image" />
                                </div>
                            </div>
                        </div>

                        <div className="content">
                            <h3 className="title is-4">Описание</h3>
                            <p>Современный конференц-зал с панорамными окнами и профессиональным оборудованием. Идеально подходит для проведения презентаций, совещаний и тренингов.</p>

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

                            <h3 className="title is-4 mt-5">Правила бронирования</h3>
                            <ol>
                                <li>Максимальное время бронирования - 4 часа</li>
                                <li>Бронирование возможно не более чем за 30 дней</li>
                                <li>Отмена бронирования - не позднее чем за 2 часа</li>
                            </ol>
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

                            <div className="datetime-picker">
                                <div className="field is-expanded">
                                    <label className="label">Время начала</label>
                                    <div className="control">
                                        <div className="select is-fullwidth">
                                            <select id="start-time">
                                                <option value="">Выберите время</option>
                                                <option value="09:00">09:00</option>
                                                <option value="10:00">10:00</option>
                                                <option value="11:00">11:00</option>
                                                <option value="12:00">12:00</option>
                                                <option value="13:00">13:00</option>
                                                <option value="14:00">14:00</option>
                                                <option value="15:00">15:00</option>
                                                <option value="16:00">16:00</option>
                                                <option value="17:00">17:00</option>
                                                <option value="18:00">18:00</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>

                                <div className="field is-expanded">
                                    <label className="label">Время окончания</label>
                                    <div className="control">
                                        <div className="select is-fullwidth">
                                            <select id="end-time">
                                                <option value="">Выберите время</option>
                                                <option value="10:00">10:00</option>
                                                <option value="11:00">11:00</option>
                                                <option value="12:00">12:00</option>
                                                <option value="13:00">13:00</option>
                                                <option value="14:00">14:00</option>
                                                <option value="15:00">15:00</option>
                                                <option value="16:00">16:00</option>
                                                <option value="17:00">17:00</option>
                                                <option value="18:00">18:00</option>
                                                <option value="19:00">19:00</option>
                                            </select>
                                        </div>
                                    </div>
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
            </div>
        </section>
        </>
    )
}
