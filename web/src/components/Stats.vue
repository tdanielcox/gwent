<template>
    <div class="stats" :class="statsClass">
        <div class="card-count-container">{{ cardsLeft }}</div>
        <div class="loss-indicators-container">
            <div class="loss-indicator loss-indicator-1" :class="lost1Classes"></div>
            <div class="loss-indicator loss-indicator-2" :class="lost2Classes"></div>
        </div>
        <div class="passed-container" v-if="roundPassed"><h2>Passed</h2></div>
        <div class="total-points-container">{{ roundScore }}</div>
        <div class="turn-indicator" :class="{ active: currentPlayer === statsForIndex }"></div>
    </div>
</template>

<style lang="scss">
    .stats {
        width: 275px;
        height: 92px;
        position: absolute;
        top: 288px;
        left: 145px;
    }

    .stats .card-count-container {
        width: 38px;
        height: 40px;
        top: 47px;
        left: 36px;
        position: absolute;
        text-align: center;
        color: #A59365;
        font-size: 2.8rem;
        line-height: 40px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }

    .stats .loss-indicator {
        width: 43px;
        height: 44px;
        top: 45px;
        left: 83px;
        position: absolute;
        text-align: center;

        &.not-lost {
            background: url("../assets/img/jewel-filled.png") no-repeat center center;
        }
    }

    .stats .turn-indicator {
        width: 108px;
        height: 80px;
        top: -4px;
        left: 164px;
        position: absolute;

        &.active {
            background: url("../assets/img/turn-indicator.png") no-repeat center center;
        }
    }

    .stats .loss-indicator-2 {
        left: 126px;
    }

    .stats .total-points-container {
        height: 40px;
        width: 40px;
        top: 8px;
        left: 198px;
        border-radius: 20px;
        position: absolute;
        text-align: center;
        line-height: 40px;
        font-size: 2.8rem;
        font-weight: bold;
        text-shadow: -1px -1px 0 rgba(255,255,255,0.6),
            1px -1px 0 rgba(255,255,255,0.6),
            -1px 1px 0 rgba(255,255,255,0.6),
            1px 1px 0 rgba(255,255,255,0.6);
    }

    .stats .passed-container {
        position: absolute;
        left: 80px;
        top: -34px;
        width: 274px;
        height: 28px;
        background: -moz-radial-gradient(center, ellipse cover, rgba(99,78,52,1) 0%, rgba(249,248,247,0) 76%, rgba(255,255,255,0) 79%);
        background: -webkit-radial-gradient(center, ellipse cover, rgba(99,78,52,1) 0%,rgba(249,248,247,0) 76%,rgba(255,255,255,0) 79%);
        background: radial-gradient(ellipse at center, rgba(99,78,52,1) 0%,rgba(249,248,247,0) 76%,rgba(255,255,255,0) 79%);
        filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#634e34', endColorstr='#00ffffff',GradientType=1 );

        h2 {
            font-size: 2.2rem;
            color: #BCA07A;
            text-align: center;
            line-height: 28px;
            text-shadow: -1px -1px 0 rgba(0,0,0,0.6),
                1px -1px 0 rgba(0,0,0,0.6),
                -1px 1px 0 rgba(0,0,0,0.6),
                1px 1px 0 rgba(0,0,0,0.6);
        }
    }

    .player-stats {
        height: 112px;
        top: 249px;
    }

    .player-stats .card-count-container {
        top: 7px;
    }

    .player-stats .loss-indicator {
        top: 2px;
    }

    .player-stats .total-points-container {
        top: 30px;
    }

    .player-stats .turn-indicator {
        top: 18px;
    }

    .player-stats .passed-container {
        top: -13px;
    }
</style>

<script>
    import GameService from '../services/GameService.js';

    export default {
        props: ['statsFor'],
        computed: {
            game() {
                return this.$store.getters.game;
            },
            currentRound() {
                return this.$store.getters.currentRound;
            },
            currentPlayer() {
                return this.$store.getters.currentPlayer;
            },
            statsForIndex() {
                return this.statsFor === 'player' ? 0 : 1;
            },
            statsClass() {
                return this.statsFor + '-stats';
            },
            roundScore() {
                if (this.game) {
                    return this.game.rounds[this.currentRound].scores.totals[this.playerIndex];
                } else {
                    return 0;
                }
            },
            playerIndex() {
                return this.statsFor === 'player' ? 0 : 1;
            },
            cardsLeft() {
                if (this.game) {
                    const rows = this.game.players[this.playerIndex].cards;
                    let cardCount = 0;

                    rows.forEach(row => {
                        cardCount += row.length;
                    });

                    return cardCount;
                }

                return 0;
            },
            losses() {
                if (this.game) {
                    return this.game.players[this.playerIndex].losses;
                }

                return false;
            },
            lost1Classes() {
                return {
                    'not-lost': this.losses ? !this.losses[0] : true
                }
            },
            lost2Classes() {
                return {
                    'not-lost': this.losses ? !this.losses[1] : true
                }
            },
            roundPassed() {
                return this.game ? this.game.players[this.playerIndex].passed[this.currentRound] : 0;
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>