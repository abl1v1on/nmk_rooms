import { useState } from "react";
import { Link } from "react-router-dom";


export default function Header() {
    const [isActive, setIsActive] = useState(false);

    const toggleBurger = () => setIsActive(!isActive);
    const handleLinkClick = () => setIsActive(false);

    return (
        <nav className="navbar is-dark is-fixed-top" role="navigation" aria-label="main navigation">
            <div className="container">
                <div className="navbar-brand">
                    <Link className="navbar-item" to="/" onClick={handleLinkClick}>
                        <h1 className="title is-5 has-text-white">НМК Конференц-залы</h1>
                    </Link>
                    <a
                        role="button"
                        className={`navbar-burger ${isActive ? "is-active" : ""}`}
                        aria-label="menu"
                        aria-expanded={isActive ? "true" : "false"}
                        onClick={toggleBurger}
                    >
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                        <span aria-hidden="true"></span>
                    </a>
                </div>

                <div className={`navbar-menu ${isActive ? "is-active" : ""}`}>
                    <div className="navbar-end">
                        <Link className="navbar-item is-active" to="/halls" onClick={handleLinkClick}>Все залы</Link>
                        <Link className="navbar-item" to="/my-bookings" onClick={handleLinkClick}>Мои бронирования</Link>
                        <div className="navbar-item">
                            <div className="buttons">
                                <Link className="button is-primary" to="/login" onClick={handleLinkClick}>Войти</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    );
}
