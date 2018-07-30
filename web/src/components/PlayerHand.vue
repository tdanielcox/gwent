<template>
    <div class="player-hand">
        <card v-for="card in playerHand" :card="card" :key="card.id"></card>
    </div>
</template>

<style lang="scss">
    .player-hand {
        background: rgba(0,0,0,0.6);
        height: 120px;
        width: 937px;
        position: absolute;
        top: 410px;
        left: 487px;
        text-align: center;
    }

    .player-hand .card {
        vertical-align: top;
    }

    .player-hand.drop-hover {
        background: rgba(255,255,255,0.4);
    }
</style>

<script>
    import Card from './Card';

    export default {
        props: [],
        components: {
            Card
        },
        computed: {
            playerHand() {
                return this.$store.getters.playerHand;
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>