<template>
    <board></board>
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

    export default {
        props: [],
        components: {
            Board
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
