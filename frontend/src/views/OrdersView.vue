<script setup>
    import { ref } from 'vue';
    import { useAuthStore } from '@/stores'
    import { getAPI } from '@/helpers';

    const authStore = useAuthStore();

    const orders = ref([]);
    getAPI.get('/computer_store/order/all/')
    .then(response => orders.value = response.data);

    async function deleteOrder(id) {
      const response = await getAPI.delete(`/computer_store/order/delete/${parseInt(id)}/`)
      if (response.status == 204) {
        orders.value = orders.value.filter(p => p.id != id)
      }
    }
</script>

<template>
    <div>
        <h1>Orders</h1>
        <br>
        <div v-for="order in orders" :key="order">
            <h2>Order {{ order.id }}</h2>
            <h5>Date: {{ order.date }}</h5>
            <h5>Shipping Address: {{ order.shipping_address }}</h5>
            <h5>Phone: {{ order.phone }}</h5>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Price</th>
                    </tr>
                </thead>
                <tbody v-for="p in order.products" :key="p">
                    <tr>
                        <td>{{ p.name }}</td>
                        <td>{{ p.quantity }}</td>
                        <td>{{ p.quantity * p.price }}</td>
                    </tr>
                </tbody>
            </table>
            <button @click="deleteOrder(order.id)" class="btn btn-outline-secondary" v-if="authStore.user && authStore.user.is_staff">Remove</button>
            <br>
        </div>
    </div>
</template>