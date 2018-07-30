import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

import GameState from './modules/GameState.js'

const store = new Vuex.Store({
    modules: {
        GameState,
    }
});

export default store;