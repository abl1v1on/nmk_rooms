import axios from "axios";
import { useState, useEffect } from "react";

import config from "../config.js";
import Loader from "../components/Loader.jsx";
import HallCard from "../components/HasllCard.jsx";


export default function HallListPage() {
    const [halls, setHalls] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const fetchHalls = async () => {
            try {
                const response = await axios.get(
                    `${config.baseUrl}/rooms`
                );
                setHalls(response.data);
            } catch (error) {
                alert('Error');
                console.log(error);
            } finally {
                setIsLoading(false);
            }
        }

        fetchHalls();
    }, []);

    const renderHalls = () => {
        if (isLoading) {
            return <Loader />
        }

        return (
            <div className="columns is-multiline mt-1">
                {halls.map((hall) => (
                    <HallCard hall={hall} key={hall.id} />
                ))}
            </div>
        )
    }

    return (
        <>
        <section className="section pt-4 pb-2 mt-4">
            <div className="container">
                <nav className="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">
                    <ul>
                        <li><a href="">Главная</a></li>
                        <li className="is-active"><a href="#" aria-current="page">Все залы</a></li>
                    </ul>
                </nav>
            </div>
        </section>

        <section className="section pt-2 pb-2">
            <div className="container">
                <div className="box">
                    <div className="columns is-vcentered">
                        <div className="column is-4">
                            <div className="field">
                                <div className="control has-icons-left">
                                    <input className="input" type="text" placeholder="Поиск по названию..." />
                                    <span className="icon is-small is-left">
                                        <i className="fas fa-search"></i>
                                    </span>
                                </div>
                            </div>
                        </div>

                        <div className="column is-2">
                            <button className="button is-primary is-fullwidth" id="apply-filters">
                                <span className="icon">
                                    <i className="fas fa-filter"></i>
                                </span>
                                <span>Применить</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section className="section pt-2">
            <div className="container">
                {renderHalls()}
            </div>
        </section>
        </>
    )
}
