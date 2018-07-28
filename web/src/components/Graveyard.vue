<template>
    <div class="graveyard" :class="graveyardClass"></div>
</template>

<style lang="scss">
    .graveyard {
        position: absolute;
        top: 55px;
        left: 1454px;
        width: 110px;
        height: 144px;
    }

    .player-container .graveyard {
        top: 393px;
    }
</style>

<script>
    // import GameService from '../services/GameService.js';

    export default {
        props: ['token'],
        computed: {
            game() {
                return this.$store.getters.game;
            },
            graveyardClass() {
                return this.graveyardFor + '-graveyard';
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>