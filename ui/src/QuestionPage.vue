<template>
    <v-container class="w-50 px-10">
        <v-col v-if="!this.answerReady" cols="12" class="text-center" justify="center" >
            <QuestionCard 
                :questionType=question.type
                :question=question.question
            />
            <AnswerQuestion :handleAnswer="this.handleAnswer" />
        </v-col>
        <ThankYouAnswerCard v-if="this.answerReady" :answer="this.currentAnswer"/>
    </v-container>
</template>

<script>
import QuestionCard from "@/components/question/QuestionCard.vue";
import axios from "axios";
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
            answerReady: false,
            question: ""
        };
    },
    async mounted(){
        this.question = await this.get_question();
    },
    methods: {
        handleAnswer(answer) {
            this.answerReady = true;
            this.currentAnswer = answer;
        },
        async get_question(){
            const url = `${axios.defaults.baseURL}/question`;
            return await axios.get(url).then(response => response.data);
        }, 
    }
}
</script>

<style>

body {
    background-color: #FFF;
}

</style>