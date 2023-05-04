import React from 'react';
import s from './Film.module.scss';

const Film = ({id, title, image, likes, onClick}) => {

    let handleClick = (e) => {
        e.preventDefault();
        onClick();
    };

    return (
        <div className={s.film}>
            <img src={`${image}`} alt=""/>
            <a href="#" onClick={handleClick}>{title}</a>
            <span>Число лайков: {likes}</span>
            <button>Поставить лайк</button>
        </div>
    );
};

export default Film;