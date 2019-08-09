<template>
<v-container fluid fill-height class="loginOverlay">
                    <v-layout flex align-center justify-center>
                        <v-flex xs12 sm4 elevation-6>
                            <v-toolbar class="pt-5 blue darken-4">
                                <v-toolbar-title class="white--text">
                                    <h3>MISNet</h3>
                                </v-toolbar-title>
                            </v-toolbar>
                            <v-card>
                                <v-card-text class="pt-4">
                                    <div>
                                        <form>
                                            <v-layout wrap>
                                                <v-flex xs12 v-if="!loggedIn">
                                                    <v-alert dense outlined :value="wrongUser" type="error">
                                                        Cet utilisateur n'existe pas</v-alert>
                                                </v-flex>
                                                <v-flex xs12>
                                                    <v-text-field label="Username" v-model="logInfo.username">
                                                        Username
                                                    </v-text-field>
                                                </v-flex>
                                                <v-flex xs12>
                                                    <v-text-field type="password" label="Password" v-model="logInfo.password">
                                                        Password
                                                    </v-text-field>
                                                </v-flex>
                                            </v-layout>
                                            <v-btn type="submit" @click.prevent="login()">Login</v-btn>
                                        </form>
                                    </div>
                                </v-card-text>
                            </v-card>
                        </v-flex>
                    </v-layout>
                </v-container>    
</template>


<script>
import { mapState, mapActions } from 'vuex';
export default {
    data() {
        return {
            logInfo: {
                username: '',
                password: '',
            },
            wrongUser: false
        }
    },
    computed: {
        ...mapState(['loggedIn'])
    },
    methods: {
        ...mapActions(['checkLogin']),
        async login() {
            await this.checkLogin(this.logInfo)
            if (this.loggedIn) {
                this.$router.push({name: 'home'})
            }
            else {
                this.wrongUser = true
            }
        }
    }
    
}
</script>


<style lang="scss" scoped>

</style>
