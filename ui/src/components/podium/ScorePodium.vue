<template>
  <v-card class="mx-auto pt-2 pb-5" variant="outlined" width="95%">
    <v-card-title>Score</v-card-title>
    <v-divider class="mb-5"></v-divider>
    <v-container>
      <v-row align="end" justify="center">
        <v-sheet
          class="py-1 rounded-t-xl"
          height="130"
          width="300"
          color="green-lighten-2"
        >
          <p class="font-weight-black podium-rank">2</p>
          <p><i>{{standings["1"]["Nom"]}}</i></p>
          <p> Réduction: <strong>{{standings["1"]["score"]}}</strong></p>
          <p class="text-subtitle-1"> Économies équivalentes à {{standings["1"]["eq_airplane"]}} <v-icon class="mt-2">mdi-airplane</v-icon> </p>
        </v-sheet>
        <v-sheet
          class="py-1 rounded-t-xl"
          height="165"
          width="300"
          color="green-accent-3"
        >
          <p class="font-weight-black podium-rank">1</p>
          <p><i>{{standings["0"]["Nom"]}}</i></p>
          <p >Réduction:  <strong>{{standings["0"]["score"]}}</strong></p>
          <p>Économies équivalentes à {{standings["0"]["eq_airplane"]}} <v-icon class="mt-2">mdi-airplane</v-icon> </p>
        </v-sheet>
        <v-sheet
          class="py-1 rounded-t-xl"
          height="115"
          width="300"
          color="light-green-lighten-1"
        >
          <p class="font-weight-black podium-rank">3</p>
          <p><i>{{standings["2"]["Nom"]}}</i></p>
          <p>Réduction: <strong>{{standings["2"]["score"]}}</strong></p>
          <p> Économies équivalentes à {{standings["2"]["eq_airplane"]}} <v-icon class="mt-2">mdi-airplane</v-icon> </p>
        </v-sheet>
      </v-row>
      <v-row class="pt-4" align="center" justify="center">
        <p > <v-icon class="mt-2">mdi-airplane</v-icon> : voyage d'avion Montréal / New-York </p>
      </v-row>
      <v-divider class="my-6"></v-divider>
        <v-card>
          <v-card-title>Visualiser les réductions du quartier aujourd'hui</v-card-title>
          <v-card-text>comparé à la moyenne du mois de l'année précédente</v-card-text>
        </v-card>
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  name: "ScorePodium",
  data() {
    return {
      standings: {"0":{}, "1":{}, "2":{}}
    };
  },
  async mounted() {
    let rawStandings = await this.getStandings();
    let newStandings = {}

    for (let position in ["0", "1", "2"]) {
      newStandings[position] = {
        "Nom": rawStandings[position]["Nom"],
        "score": this.computeReductionPercentDisplay(rawStandings[position]["score"]),
        "eq_airplane": this.computeReductionPercentDisplay(rawStandings[position]["eq_airplane"])
      }
    }

    this.standings = newStandings
  },
  methods: {
    async getStandings() {
      const url = `${axios.defaults.baseURL}/score/podium`;
      return await axios.get(url).then((response) => response.data);
    },
    computeReductionPercentDisplay(rawScore) {
      let percent = Number.parseFloat(rawScore).toFixed(2).slice(-2) + "%";
      if (percent[0] == "0") percent = percent.slice(1)

      if (rawScore > 0.005) return "-" + percent
      else return percent
    }
  },
};
</script>

<style>
  .podium-rank {
    font-size: larger;
  }
</style>