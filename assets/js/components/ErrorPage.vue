<template>
    <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex xs12>
                <v-alert dense outlined :value="true" type="error">
                    La page que vous essayez d'accéder n'existe pas <br/>
                    Vous allez être redirigé vers le dashboard d'ici {{ time }} sec...

                </v-alert>
                </v-flex>
            </v-layout>
      </v-container>
</template>


<script>
import { setInterval } from 'timers';
export default {
    data () {
        return {
            time: 3
        }
    },
    mounted () {
        this.returnToPreviousPage()
        this.timer()
    },
    methods: {
        returnToPreviousPage () {
            setTimeout( () => {
                this.$router.push({name: 'home'})
            }, 3000)
        },
        timer () {
            setInterval( () => {
                if (!this.time == 0) {
                    this.time--
                }
            }, 1000)
        }
    }

    
}
</script>


<style lang="scss" scoped>

</style>
