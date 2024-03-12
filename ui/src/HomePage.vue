<template>
  <EquivalenceAnimation />
  <GoogleMap />
</template>

<script>
import EquivalenceAnimation from './components/equivalence-animations/EquivalenceAnimation.vue';
import GoogleMap from './components/map/GoogleMap.vue';

export default {
  name: 'HomePage',
  components: {
    EquivalenceAnimation,
    GoogleMap
  }
}
</script>
