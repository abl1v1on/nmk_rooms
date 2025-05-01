import { Link } from "react-router-dom";


export default function Header() {
    return (
        <nav className="navbar is-dark is-fixed-top" role="navigation" aria-label="main navigation">
            <div className="container">
                <div className="navbar-brand">
                    <Link className="navbar-item" to="/">
                        <h1 className="title is-5 has-text-white">НМК Конференц-залы</h1>
                    </Link>
                    <a role="button" className="navbar-burger" aria-label="menu" aria-expanded="false">
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                    </a>
                </div>
                <div className="navbar-menu">
                    <div className="navbar-end">
                        <Link className="navbar-item is-active" to="/halls">Все залы</Link>
                        <a className="navbar-item" href="#">Мои бронирования</a>
                        <div className="navbar-item">
                            <div className="buttons">
                                <Link className="button is-primary" to="/login">Войти</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    )
}
