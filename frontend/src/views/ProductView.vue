<script setup>
  import { ref } from 'vue'
  import { useRoute } from 'vue-router'
  import { getAPI, router } from '@/helpers'
  import { useAuthStore } from '@/stores'
  import * as Notify from 'notifyjs'

  const product = ref({})
  const authStore = useAuthStore();
  const quantity = ref(1)

  function showNotification() {
        const notification = new Notify('Added to cart', {
            body: 'Your item was added successfully!',
        })
        notification.show()
    }

  const route = useRoute();
  getAPI.get(`/computer_store/product/id/${route.params.id}`)
    .then(response => response.data)
    .then(data => {
      product.value = data
    })

    async function addToCart() {
      const response = await getAPI.post('/computer_store/cart/add/', {
        product_id: route.params.id,
        quantity: quantity.value
      })

      if (response.status == 200) {
            if (Notify.needsPermission && Notify.isSupported())
                Notify.requestPermission(showNotification)
            else
                showNotification()
        } else {
            setErrors({ apiError: response.data.detail })
        }
    }
</script>

<template>
  <div>
    <h1>{{ product.name }}</h1>
    <table class="table">
      <tbody>
        <tr><th scope="row">Brand</th><td>{{ product.brand }}</td></tr>
        <tr><th scope="row">Series</th><td>{{ product.series }}</td></tr>
        <tr><th scope="row">Price</th><td>{{ product.price }} lei</td></tr>
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
  <div style="display: flex; gap: 10px;">
    <div>
      Quantity: <input type="number" v-model="quantity" min="1" />
    </div>
    <div>
      <button @click="addToCart" class="btn btn-primary">Add to Cart</button>
    </div>
  </div>
</template>