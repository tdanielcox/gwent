<template>
    <div class="game">
        <board></board>
        <notification></notification>
        <card-selector></card-selector>
        <copyright></copyright>
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
    import CardSelector from './CardSelector';
    import Copyright from './Copyright';

    export default {
        props: [],
        components: {
            Board,
            Notification,
            CardSelector,
            Copyright
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
        }
    }
</script>
