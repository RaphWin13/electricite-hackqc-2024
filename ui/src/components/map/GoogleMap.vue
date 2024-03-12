<template>
    <GoogleMap api-key="AIzaSyAsCjFPU5aQwdQQfSRjKtizojHMVMqmq8g"
    style="width: 100%; height: 100vh; margin-top: 70px;"
    :center="center"
    :zoom="15">
    </GoogleMap>
  </template>
  
  <script>
  import { defineComponent } from "vue";
  import { GoogleMap } from "vue3-google-map";
  
  export default defineComponent({
    components: { GoogleMap },
    setup() {
      const center = { lat: 46.8131, lng: -71.2075 };
  
      return { center };
    },
  });
  </script>