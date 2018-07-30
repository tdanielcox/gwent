import Vue from 'vue'
import Vuex from 'vuex'
import store from './vuex/store.js';

Vue.config.productionTip = false;
Vue.use(Vuex);

import Game from './components/Game.vue';

new Vue({
    el: '#app',
    store,
    data: {
        
    },
    watch: {

    },
    render: h => h(Game)
});
