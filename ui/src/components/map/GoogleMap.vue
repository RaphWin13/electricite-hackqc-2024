<template>
  <GoogleMap api-key="AIzaSyAsCjFPU5aQwdQQfSRjKtizojHMVMqmq8g"
  style="width: 100%; height: 100vh; margin-top: 70px;"
  :center="center"
  :zoom="17"
  >
    <Marker v-for="batiment in batiments" :key="batiment" :options="{ position: batiment.coords, color: '#00FF00' }">
      <InfoWindow :options="{ position: batiment.coords, content: batiment.Nom }" />
    </Marker>
    <Rectangle v-for="batiment in batiments" :key="batiment" :options="{
      strokeColor: strokeColor.red,
      bounds: {
        north: batiment.coords.lat+0.0003,
        south: batiment.coords.lat-0.0002,
        east: batiment.coords.lng+0.0002,
        west: batiment.coords.lng-0.0002
      }
    }" />
  </GoogleMap>
</template>
  
<script setup>
import { GoogleMap, Marker, InfoWindow, Rectangle } from "vue3-google-map";

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
      "coords": {lat: 45.55183, lng: -73.53906},
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

const strokeColor = {
  green: "#00FF00",
  yellow: "#FFFF00",
  red: "#FF0000"
}

</script>