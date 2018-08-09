<template>
    <div class="card-selector" :class="selectorClass">

        <div class="inner">
            <h2>Choose a card to revive</h2>

            <div class="cards">
                <card v-for="card in cards" :card="card" :key="card.id" :in-selector="true"></card>
            </div>
        </div>

    </div>
</template>

<style lang="scss">
    .card-selector {
        position: absolute;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.8);
        z-index: 210;
        font-size: 30px;
        color: #FFF;
        text-align: center;
        opacity: 0;
        transition: opacity 0.4s linear;
        display: none;

        &.visible {
            opacity: 1;
            display: block;
        }

        .inner {
            position: relative;
            top: 50%;
            transform: translateY(-50%);

            h2 {
                color: #FFF;
            }

            .cards {
                margin-top: 40px;
            }
        }
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
            game() {
                return this.$store.getters.game;
            },
            type() {
                return this.$store.getters.cardSelectorType;
            },
            showSelector() {
                return this.$store.getters.cardSelectorVisible;
            },
            cards() {
                return this.$store.getters.cardSelectorCards;
            },
            selectorClass() {
                return {
                    forMedic: this.type === 'medic',
                    forDecoy: this.type === 'decoy',
                    visible: this.showSelector
                }
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>