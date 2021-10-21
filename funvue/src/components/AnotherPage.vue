<template>
    <h1>{{ msg }}</h1>
</template>

<script>
export default {
  name: 'AnotherPage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    doSomething() {
      this.msg= 'another page hahahahahahahaha!';
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
