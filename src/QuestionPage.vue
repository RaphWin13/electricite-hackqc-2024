<template>
    <v-container full-height class="w-50 px-10">
        <v-col cols="12" class="text-center" justify="center" >
            <QuestionCard 
                questionType="POUR ou CONTRE?" 
                question="Ceci est une longue question sur un sujet demandant l'avis des citoyens blablablabla qu'en pensez-vous blablabla?" 
            />
            <v-row justify="center" align-items="center">
                <v-col cols="12" class="text-center">
                    <v-row class="align-center" justify="center">
                        <v-icon icon="mdi-thumb-up" size="75px"/>
                        <v-card class="ma-4" title="Répondez à la caméra avec votre pouce." color="green-lighten-3" rounded="lg">
                        </v-card>
                        <v-icon icon="mdi-thumb-down" size="75px"/>
                    </v-row>
                    <p class="text-caption">Aucune image n'est enregistrée.</p>
                </v-col>
            </v-row>
            <v-row class="w-50 mx-auto" justify="center" align-items="center">
                <v-img
                :height="500"
                cover
                :src=cameraView
                rounded="circle"
                ></v-img>
            </v-row>
        </v-col>
    </v-container>
</template>

<script>
import QuestionCard from "@/components/question/QuestionCard.vue";

export default {
    name: "QuestionPage",
    components: {
        QuestionCard
    },
    data() {
        return {
            cameraView: require("@/assets/someone_at_bus_stop_thumbs_up.jpg")
        };
    },
}
</script>

<style>

body {
    background-color: #FFF;
}

</style>
