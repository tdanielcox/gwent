const state = {
    gameId: '',
    game: {},
    playerHand: [],
    focusedCardId: ''
};

const getters = {
    gameId: state => {
        return state.gameId;
    },
    game: state => {
        return state.game;
    },
    playerHand: state => {
        return state.playerHand;
    },
    focusedCardId: state => {
        return state.focusedCardId;
    }
};

const mutations = {
    SET_GAME_ID(state, gameId) {
        state.gameId = gameId;
    },
    SET_GAME(state, game) {
        state.game = game;
    },
    SET_PLAYER_HAND(state, playerHand) {
        state.playerHand = playerHand;
    },
    SET_FOCUSED_CARD_ID(state, cardId) {
        state.focusedCardId = cardId;
    }
};

const actions = {
    setGameId(context, gameId) {
        context.commit('SET_GAME_ID', gameId);
    },
    setGame(context, game) {
        context.commit('SET_GAME', game);
    },
    setPlayerHand(context, playerHand) {
        context.commit('SET_PLAYER_HAND', playerHand);
    },
    setFocusedCardId(context, cardId) {
        context.commit('SET_FOCUSED_CARD_ID', cardId);
    }
};

const GameState = {
    state,
    getters,
    mutations,
    actions
};

export default GameState;
