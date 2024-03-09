<template>
  <EquivalenceAnimation />
</template>

<script>
import EquivalenceAnimation from './components/equivalence-animations/EquivalenceAnimation.vue';

export default {
  name: 'App',
  components: {
    EquivalenceAnimation
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
