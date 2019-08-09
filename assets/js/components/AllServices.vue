<template>
      <v-container grid-list-md text-xs-center>
        <v-layout wrap row>
            <v-flex xs8>
            <v-select
            v-model="selectedFilter"
            :items="filter"
            label="Filtrer par..."
            outline
            ></v-select>
            </v-flex>
            <v-flex xs4>
                <v-select
            v-model="selectedID"
            :items="selectedFilter == 'Service ID' ? filterID : selectedFilter == 'Gateway' ? filterGateway : []"
            label="Id, Type..."
            outline
            ></v-select>
                </v-flex>
                <v-flex xs12>
                <v-divider></v-divider>
                </v-flex>
    <Service v-for="service in filteredServices" :key="service.id" v-bind:id="service.id"></Service>
    </v-layout>
      </v-container>
</template>


<script>
import Service from './Service.vue'
import { mapState, mapGetters } from 'vuex'

export default {
    data() {
        return {
            filter : ['', 'Service ID', 'Gateway'],
            selectedFilter : '',
            selectedID: '',
        }
    },
    components: {
        Service
    },
    computed: {
        ...mapState(['services', 'gateways']),
        ...mapGetters(['getServicesByServiceID', 'getServicesByType', 'getServicesFilteredbyGateway']),

        filteredServices () {
            switch (`${this.selectedFilter} ${this.selectedID}`) {
                case `Service ID ${this.selectedID}`:
                    return this.getServicesByServiceID(this.selectedID)
                    break;
                case this.selectedID !== '' && `Gateway ${this.selectedID}`:
                    return this.getServicesFilteredbyGateway(this.selectedID)
                    break;
                default:
                    return this.services
            }
        },
        filterID () {
            return this.services.reduce((accumulator, currentValue) => {
                if (accumulator.indexOf(currentValue.service_id) == -1) {
                    accumulator.push(currentValue.service_id)
                }
                return accumulator
            }, [''])
        },
        filterType () {
            return this.services.reduce((accumulator, currentValue) => {
                if (accumulator.indexOf(currentValue.type) == -1) {
                    accumulator.push(currentValue.type)
                }
                return accumulator
            }, [''])
        },
        filterGateway () {
            return this.gateways.reduce((accumulator, currentValue) => {
                if (accumulator.indexOf(currentValue.gateway_id) === -1) {
                    accumulator.push(currentValue.gateway_id)
                }
                return accumulator
            }, [''])
        }
    },
}
</script>


<style lang="scss" scoped>

</style>
