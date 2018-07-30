<template>
    <div class="container">
        hi ho bo
        <div class="computer-container">
            <stats :stats-for="'computer'"></stats>

            <div class="board computer-board">
                <board-row :row-index="1" :row-type="'seige'" :row-for="'computer'"></board-row>
                <board-row :row-index="2" :row-type="'ranged'" :row-for="'computer'"></board-row>
                <board-row :row-index="3" :row-type="'melee'" :row-for="'computer'"></board-row>
            </div>

            <graveyard :graveyard-for="'computer'"></graveyard>
        </div>

        <div class="player-container">
            <stats :stats-for="'player'"></stats>

            <div class="board player-board">
                <board-row :row-index="1" :row-type="'melee'" :row-for="'player'"></board-row>
                <board-row :row-index="2" :row-type="'ranged'" :row-for="'player'"></board-row>
                <board-row :row-index="3" :row-type="'seige'" :row-for="'player'"></board-row>
            </div>

            <graveyard :graveyard-for="'player'"></graveyard>
            <hand></hand>
        </div>
    </div>
</template>

<style lang="scss">
    .container {
        width: 100%;
        height: 100vh;
        background: url("../../images/background.jpg") top left no-repeat;
        position: relative;
        overflow: hidden;
    }

    .row {
        width: 50%;
        height: 100vh;
        float: left;
    }
</style>

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
            // let game = GameService.getGame();
            // this.$store.dispatch('setGame', game);
        }
    }
</script>
