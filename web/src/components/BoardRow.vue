<template>
    <div class="row" :class="rowClasses" :id="rowId">
        <div class="row-points-container">{{ rowScore }}</div>
        <div class="commander-horn-container"></div>

        <div class="cards-in-play-container">
            <card v-for="card in cards" :card="card" :key="card.id" :in-play="true"></card>
        </div>
    </div>
</template>

<style lang="scss">
    .row {
        height: 120px;
        width: 1018px;
        position: absolute;
        top: 0;
        left: 0;
        text-align: center;
    }

    .row > div {
        position: absolute;
        text-align: center;
    }

    .computer-board .row-1,
    .player-board .row-1 {
        top: 0;
    }

    .computer-board .row-2,
    .player-board .row-2 {
        top: 131px;
    }

    .computer-board .row-3,
    .player-board .row-3 {
        top: 269px;
    }

    .row-points-container {
        height: 40px;
        width: 40px;
        top: 38px;
        left: 16px;
        border-radius: 20px;
    }

    .commander-horn-container {
        height: 120px;
        width: 120px;
        top: 0;
        left: 77px;
    }

    .cards-in-play-container {
        height: 120px;
        width: 805px;
        top: 0;
        left: 210px;
    }

    .cards-in-play-container.drop-hover {
        background: rgba(255,255,255,0.4);
    }

    .player-board .row-1 .row-points-container {
        top: 36px;
    }
</style>

<script>
    import Card from './Card';

    export default {
        props: ['rowFor', 'rowIndex', 'rowType'],
        data() {
            return {};
        },
        components: {
            Card
        },
        computed: {
            game() {
                return this.$store.getters.game;
            },
            cards() {
                if (this.game && this.game.hasOwnProperty('round')) {
                    const currRound = this.game.round;
                    const playerIndex = this.rowFor === 'player' ? 0 : 1;

                    return this.game.rounds[currRound].cards[playerIndex][this.rowIndex - 1]
                } else {
                    return []
                }
            },
            rowClasses() {
                return 'row-' + this.rowType + ' row-' + this.rowIndex + ' ' + this.rowFor + '-row-' + this.rowIndex;
            },
            rowId() {
                return this.rowFor + '-row-' + this.rowIndex;
            },
            rowScore() {
                const currRound = this.game.round;
                if (this.game && this.game.hasOwnProperty('rounds') && this.game.rounds[currRound].scores.hasOwnProperty('rows')) {

                    const playerIndex = this.rowFor === 'player' ? 0 : 1;

                    return this.game.rounds[currRound].scores.rows[playerIndex][this.rowIndex - 1];
                } else {
                    return []
                }
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>