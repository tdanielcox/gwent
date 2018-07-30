<template>
    <div class="game">
        <board></board>
        <notification></notification>
    </div>
</template>

<style lang="scss">
    @import '../assets/css/reset.css';

    body {
        margin: 0;
    }
</style>

<script>    
    import GameService from '../services/GameService.js';
    import Board from './Board';
    import Notification from './Notification';

    export default {
        props: [],
        components: {
            Board,
            Notification
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
            GameService.startGame();

            // console.log(this.game);
        }
    }
</script>
