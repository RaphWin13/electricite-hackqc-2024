<template>
  <v-app>
    <v-app-bar elevation="5">
      <v-app-bar-title class="font-weight-bold">ÉlectriCITÉ</v-app-bar-title>
    </v-app-bar>
    <v-btn class="my-6 mx-auto" variant="outlined" width="auto" @click="togglePages">{{showQuestion? "Masquer la question" : "Afficher une question"}}</v-btn>
    <QuestionPage v-if="showQuestion" />
    <HomePage v-else />
  </v-app>
</template>

<script>
import HomePage from './HomePage.vue';
import QuestionPage from './QuestionPage.vue';

export default {
  name: 'App',
  components: {
    HomePage,
    QuestionPage
  },
  data() {
    return {
      showQuestion: false
    };
  },
  methods: {
    togglePages() {
      this.showQuestion = !this.showQuestion;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  background: "#F6FAE9" !important;
}

.v-application {
  background-color: #F6FAE9 !important;
}
</style>
