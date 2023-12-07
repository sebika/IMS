<script setup>
  import { ref } from 'vue'
  import Item from './ProductItem.vue'

  // async function getData() {
  //   const products = []

  //   const response = await fetch('http://localhost:8000/computer_store', {
  //     method: 'GET',
  //   })

  //   const data = await response.json()
  //   console.log(Array.isArray(data.response))
  //   console.log(data.response.length)

  //   for (let i = 0; i < data.response.length; i++) {
  //     const comp = data.response[i]
  //     products.value.push(comp.name)
  //     console.log(products)
  //   }

  //   return products
  // }

  const products = ref(null)
  const row_indeces = ref(null)
  const extra_row = ref(null)

  fetch('http://localhost:8000/computer_store', {
    method: 'GET',
  }).then(response => response.json())
    .then(data => data.response.map(comp => comp.name))
    .then(data => products.value = data)
    .then(() => {
      extra_row.value = ((products.value.length % 3) ? 1 : 0);
      row_indeces.value = Array.from(Array(Math.floor(products.value.length/3+extra_row.value)).keys())
    })


  // const extra_row = ((products.value.length % 3) ? 1 : 0);
  // const row_indeces = Array.from(Array(Math.floor(products.value.length/3+extra_row)).keys())
</script>

<template>
  <div class="container-fluid">
    <div v-for="row_i in row_indeces" :key="row_i" class="row">
      <div v-for="p in products.slice(row_i*3, row_i*3+3)" :key="p" class="col-xs-4 col-sm-4 col-md-4 col-lg-4">
        <Item :name="p"/>
      </div>
    </div>
  </div>

  <nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
</template>
