import { Link } from "react-router-dom";


export default function HallCard({ hall }) {
    return (
        <div className="column is-one-third">
            <div className="card hall-card">
                <div className="card-image">
                    <figure className="image is-4by3">
                        <img src={hall.image ? hall.image : `no-image.webp`} alt={hall.number} />
                    </figure>
                    <div className="card-badge">
                        <span className="tag is-primary">{hall.location.address}</span>
                    </div>
                </div>
                <div className="card-content">
                    <div className="media">
                        <div className="media-content">
                            <p className="title is-4">Зал №{hall.number}</p>
                            <p className="subtitle is-6">{hall.location.address}</p>
                        </div>{}
                        <div className="media-right">
                            <span className="tag is-dark">{hall.capacity} чел.</span>
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
                            <Link to={`/halls/${hall.id}`} className="button is-primary is-outlined is-fullwidth">
                                <span>Подробнее</span>
                                <span className="icon">
                                    <i className="fas fa-arrow-right"></i>
                                </span>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
