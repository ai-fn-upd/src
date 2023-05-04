import React, {useEffect, useState} from 'react';
import s from './Film.module.scss';
import {API} from "../../api/api";

const Film = ({id, back}) => {

    let [filmData, setFilmData] = useState({});

    useEffect(() => {
        getFilm();
    }, []);

    let getFilm = async () => {
        let data = await API.getFilm(id);
        setFilmData(data);
    };

    return (
        <div className={s.film}>
            {filmData.id ? <><button onClick={back}>Назад</button>
                <img src={`http://127.0.0.1:8000${filmData.preview}`} alt=""/>
                <h1>{filmData.title}</h1>
                <span>Лайки: {filmData.likes.length}</span>
                <button>Поставить лайк</button></> : null}
        </div>
    );
};

export default Film;