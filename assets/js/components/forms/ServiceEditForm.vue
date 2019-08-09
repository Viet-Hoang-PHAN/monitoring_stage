<template>
    <v-dialog v-model="dialog" persistent max-width="900px">
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" depressed flat class="ma-0 pa-0">Configure</v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="headline">Configuration of Service : {{serviceDetails.service_id}}</span>
          </v-card-title>
          <v-card-text>
            <form>
            <v-container grid-list-md>
              <v-layout wrap>
                <!-- Input for the attributes we want to modify -->
                <v-flex xs12 sm6 md4>
                  <v-text-field label="service_id" v-model.number="dataService.service_id"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="channel" v-model.number="dataService.channel"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="label" v-model="dataService.label"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="type_trigger" v-model.number="dataService.type_trigger"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="datatype" v-model.number="dataService.datatype"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="subsample_rate" v-model.number="dataService.subsample_rate"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="high_threshold" v-model.number="dataService.high_threshold"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="low_threshold" v-model.number="dataService.low_threshold"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="delta" v-model.number="dataService.delta"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6>
                  <v-switch :label="`${dataService.enable === true ? 'Enabled' : 'Disabled'}`" v-model="dataService.enable"></v-switch>
                </v-flex>
                <v-flex xs12 sm6>
                  <v-switch :label="`Interruption : ${dataService.interruption === true ? 'Yes' : 'No'}`" v-model="dataService.interruption"></v-switch>
                </v-flex>
              </v-layout>
            </v-container>
             </form>
             <div v-if="errors.length !== 0">
            <v-alert :value="true" type="error">
              <small v-for="(error, index) in errors" :key="index" class="white--text">{{ error }}  <br /></small>
            </v-alert>
             </div>
             <div v-else-if="isEdited">
               <v-alert :value="true" type="success"><small class="white--text">Le service a bien été modifié</small></v-alert>
             </div>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="close()">Close <v-icon>clear</v-icon></v-btn>
            <v-btn color="blue darken-1" flat @click="update">Save <v-icon>done</v-icon></v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
</template>



<script>
import axios from 'axios'
import { setTimeout } from 'timers';
import { mapState, mapActions } from 'vuex';

export default {
  props: ['serviceDetails'],
  data () {
        return {
            dialog: false,
            edited: false,
            dataService: {
              id: this.serviceDetails.id,
              gw_id: this.serviceDetails.gw_id,
              term_id: this.serviceDetails.term_id,
              service_id: this.serviceDetails.service_id,
              channel: this.serviceDetails.channel,
              label: this.serviceDetails.label,
              enable: this.serviceDetails.enable,
              interruption: this.serviceDetails.interruption,
              type_trigger: this.serviceDetails.type_trigger,
              datatype: this.serviceDetails.datatype,
              subsample_rate: this.serviceDetails.subsample_rate,
              high_threshold: this.serviceDetails.high_threshold,
              low_threshold: this.serviceDetails.low_threshold,
              delta: this.serviceDetails.delta,
              request_status: this.serviceDetails.delta,
              version: this.serviceDetails.version
            }
        }
    },
    computed: {
      ...mapState(['errorsServiceForm']),
        errors() {
          return this.errorsServiceForm
        },
        isEdited() {
          return this.edited
        }
    },
    methods: {
      ...mapActions(['updateService', 'closeForm']),
      async update() {
        await this.updateService(this.dataService)
        if (this.errorsServiceForm.length === 0) {
          this.edited = true;
          setTimeout( () => {
            this.dialog = false;
            this.edited = false;
          }, 1500)
        }
      },
      close() {
        this.closeForm()
        this.dialog = false
      },
    }, 
}
</script>


<style lang="scss" scoped>

</style>
