import { Link } from "react-router-dom";

export default function PageNotFound() {
    return (
        <section className="hero is-fullheight nmk-404">
            <div className="hero-body">
                <div className="container has-text-centered">
                    <div className="columns is-centered">
                        <div className="column is-8">
                            <h1 className="title nmk-404-title has-text-white has-text-weight-bold mb-2">404</h1>
                            <h2 className="subtitle is-3 has-text-white has-text-weight-semibold mb-5">
                                Страница не найдена
                            </h2>
                            <p className="has-text-white mb-5">
                                Запрашиваемая страница не существует или была перемещена.<br/>
                                Пожалуйста, проверьте URL или вернитесь на главную.
                            </p>
                            <div className="buttons is-centered">
                                <Link href="" className="button is-primary is-medium" to="/">
                                    <span className="icon">
                                        <i className="fas fa-home"></i>
                                    </span>
                                    <span>На главную</span>
                                </Link>
                                <a href="" className="button is-white is-outlined is-medium">
                                    <span className="icon">
                                        <i className="fas fa-search"></i>
                                    </span>
                                    <span>Найти зал</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}
