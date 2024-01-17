<script setup>
  import { useAuthStore } from '@/stores'
  import { getAPI } from '@/helpers'

  const props = defineProps({
    'id': Number,
    'name': String,
    'price': Number,
    'deleteProduct': Function,
  })

  const authStore = useAuthStore();
</script>

<template>
    <div class="card">
      <router-link :to="{ name: 'product', params: { id: props.id } }">
        <div class="card-body">
          <h5 class="card-title">{{ props.name }}</h5>
        </div>
      </router-link>
      <div class="card-footer">
        <div class="col-2 float-start">
            <button @click="deleteProduct(props.id)" class="btn btn-outline-secondary" v-if="authStore.user && authStore.user.is_staff">Remove</button>
        </div>
        <div class="col-2 float-end">
            {{ props.price }} lei
        </div>
      </div>
    </div>
</template>