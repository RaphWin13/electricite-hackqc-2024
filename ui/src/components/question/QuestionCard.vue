<template>
    <v-card class="my-10 py-10 px-10 h-100" color="green-lighten-3" rounded="lg">
        <v-card-title> <p class="text-h5">{{ questionType }}</p> </v-card-title>
        <v-card-text class="mt-3 h-75 d-flex flex-column align-center justify-center">
            <p class="text-h3 font-weight-bold">{{ question }}</p>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: "QuestionCard",
    props: {
        questionType: String,
        question: String
    },
}
</script>