<template>
  <v-app>
    <div class="equivalence">
      <VehiculeAnimation 
          :co2Quantity=funfact.fact
          :equivalence=funfact.equivalence
          :type=types.airplane />
    </div>
  </v-app>
</template>

<script>
import VehiculeAnimation from './VehiculeAnimation.vue'
import axios from "axios";

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
        airplane: 'airplane',
      },
      funfact: ""
    };
  },
  async mounted(){
  this.funfact = await this.get_funfact();
  },
  methods: {
    async get_funfact(){
        const url = `${axios.defaults.baseURL}/funfact`;
        return await axios.get(url).then(response => response.data);
    } 
  }
}
</script>
