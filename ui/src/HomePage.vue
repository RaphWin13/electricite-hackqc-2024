<template>
  <EquivalenceAnimation />
  <ScorePodium style="margin-top: 5em" />
  <v-card flat title="Visualiser les réductions du quartier aujourd'hui">
    <v-card-caption>comparé à la moyenne du mois de l'année précédente</v-card-caption>
  </v-card>
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
