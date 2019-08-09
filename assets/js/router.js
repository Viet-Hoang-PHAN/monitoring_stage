import Vue from 'vue';
import VueRouter from 'vue-router';
import store from './store/store';

// import Dashboard from "./components/Dashboard.vue";
// import Site from "./components/Site.vue";
// import VM from "./components/VM.vue";
// import Gateway from "./components/Gateway.vue";
// import Terminal from "./components/Terminal.vue";
// import AllServices from "./components/AllServices.vue";
// import AllTerminals from "./components/AllTerminals.vue";

const Dashboard = () => import('./components/Dashboard.vue');
const Site = () => import('./components/Site.vue');
const VM = () => import('./components/VM.vue');
const Gateway = () => import('./components/Gateway.vue');
const Terminal = () => import('./components/Terminal.vue');
const AllServices = () => import('./components/AllServices.vue');
const AllTerminals = () => import('./components/AllTerminals.vue');
const ErrorPage = () => import('./components/ErrorPage.vue')
const Login = () => import('./components/Login.vue')

Vue.use(VueRouter)

export const router = new VueRouter ({
    routes:  [
        {
            path: '/login',
            name: 'login',
            component: Login,
            beforeEnter(to, from, next) {
                if (store.state.loggedIn) {
                    next({name: 'home'})
                }
            }
        },
        {
            path: '/',
            name: 'home',
            component: Dashboard,
            meta: { requiresAuth: true }
        },
        {
            path: '/site/:id_site/vm/',
            name: 'site-detail',
            props: true,
            component: Site,
            meta: { requiresAuth: true },
            beforeEnter(to, from, next) {
                if (store.getters.checkParams(to.params)) {
                    next()
                }
                else {
                    next({
                        name: 'error'
                    })
                }
            },
        },
        {
            path: '/site/:id_site/vm/:id_vm/gateway/',
            name: 'vm-detail',
            props: true,
            component: VM,
            meta: { requiresAuth: true },
            beforeEnter(to, from, next) {
                if (store.getters.checkParams(to.params)) {
                    next()
                }
                else {
                    next({
                        name: 'error'
                    })
                }
            },
        },
        {
            path: '/site/:id_site/vm/:id_vm/gateway/:id_gw/terminal/',
            name: 'gateway-detail',
            props: true,
            component: Gateway,
            meta: { requiresAuth: true },
            beforeEnter(to, from, next) {
                if (store.getters.checkParams(to.params)) {
                    next()
                }
                else {
                    next({
                        name: 'error'
                    })
                }
            },
        },
        {
            path: '/site/:id_site/vm/:id_vm/gateway/:id_gw/terminal/:id_tm/service/',
            name: 'terminal-detail',
            props: true,
            component: Terminal,
            meta: { requiresAuth: true },
            beforeEnter(to, from, next) {
                if (store.getters.checkParams(to.params)) {
                    next()
                }
                else {
                    next({
                        name: 'error'
                    })
                }
            },
        },
        {
            path: '/all-terminals',
            name: 'all-terminals',
            meta: { requiresAuth: true },
            component: AllTerminals
        },
        {
            path: '/all-services',
            name: 'all-services',
            meta: { requiresAuth: true },
            component: AllServices,
        },
        {
            path: '/error',
            name: 'error',
            component: ErrorPage
        },
        {
            path: '*',
            redirect: 'error'
        }
    ],
    
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (!localStorage.getItem('token')) {
            next({
                name: 'login'
            })
        }
        else {
            store.dispatch('setHeader')
            next()
        }
    }
    else {
        next()
    }
})

export default router