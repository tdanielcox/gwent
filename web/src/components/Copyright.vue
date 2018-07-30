<template>
    <div class="copyright">
        <p>CD PROJEKT®, The Witcher®, GWENT® are registered trademarks of CD PROJEKT Capital Group. GWENT game © CD PROJEKT S.A. All rights reserved. Developed by CD PROJEKT S.A. GWENT game is set in the universe created by Andrzej Sapkowski. All other copyrights and trademarks are the property of their respective owners.</p>

        <p>This website was created solely for educational purposes and is not associated with CD PROJEKT RED in any way. All code is open source and available for free.</p>

        <p><a href="https://github.com/tdanielcox/gwent">View the source code on Github</a></p>
    </div>
</template>

<style lang="scss">
    .copyright {
        position: absolute;
        top: 24px;
        left: 22px;
        width: 400px;
        height: 144px;

        p {
            font-size: 1rem;
            color: #FFF;
            margin-bottom: 10px;
        }

        a {
            color: #FFF;
        }
    }
</style>

<script>
    export default {
        props: [],
        computed: {
        },
        methods: {

        },
        mounted() {

        }
    }
</script>