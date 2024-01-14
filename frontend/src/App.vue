<script setup>
  import { ref } from 'vue'
  import { useAuthStore } from '@/stores'
  import { getAPI, router } from '@/helpers'

  const authStore = useAuthStore();
  const categories = ref([])

  getAPI.get('/computer_store/categories/')
    .then(response => categories.value = response.data)
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-fixed-top bg-body-tertiary">
    <div class="container-fluid">
      <div class="col-3 d-flex">
        <router-link :to="{ path: '/'}"><img class="nav-item" src="/favicon.ico" alt="Computer Parts Store" width="40" height="40"></router-link>
        <div class="nav-item dropdown">
          <button class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Categories</button>
          <ul class="dropdown-menu">
            <li v-for="cat in categories"><a class="dropdown-item" @click="router.push('/')">{{ cat }}</a></li>
          </ul>
        </div>
      </div>
      <div class="col-3">
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-secondary" type="submit">Search</button>
        </form>
      </div>
      <!-- <button class="nav-item nav-link" @click="authAction" v-if="!authStore.user">Login</button> -->
      <div class="col-3">
        <div class="float-end d-flex">
          <router-link :to="{ path: '/product/add'}">
            <button class="btn btn-outline-secondary" type="submit" v-if="authStore.user && authStore.user.is_staff">Add product</button>
          </router-link>
          <div class="nav-item dropdown" v-if="authStore.user">
            <button class="btn btn-outline-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Profile</button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" @click="authStore.logout()">Logout</a></li>
            </ul>
          </div>
          <button class="nav-item btn btn-outline-secondary" @click="router.push('/login')" v-else>Login</button>
        </div>
      </div>
    </div>
  </nav>
  <div class="container pt-4 pb-4">
    <RouterView />
  </div>
</template>
