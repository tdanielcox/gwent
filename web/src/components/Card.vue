<template>
    <div class="card"
         :style="css"
         :id="cardId"
         :class="cardClasses"
         @click="focusCard">

        <div class="actual-strength">{{ cardActualStrength }}</div>

        <div class="confirm-box">
            <div class="inner">
                <div class="card-details">
                    <h3>{{ cardName }}</h3>
                    <p v-if="cardAbility">{{ cardAbility }}</p>
                </div>

                <div class="actions" :class="{ 'blurred': pauseUser }">
                    <div class="cover" v-if="pauseUser">
                        {{ currentPlayer === 1 ? 'Waiting for computer' : 'Waiting' }}
                    </div>

                    <div class="actions-inner">
                        <h2>Play this card?</h2>
                        <button class="yes-button" @click="playCard">Yes</button>
                        <button class="no-button">No</button>
                    </div>
                </div>
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

            .confirm-box {
                display: none;
            }
        }

        &.inGraveyard {
            transform: scale(1);
            cursor: default;
            width: 110px;
            height: 144px;
            top: 0;
            left: 0;
            position: absolute;
            opacity: 0.4;

            &:hover {
                opacity: 0.4;
                transform: scale(1);
                z-index: 1;
            }

            .actual-strength,
            .confirm-box {
                display: none;
            }
        }

        &.inSelector {
            width: 110px;
            height: 172px;

            .actual-strength {
                display: none;
            }
        }

        .actions.blurred {

        }

        .actual-strength {
            position: absolute;
            top: 6px;
            left: 6px;
            width: 12px;
            height: 12px;
            border-radius: 6px;
            z-index: 25;
            line-height: 12px;
            font-size: 0.8rem;
            background: rgb(255,255,255);
            background: -moz-linear-gradient(-45deg, rgba(255,255,255,1) 53%, rgba(142,142,142,1) 100%);
            background: -webkit-linear-gradient(-45deg, rgba(255,255,255,1) 53%,rgba(142,142,142,1) 100%);
            background: linear-gradient(135deg, rgba(255,255,255,1) 53%,rgba(142,142,142,1) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#8e8e8e',GradientType=1 );
        }

        &.noStrength .actual-strength {
            display: none;
        }

        .confirm-box {
            opacity: 0;
            transition: opacity 0.5s ease-out;
            background: rgba(255,255,255,0.8);
            height: 100%;
            width: 100%;
            position: relative;
            color: #000;

            .inner {
                position: relative;
                top: 50%;
                transform: translateY(-50%);
                padding: 1px 0.5rem;
                color: #000;

                h2 {
                    font-size: 0.6rem;
                    margin-top: 1rem;
                    margin-bottom: 1rem;
                    color: #000;
                }

                button {
                    font-size: 0.8rem;
                    cursor: pointer;

                    &:hover {
                        background: #c0c0c0;
                    }
                }

                .card-details {
                    margin-top: 0.4rem;
                    color: #000;

                    h3 {
                        font-size: 0.8rem;
                    }

                    p {
                        font-size: 0.6rem;
                    }
                }
            }
        }

        .actions {
            position: relative;

            &.blurred .actions-inner {
                opacity: 0;
            }

            .cover {
                position: absolute;
                width: 100%;
                top: 0;
                bottom: 0;
                font-size: 0.6rem;

                &:after {
                    overflow: hidden;
                    display: inline-block;
                    vertical-align: bottom;
                    -webkit-animation: ellipsis steps(4,end) 900ms infinite;
                    animation: ellipsis steps(4,end) 900ms infinite;
                    content: "\2026";
                    width: 0;
                }

                @keyframes ellipsis {
                    to {
                        width: 1.25em;
                    }
                }

                @-webkit-keyframes ellipsis {
                    to {
                        width: 1.25em;
                    }
                }
            }
        }
    }
</style>

<script>
    import GameService from '../services/GameService.js';

    const NAME = 0;
    const ROW = 1;
    const STRENGTH = 2;
    const ABILITY = 3;
    const AFFECTS = 4;
    const IMAGE_PATH = 5;
    const ID = 6;
    const ACTUAL_STRENGTH = 7;

    const NONE = 0;
    const BOND = 1;
    const SPY = 2;
    const HERO = 3;
    const WEATHER = 6;
    const SCORCH = 7;

    export default {
        props: ['card', 'inPlay', 'inGraveyard', 'inSelector'],
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
            currentPlayer() {
                return this.$store.getters.currentPlayer;
            },
            notificationVisible() {
                return this.$store.getters.notificationVisible;
            },
            pauseUser() {
                return this.currentPlayer === 1 || this.notificationVisible;
            },
            cardClasses() {
                return {
                    selected: this.currentFocusedCard === this.card[ID],
                    inBackground: this.currentFocusedCard && this.currentFocusedCard !== this.card[ID],
                    inPlay: this.inPlay,
                    inGraveyard: this.inGraveyard,
                    inSelector: this.inSelector,
                    noStrength: this.card[ABILITY] === WEATHER
                             || this.card[ABILITY] === HERO
                             || this.card[ABILITY] === SCORCH,
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
            cardId() {
                return this.card[ID];
            },
            cardActualStrength() {
                return this.card[ACTUAL_STRENGTH];
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
                if (this.inPlay || this.inGraveyard || this.currentFocusedCard === this.card[ID]) {
                    this.$store.dispatch('setFocusedCardId', null);
                } else {
                    this.$store.dispatch('setFocusedCardId', this.card[ID]);
                }
            },
            playCard() {
                if (this.inSelector) {
                    GameService.reviveCard(this.card[ID]).catch(() => {

                    });

                    this.$store.dispatch('setCardSelectorVisible', false);
                } else {
                    GameService.playCard(this.card[ID]);
                }
            }
        },
        created() {
        }
    }
</script>