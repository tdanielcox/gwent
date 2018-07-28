const state = {
    game: {}
};

const getters = {
    game: state => {
        return state.game;
    }
};

const mutations = {
    SET_GAME(state, game) {
        state.game = game;
    }
};

const actions = {
    setGame(context, game) {
        context.commit('SET_GAME', game);
    }
};

const GameState = {
    state,
    getters,
    mutations,    actions
};

export default GameState;
