<template>
    <div class="card"></div>
</template>

<style lang="scss">
    .card {
        width: 80px;
        height: 120px;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center center;
        display: inline-block;
    }

    .card.dragging {
        width: 130px;
        height: 200px;
    }

    .card.in-play {
        width: 80px;
        height: 120px;
        display: inline-block;
        margin: 0 2px;
    }
</style>

<script>
    // import GameService from '../services/GameService.js';

    export default {
        props: [],
        computed: {
            game() {
                return this.$store.getters.game;
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>