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

    @mixin stack-cards($max_count, $offset) {
        .player-hand .card:nth-last-child(n + #{$max_count}),
        .player-hand .card:nth-last-child(n + #{$max_count}) ~ * {
            margin-left: #{$offset};
        }
    }

    @include stack-cards(12, -20px);
    @include stack-cards(14, -30px);
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