import Vue from 'vue'
import Vuex from 'vuex'
import store from './vuex/store.js';

Vue.use(Vuex);

// Vue.component('doughnut-chart', require('../../../../resources/assets/js/components/DoughnutChart.vue'));
// Vue.component('modal', require('../../../../resources/assets/js/components/Modal.vue'));
// Vue.component('sidebar-cart', require('./components/sidebar-cart/SidebarCart.vue'));
// Vue.component('profile-cart', require('./components/profile-cart/ProfileCart.vue'));
// Vue.component('add-to-cart-button', require('./components/add-to-cart-button/AddToCartButton.vue'));
// Vue.component('redirect-modal', require('./components/redirect-modal/RedirectModal.vue'));
// Vue.component('item-conversion-block', require('./components/item-conversion-block/ItemConversionBlock.vue'));
// Vue.component('lead-form-modal', require('./components/lead-form-modal/LeadFormModal.vue'));
// Vue.component('conversion-submitted-notice', require('./components/conversion-submitted-button/ConversionSubmittedNotice.vue'));

const app = new Vue({
    el: '#app',
    store,
    data: {
        
    },
    watch: {

    }
});