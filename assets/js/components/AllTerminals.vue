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
            :items="selectedFilter == 'Gateway' ? filterGateway : selectedFilter == 'Type Service' ? filterType : selectedFilter == 'Gateway' ? filterGateway : []"
            label="Id, Type..."
            outline
            ></v-select>
                </v-flex>
                <v-flex xs12>
                <v-divider></v-divider>
                </v-flex>
        <v-flex xs12 md6 lg3 v-for="terminal in filteredTerminals" :key="terminal.id">
  <v-hover>
  <v-card flat slot-scope="{ hover }" :class="`elevation-${hover ? 8 : 2}`">
      <v-card-text>
          <v-card-title>
              Terminal : {{terminal.terminal_id}}
          </v-card-title>
        <v-list>
                    <template v-for="(value, propertyName, index) in terminal">
                        <div v-if="propertyName !== 'terminal_id' && propertyName !== 'last_msg'" :key="index">
                    <v-list-tile>
                        <v-list-tile-content>{{propertyName}} : {{value}}</v-list-tile-content>
                    </v-list-tile>
                    <v-divider></v-divider>
                        </div>
                    </template>
                    <small>{{time(terminal.last_msg)}}</small>
                </v-list>
      </v-card-text>
              </v-card>
        </v-hover>
        </v-flex>
    </v-layout>
      </v-container>
      
</template>

<script>
import {mapState, mapGetters} from 'vuex'

export default {
    data () {
        return {
            filter: ['', 'Gateway'],
            selectedFilter: '',
            selectedID: ''
        }
    },
    computed: {
        ...mapState(['terminals', 'gateways',]),
        ...mapGetters(['getCurrentTime']),
        filteredTerminals () {
            switch (`${this.selectedFilter} ${this.selectedID}`) {
                case this.selectedID !== '' && `Gateway ${this.selectedID}`:
                    let gateway = this.gateways.find((gateway) => gateway.gateway_id == this.selectedID)
                    return this.terminals.filter((terminal) => terminal.gw_id == gateway.id)
                default:
                    return this.terminals
            }
        },
        filterGateway () {
            return this.gateways.reduce((accumulator, currentValue) => {
                if (accumulator.indexOf(currentValue.gateway_id) === -1) {
                    accumulator.push(currentValue.gateway_id)
                }
                return accumulator
            }, [''])
        },
    },
    methods: {
        time(lastMsg) {
            return this.getCurrentTime(lastMsg)
        }
    }
    
}
</script>


<style lang="scss" scoped>

</style>
