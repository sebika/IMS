<script setup>
  import { ref } from 'vue'
  import { useRoute } from 'vue-router'
  import { getAPI } from '@/helpers'

  const product = ref({})

  const route = useRoute();
  getAPI.get(`/computer_store/product/id/${route.params.id}`)
    .then(response => response.data)
    .then(data => {
      product.value = data
    })
</script>

<template>
  <div>
    <h1>{{ product.name }}</h1>
    <table class="table">
      <tbody>
        <tr><th scope="row">Brand</th><td>{{ product.brand }}</td></tr>
        <tr><th scope="row">Series</th><td>{{ product.series }}</td></tr>
      </tbody>
      <tbody v-if="product.category == 'cpu'">
        <tr><th scope="row">Architecture</th><td>{{ product.architecture }}</td></tr>
        <tr><th scope="row">Cores</th><td>{{ product.cores }}</td></tr>
        <tr><th scope="row">Clock speed</th><td>{{ product.clock_speed }} GHz</td></tr>
      </tbody>
      <tbody v-else-if="product.category == 'gpu'">
        <tr><th scope="row">Memory capacity</th><td>{{ product.memory_capacity }} GB</td></tr>
        <tr><th scope="row">Memory type</th><td>{{ product.memory_type }}</td></tr>
        <tr><th scope="row">Clock speed</th><td>{{ product.clock_speed }} GHz</td></tr>
      </tbody>
    </table>
  </div>
</template>