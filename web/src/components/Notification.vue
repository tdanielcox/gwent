<template>
    <div class="notification" :class="notificationsClass">{{ notification }}</div>
</template>

<style lang="scss">
    .notification {
        position: absolute;
        top: 50%;
        margin-top: -90px;
        left: 0;
        width: 100%;
        height: 180px;
        background: rgba(0, 0, 0, 0.8);
        z-index: 200;
        line-height: 180px;
        font-size: 30px;
        color: #FFF;
        text-align: center;
        opacity: 0;
        transition: opacity 0.4s linear;

        &.visible {
            opacity: 1;
        }
    }
</style>

<script>
    // import GameService from '../services/GameService.js';

    export default {
        props: [],
        computed: {
            game() {
                return this.$store.getters.game;
            },
            notification() {
                return this.$store.getters.notification;
            },
            showNotification() {
                return this.$store.getters.notificationVisible;
            },
            notificationsClass() {
                return {
                    visible: this.showNotification
                }
            }
        },
        methods: {

        },
        mounted() {

        }
    }
</script>