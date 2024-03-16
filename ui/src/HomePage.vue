<template>
  <EquivalenceAnimation />
  <ScorePodium style="margin-top: 7em" />
  <GoogleMap />
</template>

<script>
import EquivalenceAnimation from './components/equivalence-animations/EquivalenceAnimation.vue';
import GoogleMap from './components/map/GoogleMap.vue';
import ScorePodium from './components/podium/ScorePodium.vue'

export default {
  name: 'HomePage',
  components: {
    EquivalenceAnimation,
    ScorePodium,
    GoogleMap
  }
}
</script>./components/podium/ScorePodium.vue
