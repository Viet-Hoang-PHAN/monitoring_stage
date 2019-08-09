<template>
    <div class="navigation">
<v-list-group class="grey--text text--darken-4"
          v-for="site in sites" :key="site.id">
          <template v-slot:activator>
            <v-list-tile :to="{ name: 'site-detail', params: { id_site: site.id }}"
                          v-bind:id="site.id">
            <v-list-tile-action>
              <v-icon>account_circle</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title> {{site.name}} </v-list-tile-title>
            </v-list-tile-content>
            </v-list-tile>
          </template>
          <v-list-group sub-group
            v-for="vm in filterByID(vms, site.id)" :key="vm.id" 
          >
            <template v-slot:activator>
              <v-list-tile class="pl-1"
                    :to="{ name: 'vm-detail', params: { id_vm: vm.id, id_site: site.id }}">
                <v-list-tile-title>{{vm.name}}</v-list-tile-title>
              </v-list-tile>
            </template>
            <v-list-group sub-group
            v-for="gateway in filterByID(gateways, vm.id)" :key="gateway.id" 
          >
            <template v-slot:activator>
              <v-list-tile class="pl-2"
                    :to="{ name: 'gateway-detail', params: { id_vm: vm.id, id_site: site.id, id_gw: gateway.id }}">
                <v-list-tile-title>Gateway : {{ gateway.gateway_id }}</v-list-tile-title>
              </v-list-tile>
            </template>
            <v-list
            v-for="(terminal, indexTm) in filterByID(terminals, gateway.id)" :key="indexTm"
          >
              <v-list-tile class="pl-3"
                    :to="{ name: 'terminal-detail', params: { id_vm: vm.id,
                                                                id_site: site.id,
                                                                id_gw: gateway.id,
                                                                id_tm: terminal.id }}">
                <v-list-tile-title class="grey--text text--darken-4">Terminal : {{ terminal.terminal_id}}</v-list-tile-title>
              </v-list-tile>
          </v-list>
          </v-list-group>
          </v-list-group>
        </v-list-group>
    </div>
</template>


<script>
import { mapState } from 'vuex'
export default { 
  computed: {
    ...mapState(['sites', 'vms', 'gateways', 'terminals', 'services']),
  },
  methods: {
    getForeignKey (object) {
      for (let key in object) {
        if (key.match(/\w{1,4}_id/)){
          return object[key]
        }
      }
    },
    filterByID (datas, primaryKey) {
      return datas.filter( (data) => {
        return this.getForeignKey(data) == primaryKey
      })
    },
  }
}
</script>


<style lang="scss" scoped>

</style>
