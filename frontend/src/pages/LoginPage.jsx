import * as yup from 'yup';
import axios from "axios";
import { useForm } from "react-hook-form";
import { useState } from "react";
import { yupResolver } from '@hookform/resolvers/yup';

import config from "../config.js";


export default function LoginPage() {
    const [formErrors, setFormErrors] = useState(null);

    const schema = yup.object().shape({
      email: yup.string().email('Некорректный email').required('Email обязателен'),
      password: yup.string().min(8, 'Минимум 8 символов').required('Пароль обязателен'),
    });

    const { register, handleSubmit, formState: { errors } } = useForm({
        resolver: yupResolver(schema),
    });

    const onSubmit = async (data) => {
        setFormErrors(null);

        try {
            const response = await axios.post(
                `${config.baseUrl}/auth/login`, data
            );
            alert(response.data.token);
        } catch (error) {
            setFormErrors("Неправильный логин или пароль");
        }
    };

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

                    <form id="loginForm" method="post" onSubmit={handleSubmit(onSubmit)}>
                        {formErrors && (
                            <p style={{color: "red"}} className="mb-5">{formErrors}</p>
                        )}
                        <div className="field">
                            <label className="label">Корпоративная почта</label>
                            <div className="control has-icons-left">
                                <input {...register('email')} className="input input-auth" type="email" placeholder="user@nmk.ru" required/>
                                {errors.email && <p style={{ color: 'red' }}>{errors.email.message}</p>}
                                <span className="icon is-small is-left">
                                <i className="fas fa-envelope"></i>
                            </span>
                            </div>
                        </div>

                        <div className="field">
                            <label className="label">Пароль</label>
                            <div className="control has-icons-left">
                                <input {...register('password')} className="input input-auth" type="password" placeholder="••••••••" required/>
                                {errors.password && <p style={{ color: 'red' }}>{errors.password.message}</p>}
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
