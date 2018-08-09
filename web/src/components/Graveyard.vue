<template>
    <div class="graveyard" :class="graveyardClass" v-if="card">
        <card :card="card" :key="card.id" :in-graveyard="true"></card>
    </div>
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
    import Card from './Card';

    export default {
        props: ['graveyardFor'],
        components: {
            Card
        },
        computed: {
            game() {
                return this.$store.getters.game;
            },
            graveyardClass() {
                return this.graveyardFor + '-graveyard';
            },
            card() {
                if (!this.game) return [];

                if (this.graveyardFor === 'player') {
                    return this.game.players[0].graveyard[0] || null;
                } else {
                    return this.game.players[1].graveyard[0] || null;
                }
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>