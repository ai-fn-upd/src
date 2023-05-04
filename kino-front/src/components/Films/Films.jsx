import React, {useEffect, useState} from 'react';
import s from './Films.module.scss';
import Film from "./components/Film/Film";
import {API} from "../../api/api";

const Films = ({setFilm}) => {

    let [films, setFilms] = useState([]);

    let getFilms = async () => {
        let data = await API.getFilms();
        console.log(data);
        setFilms(data.movies);
    };

    useEffect(() => {
        getFilms();
    }, []);

    return (
        <div className={s.films}>
            {films.map((f) => <Film title={f.title} image={f.preview} likes={f.likes.length} key={f.id} onClick={() => {
                setFilm(f.id);
            }}/>)}
        </div>
    );
};

export default Films;