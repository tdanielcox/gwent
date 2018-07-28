<template>
    <div class="stats" :class="statsClass">
        <div class="card-count-container"></div>
        <div class="loss-indicators-container">
            <div class="loss-indicator loss-indicator-1 not-lost"></div>
            <div class="loss-indicator loss-indicator-2 not-lost"></div>
        </div>
        <div class="total-points-container"></div>
    </div>
</template>

<style lang="scss">
    .stats {
        width: 248px;
        height: 92px;
        position: absolute;
        top: 288px;
        left: 145px;
    }

    .stats .card-count-container {
        width: 38px;
        height: 40px;
        top: 47px;
        left: 36px;
        position: absolute;
        text-align: center;
    }

    .stats .loss-indicator {
        width: 43px;
        height: 44px;
        top: 45px;
        left: 83px;
        position: absolute;
        text-align: center;
    }

    .stats .loss-indicator.not-lost {
        background: url("../assets/img/jewel-filled.png") no-repeat center center;
    }

    .stats .loss-indicator-2 {
        left: 126px;
    }

    .stats .total-points-container {
        height: 40px;
        width: 40px;
        top: 8px;
        left: 198px;
        border-radius: 20px;
        position: absolute;
        text-align: center;
    }

    .player-stats {
        height: 112px;
        top: 249px;
    }

    .player-stats .card-count-container {
        top: 7px;
    }

    .player-stats .loss-indicator {
        top: 2px;
    }

    .player-stats .total-points-container {
        top: 30px;
    }
</style>

<script>
    import GameService from '../services/GameService.js';

    export default {
        props: ['token', 'statsFor'],
        computed: {
            game() {
                return this.$store.getters.game;
            },
            statsClass() {
                return this.statsFor + '-stats';
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>