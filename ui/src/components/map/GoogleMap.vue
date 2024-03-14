<template>
  <GoogleMap api-key="AIzaSyAsCjFPU5aQwdQQfSRjKtizojHMVMqmq8g"
  style="width: 100%; height: 80vh;"
  :center="center"
  :zoom="17"
  >
    <InfoWindow v-for="batiment in batiments" :key="batiment" 
    :options="{ position: this.getInfoWindowPosition(batiment), content: batiment.Nom, maxWidth: 150}" />
    <Marker v-for="batiment in batiments" :key="batiment" :options="{ position: batiment.coords, 
      icon: {path: mdiMapMarker, scale: 2, fillColor: scoreColor[batiment.score], fillOpacity: 1, strokeWeight: 0, anchor:{x:15, y:20}}}" >
      <InfoWindow :options="{ content: batiment.Nom, maxWidth: 150}" />
    </Marker>
  </GoogleMap>
</template>
  
<script setup>
import { GoogleMap, Marker , InfoWindow } from "vue3-google-map";
import { mdiMapMarker } from '@mdi/js';

const center = {lat: 45.5538, lng: -73.54037}


const batiments = {
    "0": {
      "Nom": "CCSE Maisonneuve",
      "coords": {lat: 45.5538, lng: -73.54037},
      "score": "C"
    },
    "1": {
      "Nom": "Centre Morgan",
      "coords": {lat: 45.55355, lng: -73.53818},
      "score": "B"
    },
    "2": {
      "Nom": "Maison de la Culture",
      "coords": {lat: 45.5512, lng: -73.54044},
      "score": "B"
    },
    "3": {
      "Nom": "Bibliothèque Maisonneuve",
      "coords": {lat: 45.55062, lng: -73.54063},
      "score": "B"
    },
    "4": {
      "Nom": "Centre social l'Achoppe",
      "coords": {"lat": 45.55178, "lng": -73.53816},
      "score": "D"
    },
    "5": {
      "Nom": "École secondaire Chomedey-De-Maisonneuve",
      "coords": {lat: 45.55272, lng: -73.53847},
      "score": "B"
    },
    "6": {
      "Nom": "Restaurant Bagatelle Bistro",
      "coords": {lat: 45.55296, lng: -73.5397},
      "score": "A"
    }
}

const scoreColor = {
  "A": "#00FF00", // green
  "B": "#FFD700", // yellow
  "C": "#FF8C00", // orange
  "D": "#FF0000", // red
  "E": "#FF0000" // red
}

</script>

<script>
export default {
  name: "GoogleMap",
  methods: {
    getInfoWindowPosition(batiment) {
      return {lat: batiment.coords.lat + 0.00025, lng: batiment.coords.lng - 0.00005}
    }
  },
}
</script>

<style>
  .gm-style-iw {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
</style>