<template>
    <v-container grid-list-md text-xs-center fill-height="true">
        <v-layout wrap row>
            <v-flex xs12 sm6>
                <v-card height="100%">
                    <v-card-title class="justify-center">
                        <v-icon size=200>router</v-icon>
                    </v-card-title>
                    <v-card-text>
                        <v-list>
                        <template v-for="(value, propertyName, index) in gateway">

                            <div v-if="propertyName !== 'id' && propertyName !== 'last_msg'" :key="index">
                            <v-list-tile >
                                <v-list-tile-content>
                                    {{propertyName}} : {{value}}
                                </v-list-tile-content>
                            </v-list-tile>
                            </div>
                        </template>
                            <v-list-tile>
                                <v-list-tile-content>
                                    Numbers of Terminals : {{terminalList.length}}
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-flex>
            <v-flex xs12 sm6 class="scroll-list">
                <v-card outlined class="mb-1">
                    <v-card-text>
                        Terminal List
                    </v-card-text>
                </v-card>
                <template v-for="terminal in terminalList">
                    <v-hover v-slot:default="{ hover }" :key="terminal.id">
                <v-card :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }" class="mb-1"
              :to="{ name: 'terminal-detail', params: { id_vm: id_vm, id_site: id_site, id_gw: gateway.id, id_tm: terminal.id }}">
                    <v-card-text>
                        <v-list>
                            <template v-for="(value, propertyName, index) in terminal">
                                    <div v-if="propertyName !== 'id' && propertyName !== 'site_id' && propertyName !== 'last_msg'" :key="index">
                                <v-list-tile>
                                        <v-list-tile-content>
                                            {{propertyName}} : {{value}}
                                        </v-list-tile-content>
                                </v-list-tile>
                                    </div>
                            </template>
                            <small>{{time(terminal.last_msg)}}</small>
                        </v-list>
                    </v-card-text>
                </v-card>
                </v-hover>
                </template>

            </v-flex>
    </v-layout>
        </v-container>
</template>


<script>
import { mapGetters } from 'vuex';

export default {
    data () {
        return {
            dialog: false,
            id_site: this.$route.params.id_site,
            id_vm: this.$route.params.id_vm
        }
    },
    computed: {
        ...mapGetters(['checkParams', 'getGatewayByID', 'getGatewayTerminalsFilteredByID', 'getCurrentTime']),
        gateway() {
            return this.getGatewayByID(this.$route.params.id_gw)
        },
        terminalList() {
            return this.getGatewayTerminalsFilteredByID(this.$route.params.id_gw)
        }
    },
    methods: {
        time (lastMsg) {
            return this.getCurrentTime(lastMsg)
        },
    },
}
</script>


<style lang="scss" scoped>
.slide-fade-enter-active {
  transition: all .2s .4s ease;
}
.slide-fade-leave-active {
  transition: all .2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
