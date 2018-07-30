<template>
    <div class="card"
         :style="css"
         :id="cardId"
         :class="cardClasses"
         @click="focusCard">

        <div class="confirm-box">
            <div class="inner">
                <div class="card-details">
                    <h3>{{ cardName }}</h3>
                    <p v-if="cardStrength">Strength: {{ cardStrength }}</p>
                    <p v-if="cardAbility">Ability: {{ cardAbility }}</p>
                </div>

                <h2>Play this card?</h2>
                <button class="yes-button" @click="playCard">Yes</button>
                <button class="no-button">No</button>
            </div>
        </div>
    </div>
</template>

<style lang="scss">
    .card {
        width: 80px;
        height: 120px;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center center;
        display: inline-block;
        transition: transform 0.2s ease-out;
        position: relative;
        cursor: pointer;
        vertical-align: top;

        &.inBackground {
            opacity: 0.6;
        }

        &:hover {
            opacity: 1;
            transform: scale(1.2);
            z-index: 30;
        }

        &.selected {
            transform: scale(2.3);
            z-index: 31;

            .confirm-box {
                opacity: 1;
            }
        }

        &.inPlay {
            opacity: 1;
            transform: scale(1);
            cursor: default;

            &:hover {
                opacity: 1;
                transform: scale(1);
                z-index: 1;
            }
        }

        .confirm-box {
            opacity: 0;
            transition: opacity 0.5s ease-out;
            background: rgba(255,255,255,0.8);
            height: 100%;
            width: 100%;
            position: relative;

            .inner {
                position: relative;
                top: 50%;
                transform: translateY(-50%);
                padding: 1px 0.5rem;

                h2 {
                    font-size: 0.6rem;
                    margin-top: 1rem;
                    margin-bottom: 1rem;
                }

                button {
                    font-size: 0.8rem;
                }

                .card-details {
                    margin-top: 0.4rem;

                    h3 {
                        font-size: 0.8rem;
                    }

                    p {
                        font-size: 0.6rem;
                    }
                }
            }
        }
    }

    .card.dragging {
        width: 130px;
        height: 200px;
    }

    .card.in-play {
        width: 80px;
        height: 120px;
        display: inline-block;
        margin: 0 2px;
    }
</style>

<script>
    import GameService from '../services/GameService.js';

    const NAME = 0;
    const ROW = 1;
    const STRENGTH = 2;
    const ABILITY = 3;
    const IMAGE_PATH = 4;
    const ID = 5;
    const ACTUAL_STRENGTH = 6;

    const NONE = 0;
    const BOND = 1;
    const SPY = 2;
    const HERO = 3;
    const WEATHER = 6;

    export default {
        props: ['card', 'inPlay'],
        data() {
            return {
            }
        },
        computed: {
            currentFocusedCard() {
                return this.$store.getters.focusedCardId;
            },
            game() {
                return this.$store.getters.game;
            },
            cardClasses() {
                return {
                    selected: this.currentFocusedCard === this.card[ID],
                    inBackground: this.currentFocusedCard && this.currentFocusedCard !== this.card[ID],
                    inPlay: this.inPlay
                };
            },
            css() {
                return {
                    backgroundImage: 'url(' + this.getImgUrl() + ')',
                };
            },
            cardName() {
                return this.card[NAME];
            },
            cardStrength() {
                return this.card[STRENGTH];
            },
            cardId() {
                return this.card[ID];
            },
            cardAbility() {
                switch (this.card[ABILITY]) {
                    case 0:
                    case 6:
                        return false;
                    case 1:
                        return 'Bond';
                    case 2:
                        return 'Spy';
                    case 3:
                        return 'Hero';
                    case 4:
                        return '';
                    case 5:
                        return '';
                }
            },
            cardRow() {
                switch (this.card[ROW]) {
                    case 0:
                        return 'Melee';
                    case 1:
                        return 'Ranged';
                    case 2:
                        return 'Siege';
                    case 3:
                        return 'Special';
                }
            }
        },
        methods: {
            getImgUrl() {
                const images = require.context('../assets/img/cards/', true);
                return images('./' + this.card[IMAGE_PATH])
            },
            focusCard() {
                if (this.currentFocusedCard === this.card[ID]) {
                    this.$store.dispatch('setFocusedCardId', null);
                } else {
                    this.$store.dispatch('setFocusedCardId', this.card[ID]);
                }
            },
            playCard() {
                GameService.playCard(this.card[ID]).then(response => {

                });
            }
        },
        created() {
        }
    }
</script>