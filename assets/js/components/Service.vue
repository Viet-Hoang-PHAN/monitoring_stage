<template>
<v-flex xs12 md6 lg3>
  <v-hover>
  <v-card flat slot-scope="{ hover }" :class="`elevation-${hover ? 8 : 2}`">
            <v-card-title class="display-1 font-weight-medium"> Service : {{service.service_id}}
                <v-spacer></v-spacer>
                <v-menu bottom left>
              <template v-slot:activator="{ on }">
                <v-btn
                  light
                  icon
                  v-on="on"
                >
                  <v-icon>settings</v-icon>
                </v-btn>
              </template>
  
              <v-list>
                <v-list-tile>
                  <ServiceEditForm v-bind:serviceDetails="service"></ServiceEditForm>
                </v-list-tile>
              </v-list>
            </v-menu>
            </v-card-title>
            <v-card-text>
                <v-list>
                    <template v-for="(value, propertyName) in service">
                      <div v-if="propertyName !== 'term_id'" :key="propertyName">
                    <v-list-tile>
                        <v-list-tile-content>{{propertyName}} : {{value}}</v-list-tile-content>
                    </v-list-tile>
                    <v-divider></v-divider>
                      </div>
                    </template>
                </v-list>
            </v-card-text>
        </v-card>
        </v-hover>
        </v-flex>

</template>


<script>
import ServiceEditForm from './forms/ServiceEditForm.vue'
import {mapGetters} from 'vuex'

export default {
    props: ['id'],
    components: {
        ServiceEditForm
    },
    computed: {
      ...mapGetters(['getServiceByID']),
      service () {
        return this.getServiceByID(this.id)
      }
    },
}
</script>


<style lang="scss" scoped>

</style>
