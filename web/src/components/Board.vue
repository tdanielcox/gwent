<template>
    <div class="container">
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
            <pass-button></pass-button>

            <div class="board player-board">
                <board-row :row-index="1" :row-type="'melee'" :row-for="'player'"></board-row>
                <board-row :row-index="2" :row-type="'ranged'" :row-for="'player'"></board-row>
                <board-row :row-index="3" :row-type="'seige'" :row-for="'player'"></board-row>
            </div>

            <graveyard :graveyard-for="'player'"></graveyard>
            <player-hand></player-hand>
        </div>
    </div>
</template>

<style lang="scss">
    .container {
        width: 100%;
        height: 100vh;
        background: url("../assets/img/background.jpg") top left no-repeat;
        position: relative;
        overflow: hidden;
    }

    .computer-container,
    .player-container {
        height: 389px;
        width: 1570px;
        position: absolute;
        top: 16px;
        left: 90px;
    }

    .player-container {
        top: 435px;
        height: 550px;
    }

    .computer-board,
    .player-board {
        height: 389px;
        width: 1015px;
        position: absolute;
        top: 0;
        left: 410px;
    }
</style>

<script>    
    // import GameService from '../services/GameService.js';
    import BoardRow from './BoardRow';
    import Graveyard from './Graveyard';
    import Stats from './Stats';
    import PlayerHand from './PlayerHand';
    import PassButton from './PassButton';

    export default {
        props: [],
        components: {
            BoardRow,
            Stats,
            Graveyard,
            PlayerHand,
            PassButton
        },
        data() {
            return {

            }
        },
        computed: {
            game() {
                return this.$store.getters.game;
            },
        },
        methods: {

        },
        mounted() {

        }
    }
</script>
