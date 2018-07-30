<template>
    <div class="row row-melee row-1" v-bind:class="rowClasses">
        <div class="row-points-container"></div>
        <div class="commander-horn-container"></div>

        <div class="cards-in-play-container">
        </div>
    </div>
</template>

<script>
    import GameService from '../services/GameService.js';

    export default {
        props: ['rowIndex', 'rowType'],
        data: {
            
        },
        computed: {
            game() {
                return this.$store.getters.game;
            },
            rowClasses() {
                return 'row-' + this.rowType + ' row-' + this.rowIndex;
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