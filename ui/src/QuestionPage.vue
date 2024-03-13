<template>
    <v-container class="w-50 px-10">
        <v-col v-if="!this.answerReady" cols="12" class="text-center" justify="center" >
            <QuestionCard 
                questionType="POUR ou CONTRE?" 
                question="Ceci est une longue question sur un sujet demandant l'avis des citoyens blablablabla qu'en pensez-vous blablabla?" 
            />
            <AnswerQuestion :handleAnswer="this.handleAnswer" />
        </v-col>
        <ThankYouAnswerCard v-if="this.answerReady" :answer="this.currentAnswer"/>
    </v-container>
</template>

<script>
import QuestionCard from "@/components/question/QuestionCard.vue";
import AnswerQuestion from "@/components/question/AnswerQuestion.vue";
import ThankYouAnswerCard from "@/components/question/ThankYouAnswerCard.vue";

export default {
    name: "QuestionPage",
    components: {
        QuestionCard,
        AnswerQuestion,
        ThankYouAnswerCard
    },
    data() {
        return {
            currentAnswer: null,
            answerReady: false
        };
    },
    methods: {
        handleAnswer(answer) {
            this.answerReady = true;
            this.currentAnswer = answer;
        }
    }
}
</script>

<style>

body {
    background-color: #FFF;
}

</style>