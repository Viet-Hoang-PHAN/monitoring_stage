<template>
  <v-app id="inspire">
    <div v-if="!loggedIn">
      <Login />
    </div>
    <div v-else>

    
    <!-- Start Topbar -->
    <v-toolbar class="toolbar grey--text text--darken-4" app>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>MISNet - Fleet Monitoring</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text flat @click="logout()">Logout</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <!-- End Topbar -->
    
    <!-- Start Navigation Bar -->
    <v-navigation-drawer class="navigation-bg" dark app v-model="drawer">
      <v-layout row wrap>
        <v-flex xs12 ma-auto>

          <!-- Start Basic Menu -->
          <v-list dense class="pm-0 grey--text text--darken-4">
            <v-list-tile v-for="link in links" :key="link.title" :to="link.path">
              <v-list-tile-action>
                <v-icon>{{ link.icon }}</v-icon>
              </v-list-tile-action>

              <v-list-tile-content>
                <v-list-tile-title>{{ link.title }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>

            <!-- Start Collapsible Tree Menu -->
            <Navigation />
        <!-- End Collapsible Tree Menu -->
          </v-list>
          <!-- End Basic Menu -->

        </v-flex>
      </v-layout>
    </v-navigation-drawer>

    <!-- End Navigation Bar -->

    <v-content>
        <transition name="slide-fade">
          <router-view></router-view>
        </transition>
    </v-content>
    </div>
  </v-app>
</template>


<script>
import axios from 'axios'

import Navigation from './components/Navigation.vue'
import Login from './components/Login.vue'
import { mapState, mapActions } from 'vuex';

export default {
  name: "app",
  components: {
    Navigation,
    Login
  },
  props: ['id_site', 'id_vm', 'id_gw', 'id_tm', 'id_sv'],
  data() {
    return {
      depth: 1,
      drawer: false,
      links: [
        { icon: "dashboard", title: "Dashboard", path: "/" },
        { icon: "perm_data_setting", title: "All services", path: "/all-services" },
        { icon: "devices_other", title: "All terminals", path: "/all-terminals" },
      ]
    };
  },
  computed: {
    ...mapState(['loggedIn']),
  },
  methods: {
    ...mapActions(['reset']),
    logout () {
      localStorage.removeItem('token')
      localStorage.removeItem('vuex')
      this.$store.state.loggedIn = false
      this.$router.push({name: 'login'})
      this.reset()
    }
  }
  
};
</script>

<style lang="scss" scoped>
.toolbar, .navigation-bg {
  background: linear-gradient(135deg, #1E88E5, white, #FFA000);
}

.slide-fade-enter-active {
  transition: all 0.2s 0.4s ease;
}
.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
