import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios";

import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

axios.defaults.baseURL = "http://127.0.0.1:5050";

const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: "mdi",
    },
});

createApp(App).use(vuetify).mount('#app')
