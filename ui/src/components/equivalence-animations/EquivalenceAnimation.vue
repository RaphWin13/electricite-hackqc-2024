<template>
  <div class="equivalence">
    <VehiculeAnimation co2Quantity="103 tonnes" equivalence="un aller Paris-Montréal" :type=types.airplane />
  </div>
</template>

<script>
import VehiculeAnimation from './VehiculeAnimation.vue'

export default {
  name: 'EquivalenceAnimation',
  components: {
    VehiculeAnimation
  },
  data() {
    return {
      types: {
        car: 'car',
        bus: 'bus',
        airplane: 'airplane'
      }
    }
  }
}
</script>
