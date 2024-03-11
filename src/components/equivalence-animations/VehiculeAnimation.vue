<template>
  <v-row class="animation" justify="center" align-items="center">
    <v-sheet class="flag py-1" elevation="24" height="50" width="300" rounded="lg" color="green-lighten-3">
        <p class="font-weight-black">{{co2Quantity}} de CO₂</p>
        <p>équivaut à {{equivalence}}</p>
    </v-sheet>
    <v-icon class="animated-vehicule ml-2" size="60" :icon=icons[type] :class="type" elevation="24"/>
  </v-row>
</template>

<script>
export default {
  name: 'VehiculeAnimation',
  props: {
    co2Quantity: String,
    equivalence: String,
    type: String
  },
  data() {
    return {
      icons: {
        airplane: 'mdi-airplane',
        bus: 'mdi-bus-side',
        car: 'mdi-car-side',
      }
    };
  },
}
</script>

<style scoped>
.animation {
  position: absolute;
  animation: fly 20s linear infinite;
}

.animated-vehicule {
  position: absolute;
  left: 100%
}

.airplane {
  transform: rotate(45deg);
  top: -5px;
}

@keyframes fly {
  0% {
    left: -360px;
  }
  100% {
    left: calc(100% + 360px);
  }
}
</style>
