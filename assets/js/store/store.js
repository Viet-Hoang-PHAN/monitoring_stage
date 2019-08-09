import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

/**
 * 
 */
function initialState () {
    return {
        sites: [],
        vms: [],
        gateways: [],
        terminals: [],
        services: [],
        errorsServiceForm: [],
        loggedIn: false,
        currentTime: Math.floor((new Date).getTime()/1000)
    }
}

export default new Vuex.Store({
    plugins: [createPersistedState()],
    state: initialState,
    mutations: {
        resetState(state) {
            const s = initialState()
            Object.keys(s).forEach(key => {
                state[key] = s[key]
            })
        },
        setSites (state, site) {
            state.sites.push(site)
        },
        setVms (state, vm) {
            state.vms.push(vm)
        },
        setGateways (state, gateway) {
            state.gateways.push(gateway)
        },
        setTerminals (state, terminal) {
            state.terminals.push(terminal)
        },
        setServices (state, service) {
            state.services.push(service)
        },
        replaceService (state, newDataService) {
            let serviceIndex = state.services.findIndex( service => service.id == newDataService.id);
            state.errorsServiceForm = []
            Vue.set(state.services, serviceIndex, newDataService)
        },
        setError (state, errors) {
            state.errorsServiceForm = []
            errors.forEach((error) => state.errorsServiceForm.push(error))
        },
        resetErrorList(state) {
            state.errorsServiceForm = []
        },
        setToken (state, setToken) {
            state.loggedIn = true
            axios.defaults.headers.common['Authorization'] = `Bearer ${setToken}`
        }

    },
    actions: {
        checkLogin ({commit, dispatch}, logInfo) {
            return axios.post(
                '/api/token/obtain/',
            {
                username: logInfo.username,
                password: logInfo.password,
            },
            {
                headers: {'Content-Type': 'application/json',}
            })
            .then((response) => {
                localStorage.setItem('token', response.data.access)
                commit('setToken', response.data.access)
                dispatch('loadData')
            }).catch((error) => {
                console.log(error.response)
            })
        },
        reset ({commit}) {
            commit('resetState')
        },
        setHeader ({commit}) {
            commit('setToken', localStorage.getItem('token'))
        } ,
        closeForm({commit}) {
            commit('resetErrorList')
        },
        updateService ({commit}, service) {
            return axios.put(
                `/api/service/${service.id}/`,
                service,
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                }).then((response) => {
                    commit('replaceService', response.data)
            }).catch((error) => {
                let errorList = []
                for (let prop in error.response.data) {
                    errorList.push(`${prop} : ${error.response.data[prop][0]}`)
                }
                commit('setError', errorList)
            })
        },
        loadData ({commit}) {

            function getSites() {
                return axios.get('/api/site/');
            };

            function getVms() {
                return axios.get('/api/vm/');
            };

            function getGateways() {
                return axios.get('/api/gateway/');
            };

            function getTerminals() {
                return axios.get('/api/terminal/');
            };

            function getServices() {
                return axios.get('/api/service/');
            }

            axios.all([
                getSites(),
                getVms(),
                getGateways(),
                getTerminals(),
                getServices()
            ])
              .then(axios.spread((sites, vms, gateways, terminals, services) => {
                sites.data.data.forEach( site => commit('setSites', site));
                vms.data.data.forEach( vm => commit('setVms', vm));
                gateways.data.data.forEach( gateway => commit('setGateways', gateway));
                terminals.data.data.forEach( terminal => commit('setTerminals', terminal));
                services.data.data.forEach( service => commit('setServices', service))
              }))
        },

    },
    getters: {
        // Getters to check if the data exist before rendering the component
        checkIDSite: (state) => (id) => {
            return state.sites.some(site => site.id == id)
        },
        checkIDVm: (state) => (id) => {
            return state.vms.some(vm => vm.id == id)
        },
        checkIDGateway: (state) => (id) => {
            return state.gateways.some(gateway => gateway.id == id)
        },
        checkIDTerminal: (state) => (id) => {
            return state.terminals.some(terminal => terminal.id == id)
        },

        checkParams: (state, getters) => (params) => {
            switch (Object.keys(params).length) {
                case 1:
                    return getters.checkIDSite(params.id_site)
                case 2:
                    return getters.checkIDSite(params.id_site) && getters.checkIDVm(params.id_vm)
                case 3:
                    return getters.checkIDSite(params.id_site) && getters.checkIDVm(params.id_vm)
                        && getters.checkIDGateway(params.id_gw)
                case 4:
                    return getters.checkIDSite(params.id_site) && getters.checkIDVm(params.id_vm)
                    && getters.checkIDGateway(params.id_gw) && getters.checkIDTerminal(params.id_tm)
            }
        },


        // Get a data by ID
        getSiteByID: (state) => (id) => {
            return state.sites.find( site => site.id == id)
        },
        getVmByID: (state) => (id)=> {
            return state.vms.find( vm => vm.id == id)
        },
        getGatewayByID: (state) => (id)=> {
            return state.gateways.find( gateway => gateway.id == id)
        },
        getTerminalByID: (state) => (id)=> {
            return state.terminals.find( terminal => terminal.id == id)
        },
        getServiceByID: (state) => (id)=> {
            return state.services.find( service => service.id == id)
        },

        // Get a dataList filtered by ID
        getSiteVmsFilteredByID: (state) => (primaryKey) => {
            return state.vms.filter((vm) => vm.site_id == primaryKey)
        },
        getVmGatewaysFilteredByID: (state) => (primaryKey) => {
            return state.gateways.filter((gateway) => gateway.vm_id == primaryKey)
        },
        getGatewayTerminalsFilteredByID: (state) => (primaryKey) => {
            return state.terminals.filter((terminal) => terminal.gw_id == primaryKey)
        },
        getTerminalServicesFilteredByID: (state) => (primaryKey) => {
            return state.services.filter((service) => service.term_id == primaryKey)
        },

        // Getters for the AllServices.vue search filter
        getServicesByServiceID: (state) => (service_id) => {
            return state.services.filter((service) => service.service_id == service_id)
        },
        getServicesByType: (state) => (type) => {
            return state.services.filter((service) => service.type == type)
        },
        getServicesFilteredbyGateway: (state, getters) => (id) => {
            let gateway = state.gateways.find( gateway => gateway.gateway_id == id);
            let terminals = getters.getGatewayTerminalsFilteredByID(gateway.id);
            return state.services.filter(service => {
                return terminals.some((terminal) => terminal.id == service.term_id)
            }
        )}, 

        getCurrentTime: (state) => (lastMsg) => {
            const message = 'Last message : '
            const minute = 60
            const hour = minute * 60
            const day = hour*24
            let currentTimeInSec = Math.abs(Math.round(lastMsg) - state.currentTime)
            if (Math.round(currentTimeInSec/minute) < 60) {
                let currentTimeInMinute = Math.round(currentTimeInSec/minute)
                return `${message+currentTimeInMinute} minutes ago...`
            }
            else if (Math.round(currentTimeInSec/hour) < 24) {
                let currentTimeInHours = Math.round(currentTimeInSec/hour)
                return `${message+currentTimeInHours} hours ago...`
            }
            else if (Math.round(currentTimeInSec/day) > 0) {
                let currentTimeInDays = Math.round(currentTimeInSec/day)
                return `${message+currentTimeInDays} days ago...`
            }
            else {
                return `${message+currentTimeInSec} secondes ago...`
            }
        }
    }
})