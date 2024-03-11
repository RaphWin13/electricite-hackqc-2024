<template>
  <v-app>
    <v-btn class="mb-4 mx-auto" width="200" @click="togglePages">{{showQuestion? "Hide question" : "Show questions"}}</v-btn>
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
}
</style>
