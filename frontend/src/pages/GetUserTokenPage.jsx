import axios from "axios";
import {useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import { Navigate } from "react-router-dom";

import config from "../config.js";
import Loader from "../components/Loader.jsx";


export default function GetUserTokenPage() {
    const { token } = useParams();
    const [redirect, setRedirect] = useState(false);

    useEffect(() => {
        const fetchUserId = async () => {
            try {
                const response = await axios.get(
                    `${config.baseUrl}/users/by-token/${token}`
                )
                const userId = response.data.user_id;
                localStorage.setItem("userId", userId);
                setRedirect(true);
            } catch (error) {
                console.log(error);
                alert("Error");
            }
        }

        fetchUserId();
    }, [token]);

    if (redirect) {
        return <Navigate to="/" />
    }

    return <Loader />
}
