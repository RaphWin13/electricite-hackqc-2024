<template>
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
        <p>Réduction: <strong>{{standings["1"]["score"]}}</strong></p>
      </v-sheet>
      <v-sheet
        class="py-1 rounded-t-xl"
        height="155"
        width="300"
        color="green-accent-3"
      >
        <p class="font-weight-black podium-rank">1</p>
        <p><i>{{standings["0"]["Nom"]}}</i></p>
        <p>Réduction:  <strong>{{standings["0"]["score"]}}</strong></p>
      </v-sheet>
      <v-sheet
        class="py-1 rounded-t-xl"
        height="105"
        width="300"
        color="light-green-lighten-1"
      >
        <p class="font-weight-black podium-rank">3</p>
        <p><i>{{standings["2"]["Nom"]}}</i></p>
        <p>Réduction: <strong>{{standings["2"]["score"]}}</strong></p>
      </v-sheet>
    </v-row>
  </v-container>
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
        "score": this.computeReductionPercentDisplay(rawStandings[position]["score"])
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