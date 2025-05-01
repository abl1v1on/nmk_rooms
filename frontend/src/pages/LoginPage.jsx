export default function LoginPage() {
    return (
        <div className="auth-container">
            <div className="auth-card">
                <div className="auth-header">
                    <div className="auth-logo">
                        <i className="fas fa-building"></i>
                    </div>
                    <h1 className="title is-4 has-text-white">НефтеМодульКомплект</h1>
                    <p className="subtitle is-6 has-text-white">Корпоративная система бронирования</p>
                </div>

                <div className="auth-body">
                    <h2 className="auth-title title is-3 has-text-centered">Вход в систему</h2>

                    <form id="loginForm">
                        <div className="field">
                            <label className="label">Корпоративная почта</label>
                            <div className="control has-icons-left">
                                <input className="input input-auth" type="email" placeholder="user@nmk.ru" required/>
                                <span className="icon is-small is-left">
                                <i className="fas fa-envelope"></i>
                            </span>
                            </div>
                        </div>

                        <div className="field">
                            <label className="label">Пароль</label>
                            <div className="control has-icons-left">
                                <input className="input input-auth" type="password" placeholder="••••••••" required/>
                                <span className="icon is-small is-left">
                                <i className="fas fa-lock"></i>
                            </span>
                            </div>
                        </div>

                        <div className="field mt-5">
                            <div className="control">
                                <button className="button is-primary is-fullwidth button-auth" type="submit">
                                <span className="icon">
                                    <i className="fas fa-sign-in-alt"></i>
                                </span>
                                    <span>Войти</span>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}
