<template>
    <div class="pass-button" v-if="!roundPassed">
        <button @click="passRound">Pass</button>
    </div>
</template>

<style lang="scss">
    .pass-button {
        position: absolute;
        top: 452px;
        left: 200px;
        width: 110px;
        height: 30px;
        line-height: 30px;
        text-align: center;

        button {
            font-size: 1.6rem;
        }
    }
</style>

<script>
    import GameService from '../services/GameService.js';

    export default {
        props: [],
        computed: {
            game() {
                return this.$store.getters.game;
            },
            currentRound() {
                return this.$store.getters.currentRound;
            },
            passClass() {
                return '';
            },
            roundPassed() {
                return this.game ? this.game.players[0].passed[this.currentRound] : 0;
            }
        },
        methods: {
            passRound() {
                GameService.passRound().then(response => {

                });
            }
        },
        mounted() {

        }
    }
</script>