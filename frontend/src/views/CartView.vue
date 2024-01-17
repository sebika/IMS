<script setup>
  import { ref } from 'vue'
  import { getAPI } from '@/helpers'

  const products = ref([])
  // console.log('fdsfsad')

  getAPI.get('/computer_store/cart/all/')
    .then(response => {
      console.log(response)
      return response
    })
    .then(response => {
      console.log(response.data)
      products.value = response.data
    })
    // .then(response => products.value = response.data)
    .then(() => {
      console.log(products.value)
    })
</script>

<template>
  <div>
    <h1>Cart</h1>
    <table class="table">
      <thead>
        <tr><th scope="col">Name</th><th scope="col">Quantity</th><th scope="col">Price</th></tr>
      </thead>
      <tbody v-for="p in products" :key="p">
        <tr>
          <td>{{ p.name }}</td>
          <td>{{ p.quantity }}</td>
          <td>{{ p.quantity * p.price }}</td>
          <button class="btn btn-outline-secondary">Remove</button>
        </tr>
      </tbody>
    </table>
  </div>
</template>