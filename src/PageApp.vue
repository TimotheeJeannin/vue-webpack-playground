<template>
    <div id="app">
        <h1>{{ msg }}</h1>
    </div>
</template>

<script>
    export default {
        name: 'app',
        data() {
            return {
                msg: 'Welcome to Page!'
            }
        }
    }
</script>

<style lang="scss">
    h1 {
        color: #42b983;
    }
</style>
