<template>
    <div class="card"></div>
</template>

<script>
    import GameService from '../services/GameService.js';

    export default {
        props: ['token'],
        computed: {
            game() {
                return this.$store.getters.game;
            }
        },
        methods: {
            formatMoney(amount) {
                return UtilityService.formatMoney(amount);
            },
            goToCheckout() {
                let url = process.env.MIX_ADISTRY_URL + 'redirect/checkout/' + this.token;

                window.parent.postMessage(['publistry_scrollToTopIframe', 1], '*');

                this.$root.redirectModalLink = url;
                this.$root.showRedirectModal = true;
            }
        },
        mounted() {
            let game = GameService.getGame();
            this.$store.dispatch('setGame', game);
        }
    }
</script>