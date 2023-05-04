import axios from "axios";

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/'
});

export const API = {
    async auth(login, password) {
        let response = await instance.post('/auth', {login, password});
        return response.data;
    },
    async getFilms() {
        let response = await instance.get('movies/?format=json');
        return response.data;
    },
    async getFilm(id) {
        let response = await instance.get(`movies/${id}/?format=json`);
        return response.data;
    },
    async like(id) {
        let response = await instance.post(`/film/${id}/like`);
        return response.data;
    }
}