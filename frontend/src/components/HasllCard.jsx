export default function HallCard() {
    return (
        <div className="column is-one-third">
            <div className="card hall-card">
                <div className="card-image">
                    <figure className="image is-4by3">
                        <img src="" alt="Зал 'Нефтяник'" />
                    </figure>
                    <div className="card-badge">
                        <span className="tag is-primary">Корпус А</span>
                    </div>
                </div>
                <div className="card-content">
                    <div className="media">
                        <div className="media-content">
                            <p className="title is-4">Нефтяник</p>
                            <p className="subtitle is-6">3 этаж, каб. А-304</p>
                        </div>
                        <div className="media-right">
                            <span className="tag is-dark">20 чел.</span>
                        </div>
                    </div>

                    <div className="content">
                        <div className="hall-features mb-4">
                            <span className="icon-text">
                                <span className="icon has-text-primary">
                                    <i className="fas fa-tv"></i>
                                </span>
                                <span>Проектор</span>
                            </span>
                            <span className="icon-text ml-3">
                                <span className="icon has-text-primary">
                                    <i className="fas fa-microphone"></i>
                                </span>
                                <span>Аудио</span>
                            </span>
                        </div>
                        <div className="buttons">
                            <a href="" className="button is-primary is-outlined is-fullwidth">
                                <span>Подробнее</span>
                                <span className="icon">
                                    <i className="fas fa-arrow-right"></i>
                                </span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}