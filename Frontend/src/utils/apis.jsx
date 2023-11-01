import axios from "axios";
import { BACKEND_URL } from "../constant/variables"



const getAllMovies = async (adult) => {
    const url = `${BACKEND_URL}titles`;
    const res = await axios.get(`${url}?adult=${adult}`);
    return res;
}


const getAllAction = async (adult) => {
    const url = `${BACKEND_URL}titles/genres?gen_list=Action&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getAllPerson = async () => {
    const url = `${BACKEND_URL}allPeople/`;
    const res = await axios.get(url);
    return res;
}

const getMovieByTitle = async (name, adult) => {
    const url = `${BACKEND_URL}titles/name?sub_string=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieByDirector = async (name, adult) => {
    const url = `${BACKEND_URL}titles/director?director=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieByWriter = async (name, adult) => {
    const url = `${BACKEND_URL}titles/writer?writer=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieByPerson = async (name, adult) => {
    const url = `${BACKEND_URL}titles/person?name=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieByGenre = async (name, adult) => {
    const url = `${BACKEND_URL}titles/genres?gen_list=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieByRelYear = async (name, adult) => {
    const url = `${BACKEND_URL}titles/search?param=start_year&val=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieByRating = async (name, adult) => {
    const url = `${BACKEND_URL}titles/search?param=rating&val=${name}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getMovieActors = async (id) => {
    const url = `${BACKEND_URL}actors?tconst=${id}`;
    const res = await axios.get(url);
    return res;
}

const getMovieDirector = async (id) => {
    const url = `${BACKEND_URL}directors?tconst=${id}`;
    const res = await axios.get(url);
    return res;
}

const getMovieData = async (id) => {
    const url = `${BACKEND_URL}title/id?tconst=${id}`;
    const res = await axios.get(url);
    return res;
}

const getMovieOtherTitles = async (id) => {
    const url = `${BACKEND_URL}titles/other_names?tconst=${id}`;
    const res = await axios.get(url);
    return res;
}

const getPersonDetails = async (id) => {
    const url = `${BACKEND_URL}person/details?nconst=${id}`;
    const res = await axios.get(url);
    return res;
}

const getPersonAllMovies = async (id, adult) => {
    const url = `${BACKEND_URL}person/titles?nconst=${id}&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getAllShows = async (adult) => {
    const url = `${BACKEND_URL}titles/search?param=title_type&val=television&adult=${adult}`;
    const res = await axios.get(url);
    return res;
}

const getShowsByTitle = async (name, adult) => {
    const url = `${BACKEND_URL}title/tv_show/og_title?title=${name}&adult=${adult}`
    const res = await axios.get(url);
    return res;
}

const getShowsByRelYear = async (year, adult) => {
    const url = `${BACKEND_URL}title/tv_show/start_year?start_year=${year}&adult=${adult}`
    const res = await axios.get(url);
    return res;
}

const getShowsByEndYear = async (year, adult) => {
    const url = `${BACKEND_URL}title/tv_show/end_year?end_year=${year}&adult=${adult}`
    const res = await axios.get(url);
    return res;
}

const getAdvancedSearch = async (data, adult) => {
    const url = `${BACKEND_URL}titles/advSearch?adult=${adult}`;
    const res = await axios.post(url, JSON.stringify(data), {
        headers: {
            'Content-Type': 'application/json'
        }
    });
    return res;
}

const sendReview = async (data,url) => {
    const res = await axios.post(url,JSON.stringify(data),{
        headers:{
            'Content-Type':'application/json'
        }
    });
    return res;
}

const findPerson = async (name) => {
    const url = `${BACKEND_URL}person/findPerson?name=${name}`;
    const res = await axios.get(url);
    return res;
}

export {
    getAllMovies,
    getAllAction,
    getAllPerson,
    getMovieByDirector,
    getMovieByGenre,
    getMovieByPerson,
    getMovieByTitle,
    getMovieByWriter,
    getMovieByRelYear,
    getMovieByRating,
    getMovieActors,
    getMovieDirector,
    getMovieData,
    getMovieOtherTitles,
    getPersonDetails,
    getPersonAllMovies,
    getAllShows,
    getShowsByTitle,
    getShowsByEndYear,
    getShowsByRelYear,
    getAdvancedSearch,
    sendReview
}