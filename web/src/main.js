import Vue from 'vue'
import Vuex from 'vuex'
import store from './vuex/store.js';

Vue.config.productionTip = false;
Vue.use(Vuex);

import Board from './components/Board.vue';

const app = new Vue({
    el: '#app',
    store,
    data: {
        
    },
    watch: {

    },
    render: h => h(Board)
});
