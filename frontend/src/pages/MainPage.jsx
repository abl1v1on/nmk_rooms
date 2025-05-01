export default function MainPage() {
    return (
        <>
        <section className="hero is-medium is-dark">
            <div className="hero-body">
                <div className="container has-text-centered">
                    <h1 className="title is-2 has-text-weight-bold mb-4">Корпоративная система бронирования</h1>
                    <p className="subtitle is-4">Удобное резервирование конференц-залов предприятия</p>
                    <a href="" className="button is-primary is-medium mt-3">
                        <span>Перейти к бронированию</span>
                        <span className="icon">
                            <i className="fas fa-arrow-right"></i>
                        </span>
                    </a>
                </div>
            </div>
        </section>

        <section className="section">
            <div className="container">
                <div className="columns is-centered">
                    <div className="column is-8 has-text-centered">
                        <h2 className="title is-3 mb-6">О системе</h2>
                        <p className="is-size-5 mb-5">
                            Сервис бронирования конференц-залов предприятия "НефтеМодульКомплект" предназначен для
                            удобного резервирования переговорных помещений сотрудниками компании.
                        </p>
                        <div className="box has-background-light">
                            <div className="columns is-vcentered">
                                <div className="column is-one-third">
                                    <span className="icon is-large has-text-primary">
                                        <i className="fas fa-calendar-alt fa-3x"></i>
                                    </span>
                                    <h3 className="title is-5 mt-2">Онлайн-бронирование</h3>
                                    <p>Круглосуточный доступ к системе</p>
                                </div>
                                <div className="column is-one-third">
                                    <span className="icon is-large has-text-primary">
                                        <i className="fas fa-bell fa-3x"></i>
                                    </span>
                                    <h3 className="title is-5 mt-2">Уведомления</h3>
                                    <p>Напоминания о бронировании</p>
                                </div>
                                <div className="column is-one-third">
                                    <span className="icon is-large has-text-primary">
                                        <i className="fas fa-chart-bar fa-3x"></i>
                                    </span>
                                    <h3 className="title is-5 mt-2">Статистика</h3>
                                    <p>Анализ использования залов</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section className="section has-background-light">
            <div className="container">
                <h2 className="title is-3 has-text-centered mb-6">Как забронировать зал</h2>

                <div className="columns is-centered">
                    <div className="column is-10">
                        <div className="steps">
                            <div className="step">
                                <div className="step-number">1</div>
                                <div className="step-content">
                                    <h3 className="title is-5">Авторизуйтесь</h3>
                                    <p>Войдите в систему с помощью корпоративного email и пароля</p>
                                </div>
                            </div>

                            <div className="step">
                                <div className="step-number">2</div>
                                <div className="step-content">
                                    <h3 className="title is-5">Выберите зал</h3>
                                    <p>Просмотрите доступные конференц-залы и их характеристики</p>
                                </div>
                            </div>

                            <div className="step">
                                <div className="step-number">3</div>
                                <div className="step-content">
                                    <h3 className="title is-5">Укажите дату и время</h3>
                                    <p>Выберите удобные дату и время из доступных слотов</p>
                                </div>
                            </div>

                            <div className="step">
                                <div className="step-number">4</div>
                                <div className="step-content">
                                    <h3 className="title is-5">Подтвердите бронь</h3>
                                    <p>Заполните форму бронирования и получите подтверждение</p>
                                </div>
                            </div>
                        </div>

                        <div className="has-text-centered mt-6">
                            <a href="" className="button is-primary is-medium">
                                <span>Начать бронирование</span>
                                <span className="icon">
                                    <i className="fas fa-arrow-right"></i>
                                </span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section className="section">
            <div className="container">
                <div className="columns is-centered">
                    <div className="column is-6 has-text-centered">
                        <h2 className="title is-3 mb-4">Техническая поддержка</h2>
                        <p className="mb-4">Если у вас возникли вопросы по работе системы, обратитесь в службу поддержки:</p>
                        <div className="buttons is-centered">
                            <a className="button is-black is-outlined">
                                <span className="icon">
                                    <i className="fas fa-phone"></i>
                                </span>
                                <span>Внутр. 1234</span>
                            </a>
                            <a className="button is-black is-outlined">
                                <span className="icon">
                                    <i className="fas fa-envelope"></i>
                                </span>
                                <span>support@nmk.ru</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
      </>
    )
}
