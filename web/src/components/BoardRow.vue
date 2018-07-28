<template>
    <div class="row" :class="rowClasses">
        <div class="row-points-container"></div>
        <div class="commander-horn-container"></div>

        <div class="cards-in-play-container">
        </div>
    </div>
</template>

<style lang="scss">
    .row {
        height: 120px;
        width: 940px;
        position: absolute;
        top: 0;
        left: 0;
        text-align: center;
    }

    .row > div {
        position: absolute;
        text-align: center;
    }

    .computer-board .row-1,
    .player-board .row-1 {
        top: 0;
    }

    .computer-board .row-2,
    .player-board .row-2 {
        top: 131px;
    }

    .computer-board .row-3,
    .player-board .row-3 {
        top: 269px;
    }

    .row-points-container {
        height: 40px;
        width: 40px;
        top: 38px;
        left: 16px;
        border-radius: 20px;
    }

    .commander-horn-container {
        height: 120px;
        width: 120px;
        top: 0;
        left: 77px;
    }

    .cards-in-play-container {
        height: 120px;
        width: 805px;
        top: 0;
        left: 210px;
    }

    .cards-in-play-container.drop-hover {
        background: rgba(255,255,255,0.4);
    }

    .player-board .row-1 .row-points-container {
        top: 36px;
    }
</style>

<script>
    import GameService from '../services/GameService.js';

    export default {
        props: ['rowIndex', 'rowType'],
        data() {
            return {};
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

        },
        mounted() {
            let game = GameService.getGame();
            this.$store.dispatch('setGame', game);
        }
    }
</script>