import logo from './logo.svg';
import './App.css';
import Films from "./components/Films/Films";
import {useState} from "react";
import Auth from "./components/Auth/Auth";
import Film from "./components/Film/Film";

function App() {

    let [film, setFilm] = useState(0);
    let [authData, setAuthData] = useState({});

    return (
        <div className="App">
            <div className={"container"}>
                <Auth/>
                {film == 0 ? <Films setFilm={setFilm}/> : <Film id={film} back={(e) => {setFilm(0);}}/>}
            </div>
        </div>
    );
}

export default App;
