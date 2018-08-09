import axios from "axios";

const API_URL = 'http://127.0.0.1:5000';

const GameService = {

    startGame() {
        return axios.post(API_URL + '/start-game', {});
    },

    playCard(gameId, cardId) {
        return axios.post(API_URL + '/play-card?game_id=' + gameId, { card_id: cardId });
    },

    reviveCard(gameId, cardId) {
        return axios.post(API_URL + '/revive-card?game_id=' + gameId, { card_id: cardId });
    },

    passRound(gameId) {
        return axios.post(API_URL + '/pass-round?game_id=' + gameId, {});
    },

    aiTurn(gameId) {
        return axios.get(API_URL + '/ai-turn?game_id=' + gameId);
    }


};

export default GameService;
