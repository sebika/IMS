import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import App from './App.vue'
import Main from './MainView.vue'
import Profile from './ProfileView.vue'
import About from './AboutView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Main },
    { path: '/profile', component: Profile },
    { path: '/about', component: About }
  ]
})

const app = createApp(App)

app.use(router)

app.mount('#app')
