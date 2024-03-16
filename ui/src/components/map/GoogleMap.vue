<template>
  <v-card class="mx-auto mb-9 justify-lg-center" variant ="outlined" width="95%">
    <GoogleMap :api-key="googleMapsApiKey"
    style="width: 100%; height: 80vh;"
    :center="center"
    :zoom="17"
    >
      <InfoWindow v-for="batiment in buildings" :key="batiment" 
      :options="{ position: getInfoWindowPosition(batiment), content: batiment.Nom, maxWidth: 150}" />
      <Marker v-for="batiment in buildings" :key="batiment" :options="{ position: {lat: batiment.Latitude, lng: batiment.Longitude}, 
        icon: {path: mdiMapMarker, scale: 2, fillColor: scoreColor[batiment.score], fillOpacity: 1, strokeWeight: 0, anchor:{x:15, y:20}}}" >
        <InfoWindow :options="{ content: batiment.Nom, maxWidth: 150}" />
      </Marker>
    </GoogleMap>
  </v-card>
</template>
  
<script setup>
import { GoogleMap, Marker , InfoWindow } from "vue3-google-map";
import { mdiMapMarker } from '@mdi/js';

const center = {lat: 45.5538, lng: -73.54037}

const scoreColor = {
  "A": "#00FF00", // green
  "B": "#FFD700", // yellow
  "C": "#FF8C00", // orange
  "D": "#FF0000", // red
  "E": "#FF0000" // red
}

</script>

<script>
import axios from "axios";

export default {
  name: "GoogleMap",
  data() {
    return {
      buildings: [],
      googleMapsApiKey: process.env.VUE_APP_GOOGLE_MAPS_API_KEY
    }
  },
  async mounted() {
    this.buildings = await this.getBuildingsPositionAndScore()
  },
  methods: {
    getInfoWindowPosition(batiment) {
      return {lat: batiment.Latitude + 0.00025, lng: batiment.Longitude - 0.00005}
    },
    async getBuildingsPositionAndScore() {
      const url = `${axios.defaults.baseURL}/score/letters`;
      return await axios.get(url).then(response => response.data);
    }
  },
}
</script>
