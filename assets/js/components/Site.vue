<template>
    <v-container grid-list-md text-xs-center fill-height="true">
        <v-layout wrap row>
            <v-flex xs12 sm6>
                <v-card height="100%">
                    <v-card-title class="justify-center">
                        <v-icon size=200>account_circle</v-icon>
                    </v-card-title>
                    <v-card-text>
                        <v-list>
                        <template v-for="(value, propertyName) in getSite">

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
                                    VM : {{vmsList.length}}
                                </v-list-tile-content>
                            </v-list-tile>
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-flex>
            <v-flex xs12 sm6 class="scroll-list">
                <v-card outlined class="mb-1">
                    <v-card-text>
                        VM List
                    </v-card-text>
                </v-card>
                <template v-for="vm in vmsList">
                    <v-hover v-slot:default="{ hover }" :key="vm.id">
                <v-card :elevation="hover ? 12 : 2"
              :class="{ 'on-hover': hover }" class="mb-1"
              :to="{ name: 'vm-detail', params: { id_vm: vm.id, id_site: getSite.id }}">
                    <v-card-text>
                        <v-list>
                            <template v-for="(value, propertyName) in vm">
                                    <div v-if="propertyName !== 'id' && propertyName !== 'site_id'" :key="value.id">
                                <v-list-tile>
                                        <v-list-tile-content>
                                            {{propertyName}} : {{value}}
                                        </v-list-tile-content>
                                </v-list-tile>
                                    </div>
                            </template>
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
import {mapState, mapGetters} from 'vuex';

export default { 
    computed: {
        ...mapGetters(['getSiteByID', 'getSiteVmsFilteredByID']),
        getSite () {
            return this.getSiteByID(this.$route.params.id_site)
        },
        vmsList() {
            return this.getSiteVmsFilteredByID(this.$route.params.id_site)
        }
    },
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
