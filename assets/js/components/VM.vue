<template>
<v-container grid-list-md text-xs-center fill-height="true">
        <v-layout wrap row>
            <v-flex xs12 sm6>
                <v-card height="100%">
                    <v-card-title class="justify-center">
                        <v-icon size=200>computer</v-icon>
                    </v-card-title>
                    <v-card-text>
                        <v-list>
                        <template v-for="(value, propertyName) in getVM">

                            <div v-if="propertyName !== 'id'" :key="value.id">
                            <v-list-tile >
                                <v-list-tile-content>
                                    {{propertyName}} : {{value}}
                                </v-list-tile-content>
                            </v-list-tile>
                            </div>
                        </template>
                            <v-list-tile>
                                <v-list-tile-content>
                                    Numbers of Gateways : {{gatewaysList.length}}
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-flex>
            <v-flex xs12 sm6 class="scroll-list">
                <v-card outlined class="mb-1">
                    <v-card-text>
                        Gateway List
                    </v-card-text>
                </v-card>
                <template v-for="gateway in gatewaysList">
                    <v-hover v-slot:default="{ hover }" :key="gateway.id">
                <v-card :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }" class="mb-1"
              :to="{ name: 'gateway-detail', params: { id_vm: getVM.id, id_site: getSite.id, id_gw: gateway.id }}">
                    <v-card-text>
                        <v-list>
                            <template v-for="(value, propertyName) in gateway">
                                    <div v-if="propertyName !== 'id' && propertyName !== 'site_id' && propertyName !== 'last_msg'" :key="value.id">
                                <v-list-tile>
                                        <v-list-tile-content>
                                            {{propertyName}} : {{value}}
                                        </v-list-tile-content>
                                </v-list-tile>
                                    </div>
                            </template>
                            <small>{{time(gateway.last_msg)}}</small>
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
import {mapGetters} from 'vuex'

export default {
    computed: {
        ...mapGetters(['getSiteByID', 'getVmByID', 'getVmGatewaysFilteredByID', 'getCurrentTime']),
        getSite () {
            return this.getSiteByID(this.$route.params.id_site)
        },
        getVM () {
            return this.getVmByID(this.$route.params.id_vm)
        },
        gatewaysList() {
            return this.getVmGatewaysFilteredByID(this.$route.params.id_vm)
        }
    },
    methods: {
        time(lastMsg) {
            return this.getCurrentTime(lastMsg)
        }
    }
}
</script>


<style lang="scss" scoped>
@media screen and (max-width: 600px){
    .scroll-list {
        height: auto;
        overflow: unset
    }
}
@media screen and (min-width: 601px){
    
    .scroll-list {
        height: 825px;
        overflow: auto
    }
}
</style>
