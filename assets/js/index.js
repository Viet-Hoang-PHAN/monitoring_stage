import Vue from 'vue';
import Vuetify from 'vuetify'
import router from './router';
import store from './store/store';

import 'vuetify/dist/vuetify.min.css'

import App from "./App.vue";
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify, {
    theme: {
        primary: colors.indigo.darken2,
        secondary: colors.indigo.lighten3,
    }
})


const app = new Vue({
    el: '#app',
    router,
    store,
    components: {
        App,
    },
    render: h => h(App)
});