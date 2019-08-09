<template>
      <v-container grid-list-md text-xs-center>
        <v-layout row wrap>
    <v-flex xs12>
                <v-card class="mx-auto my-3 text-xs-center" width="auto"
                    outlined>
                    <v-container grid-list-md fluid>
                        <v-layout row wrap>
                    <template v-if="terminal !== undefined">
                        <v-flex xs12>
                            <v-icon>devices_other</v-icon><v-spacer></v-spacer> Terminal : {{ terminal.terminal_id }}
                        </v-flex>
                        <v-flex xs6 sm3 v-for="(value, propertyName, index) in terminal" :key="index">
                            <div v-if="propertyName !== 'last_msg'">
                        {{ propertyName }} : {{ value }}

                            </div>

                        </v-flex>
                        <v-flex xs12><small>{{ time }}</small></v-flex>
                    </template>
                        </v-layout>
                    </v-container>
                </v-card>
            </v-flex>
            <v-flex xs12>
                <v-divider></v-divider>
            </v-flex>
            <template v-if="servicesList !== undefined">
                <Service v-for="service in servicesList" :key="service.id" v-bind:id="service.id"></Service>
                <div v-if="servicesList.length === 0">
                    Pas de service attribué
                </div>
            </template>
        </v-layout>
      </v-container>
</template>


<script>
import Service from './Service.vue'
import { mapGetters, mapState } from 'vuex';

export default {
    components: {
        Service
    },
    computed: {
        ...mapGetters(['getTerminalByID', 'getTerminalServicesFilteredByID', 'getCurrentTime']),
        ...mapState(['currentTime']),
        time () {
            return this.getCurrentTime(this.terminal.last_msg)
        },
        terminal () {
            return this.getTerminalByID(this.$route.params.id_tm)
        },
        servicesList() {
            return this.getTerminalServicesFilteredByID(this.$route.params.id_tm)
        }
    },
}
</script>


<style lang="scss" scoped>

</style>
