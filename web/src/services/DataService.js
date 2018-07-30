import axios from "axios";

const API_URL = 'http://127.0.0.1:5000';

const GameService = {

    startGame() {
        return axios.post(API_URL + '/start-game', {});
    },

    playCard(gameId, cardId) {
        return axios.post(API_URL + '/play-card?game_id=' + gameId, { card_id: cardId });
    }


};

export default GameService;
