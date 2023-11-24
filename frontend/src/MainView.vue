<script setup>
  import Item from './ProductItem.vue'

  const products = [
    'Nvidia GeForce RTX 3070',
    'Nvidia GeForce RTX 3080',
    'Nvidia GeForce RTX 3090',
    'AMD Radeon RX 6800',
    'AMD Radeon RX 6800 XT',
    'AMD Radeon RX 6900 XT',
    'AMD Radeon RX 6700 XT'
  ]

  const extra_row = ((products.length % 3) ? 1 : 0);
  const row_indeces = Array.from(Array(Math.floor(products.length/3+extra_row)).keys())
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
