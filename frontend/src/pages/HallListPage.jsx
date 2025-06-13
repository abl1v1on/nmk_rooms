import axios from "axios";
import { useState, useEffect } from "react";

import config from "../config.js";
import Loader from "../components/Loader.jsx";
import HallCard from "../components/HasllCard.jsx";


export default function HallListPage() {
    const [halls, setHalls] = useState([]);
    const [initialHalls, setInitialHalls] = useState();
    const [isLoading, setIsLoading] = useState(true);
    const [search, setSearch] = useState("");

    useEffect(() => {
        const fetchHalls = async () => {
            try {
                const response = await axios.get(
                    `${config.baseUrl}/rooms`
                );
                setHalls(response.data);
                setInitialHalls(response.data);
            } catch (error) {
                alert('Error');
                console.log(error);
            } finally {
                setIsLoading(false);
            }
        }

        fetchHalls();
    }, []);

    const searchHalls = (e) => {
        e.preventDefault();
        if (search.trim().length > 0) {
            setHalls(
                initialHalls.filter(hall => String(hall.number).includes(search))
            );
        } else {
            setSearch("");
            setHalls(initialHalls);
        }
    };

    const renderHalls = () => {
        if (isLoading) {
            return <Loader />
        }

        return (
            <div className="columns is-multiline mt-1">
                {halls.length > 0 ? (
                    halls.map((hall) => (
                        <HallCard hall={hall} key={hall.id} />
                    ))
                ): (
                    <div className="no-bookings">
                        <span className="icon is-large has-text-grey-light mb-4">
                            <i className="fas fa-calendar-times fa-3x"></i>
                        </span>
                        <h3 className="title is-4 has-text-grey">
                            Мы не смогли найти залы по вашему запросу
                        </h3>
                    </div>
                )}
            </div>
        )

    }

    return (
        <>
        <section className="section pt-2 pb-2">
            <div className="container">
                <div className="box">
                    <form action="" method="get" onSubmit={searchHalls}>
                    <div className="columns is-vcentered">
                            <div className="column is-10">
                                <div className="field">
                                    <div className="control has-icons-left">
                                        <input onChange={(e) => setSearch(e.target.value)} className="input" type="text" placeholder="Поиск по названию..." value={search} />
                                        <span className="icon is-small is-left">
                                            <i className="fas fa-search"></i>
                                        </span>
                                    </div>
                                </div>
                            </div>

                            <div className="column is-2">
                                <button onClick={searchHalls} className="button is-primary is-fullwidth" id="apply-filters">
                                    <span className="icon">
                                        <i className="fas fa-filter"></i>
                                    </span>
                                    <span>Применить</span>
                                </button>
                            </div>
                    </div>
                    </form>
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
