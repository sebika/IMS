<script setup>
  import { ref } from 'vue'
  import { getAPI, router } from '@/helpers'

  const cartProducts = ref([])
  const sum = ref(0)

  getAPI.get('/computer_store/cart/all/')
    .then(response => {
      return response
    })
    .then(response => {
      cartProducts.value = response.data
    })

    async function deleteFromCart(id) {
      const response = await getAPI.delete(`/computer_store/cart/delete/${id}`)
      if (response.status == 204) {
        cartProducts.value = cartProducts.value.filter(p => p.cart_product_id != id)
      }
    }

</script>

<template>
  <div>
    <h1>Cart</h1>
    <table class="table">
      <thead>
        <tr><th scope="col">Name</th><th scope="col">Quantity</th><th scope="col">Price</th></tr>
      </thead>
      <tbody v-for="p in cartProducts" :key="p">
        <tr>
          <td>{{ p.name }}</td>
          <td>{{ p.quantity }}</td>
          <td>{{ p.quantity * p.price }}</td>
          <button @click="deleteFromCart(p.cart_product_id)" class="btn btn-outline-secondary">Remove</button>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-primary" v-if="cartProducts.length > 0" @click="router.push('/cart/checkout/')">Checkout</button>
  </div>
</template>