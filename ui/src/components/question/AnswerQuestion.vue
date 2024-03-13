<template>
    <v-container>
        <v-row justify="center" align-items="center">
            <v-col cols="12" class="text-center">
                <v-row class="align-center" justify="center">
                    <v-btn class="h-auto" @click="this.handleAnswer(1)" variant="plain">
                        <v-icon :class="thumbUpClass" size="70px" icon="mdi-thumb-up" />
                    </v-btn>
                    <v-card class="ma-4" title="Répondez à la caméra avec votre pouce." color="green-lighten-3" rounded="lg">
                    </v-card>
                    <v-btn class="h-auto" @click="this.handleAnswer(0)" variant="plain">
                        <v-icon :class=this.thumbDownClass icon="mdi-thumb-down" size="70px" />
                    </v-btn>
                    </v-row>
                <p class="text-caption">Aucune image n'est enregistrée.</p>
            </v-col>
        </v-row>
        <v-row class="w-50 mx-auto" justify="center" align-items="center">
            <HandRecognitionVideo :handleGesture=this.handleGesture />
        </v-row>
    </v-container>
</template>

<script>
import HandRecognitionVideo from "@/components/question/HandRecognitionVideo.vue";

export default {
    name: "AnswerQuestion",
    components: {
        HandRecognitionVideo,
    },
    props: {
        handleAnswer: {
            type: Function,
            required: true
        }
    },
    data() {
        return {
            thumbUpClass: "undetected",
            thumbDownClass: "undetected",
            answerCountdownTime: 2000, //2 seconds
            currentCountdown: null,
        };
    },
    methods: {
        handleGesture(gesture) {
            console.log(gesture, " detected!");
            if (gesture == "thumbs_up") {
                this.handleThumbsUpDetected();
            } else if (gesture == "thumbs_down") {
                this.handleThumbsDownDetected();
            } else {
                this.handleNoGestureDetected();
            }
        },
        handleThumbsUpDetected() {
            this.thumbDownClass = "undetected";
            this.thumbUpClass = "thumbs-up-detected";
            if (this.currentAnswer != 1) {
                this.startNewAnswerCountdown(1);
                this.currentAnswer = 1;
            }
        },
        handleThumbsDownDetected() {
            this.thumbUpClass = "undetected";
            this.thumbDownClass = "thumbs-down-detected";
            if (this.currentAnswer != 0) {
                this.startNewAnswerCountdown(0);
                this.currentAnswer = 0;
            }
        },
        handleNoGestureDetected() {
            this.stopExistingTimeout();
            this.currentAnswer = null;
            this.thumbUpClass = "undetected";
            this.thumbDownClass = "undetected";
        },
        startNewAnswerCountdown(answer) {
            this.stopExistingTimeout();

            this.currentCountdown = setTimeout(() => {
                this.handleAnswer(answer);
            }, this.answerCountdownTime);
        },
        stopExistingTimeout() {
            if (this.currentCountdown)
                clearTimeout(this.currentCountdown);
        },
    }
}
</script>

<style>

.undetected {
    color: #000;
}

.thumbs-up-detected {
    color: #00FF00;
    transition: color 2s ease-in-out;
    animation: shake 0.5s infinite;
}

.thumbs-down-detected {
    color: #FF0000;
    transition: color 2s ease-in-out;
    animation: shake 0.5s infinite;
}

@keyframes shake {
    0% { transform: rotate(0); }
    25% { transform: rotate(-10deg); }
    50% { transform: rotate(10deg); }
    75% { transform: rotate(-10deg); }
    100% { transform: rotate(0); }
}

</style>