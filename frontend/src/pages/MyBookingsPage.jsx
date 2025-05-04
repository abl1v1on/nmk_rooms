export default function MyBookingsPage() {
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
                    <button className="button is-primary">
                        <span className="icon">
                            <i className="fas fa-plus"></i>
                        </span>
                        <span>Новое бронирование</span>
                    </button>
                </div>
            </div>

            <div className="filter-tabs">
                <div className="tabs is-boxed">
                    <ul>
                        <li className="is-active"><a>Все</a></li>
                        <li><a>Предстоящие</a></li>
                        <li><a>Завершенные</a></li>
                        <li><a>Отмененные</a></li>
                    </ul>
                </div>
            </div>

            <div className="bookings-list">
                <div className="booking-card">
                    <div className="booking-card-header">
                        <div className="columns is-vcentered is-mobile">
                            <div className="column">
                                <h3 className="title is-4 mb-0">Конференц-зал "Нефтяник"</h3>
                                <span className="booking-status status-confirmed">
                                    <span className="icon is-small">
                                        <i className="fas fa-check-circle"></i>
                                    </span>
                                    <span>Подтверждено</span>
                                </span>
                            </div>
                            <div className="column is-narrow">
                                <button className="button is-light is-danger cancel-btn">
                                    <span className="icon">
                                        <i className="fas fa-times"></i>
                                    </span>
                                    <span>Отменить</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="booking-card-body">
                        <div className="booking-details">
                            <div className="booking-detail">
                                <div className="detail-label">Дата и время</div>
                                <div className="detail-value">15 мая 2023, 14:00 - 16:00</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Местоположение</div>
                                <div className="detail-value">Корпус А, 3 этаж, каб. 301</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Цель</div>
                                <div className="detail-value">Совещание по проекту "Северный поток"</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Номер брони</div>
                                <div className="detail-value">NMK-20230515-142</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="booking-card">
                    <div className="booking-card-header">
                        <div className="columns is-vcentered is-mobile">
                            <div className="column">
                                <h3 className="title is-4 mb-0">Переговорная "Бурение"</h3>
                                <span className="booking-status status-confirmed">
                                    <span className="icon is-small">
                                        <i className="fas fa-check-circle"></i>
                                    </span>
                                    <span>Подтверждено</span>
                                </span>
                            </div>
                            <div className="column is-narrow">
                                <button className="button is-light is-danger cancel-btn">
                                    <span className="icon">
                                        <i className="fas fa-times"></i>
                                    </span>
                                    <span>Отменить</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="booking-card-body">
                        <div className="booking-details">
                            <div className="booking-detail">
                                <div className="detail-label">Дата и время</div>
                                <div className="detail-value">16 мая 2023, 09:00 - 11:00</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Местоположение</div>
                                <div className="detail-value">Корпус Б, 2 этаж, каб. 215</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Цель</div>
                                <div className="detail-value">Обсуждение ТЗ с заказчиком</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Номер брони</div>
                                <div className="detail-value">NMK-20230516-087</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="booking-card">
                    <div className="booking-card-header">
                        <div className="columns is-vcentered is-mobile">
                            <div className="column">
                                <h3 className="title is-4 mb-0">Зал заседаний</h3>
                                <span className="booking-status status-cancelled">
                                    <span className="icon is-small">
                                        <i className="fas fa-times-circle"></i>
                                    </span>
                                    <span>Отменено</span>
                                </span>
                            </div>
                            <div className="column is-narrow">
                                <button className="button is-light is-danger" disabled>
                                    <span className="icon">
                                        <i className="fas fa-times"></i>
                                    </span>
                                    <span>Отменить</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="booking-card-body">
                        <div className="booking-details">
                            <div className="booking-detail">
                                <div className="detail-label">Дата и время</div>
                                <div className="detail-value">10 мая 2023, 13:00 - 15:00</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Местоположение</div>
                                <div className="detail-value">Корпус В, 1 этаж, каб. 101</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Цель</div>
                                <div className="detail-value">Презентация годового отчета</div>
                            </div>
                            <div className="booking-detail">
                                <div className="detail-label">Номер брони</div>
                                <div className="detail-value">NMK-20230510-056</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/*<div className="no-bookings">*/}
            {/*    <span className="icon is-large has-text-grey-light mb-4">*/}
            {/*        <i className="fas fa-calendar-times fa-3x"></i>*/}
            {/*    </span>*/}
            {/*    <h3 className="title is-4 has-text-grey">Нет активных бронирований</h3>*/}
            {/*    <p className="subtitle is-6 has-text-grey">У вас пока нет предстоящих бронирований конференц-залов</p>*/}
            {/*    <button className="button is-primary mt-3">*/}
            {/*        <span className="icon">*/}
            {/*            <i className="fas fa-plus"></i>*/}
            {/*        </span>*/}
            {/*        <span>Забронировать зал</span>*/}
            {/*    </button>*/}
            {/*</div>*/}
        </div>
    </section>

    );
}
