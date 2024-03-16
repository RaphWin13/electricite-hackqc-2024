<template>
    <v-card variant="flat" class="ma-4" title="Merci pour votre réponse!" color="#F6FAE9" rounded="lg">
        <v-card-text>
            <v-icon :icon="this.answersIcon[this.answer]" size="75px"></v-icon>
        </v-card-text>
    </v-card>
</template>

<script>

export default {
    name: "ThankYouAnswerCard",
    props: {
        answer: Number,
    },
    data() {
        return {
            answersIcon: {
                0: "mdi-thumb-down",
                1: "mdi-thumb-up"
            }
        }
    }
}

</script>