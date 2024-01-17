<script setup>
  import { ref } from 'vue'
  import { getAPI } from '@/helpers'
  import Item from './ProductItem.vue'
  import * as Notify from 'notifyjs'

  const products = ref([])
  const row_indeces = ref([])
  const extra_row = ref(0)

  getAPI.get('/computer_store/product/all/')
    .then(response => products.value = response.data)
    .then(() => {
      extra_row.value = ((products.value.length % 3) ? 1 : 0);
      row_indeces.value = Array.from(Array(Math.floor(products.value.length/3+extra_row.value)).keys())
    })

  function showNotification() {
    const notification = new Notify('Product deleted', {
        body: 'Product deleted successfully!',
      })
      notification.show()
  }

  async function deleteProduct(id) {
    const response = await getAPI.delete('/computer_store/product/delete/' + id + '/')
    if (response.status == 204) {
      products.value = products.value.filter(p => p.id != id)
      extra_row.value = ((products.value.length % 3) ? 1 : 0);
      row_indeces.value = Array.from(Array(Math.floor(products.value.length/3+extra_row.value)).keys())
      if (Notify.needsPermission && Notify.isSupported())
        Notify.requestPermission(showNotification)
      else
        showNotification()
    }
  }
</script>

<template>
  <div class="container-fluid">
    <div v-for="row_i in row_indeces" :key="row_i" class="row">
      <div v-for="p in products.slice(row_i*3, row_i*3+3)" :key="p" class="col-xs-4 col-sm-4 col-md-4 col-lg-4">
        <Item :id="p.id" :name="p.name" :price="p.price" :deleteProduct="deleteProduct"/>
      </div>
    </div>
  </div>

  <!-- <nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav> -->
</template>
