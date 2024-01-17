<script setup>
  import { ref } from 'vue'
  import { Form, Field } from 'vee-validate';
  import FormField from './FormField.vue';
  import { getAPI, router } from '@/helpers'

  const category = ref('')

  async function cpuSubmit(values, { setErrors }) {
    const { name, brand, series, price, architecture, cores, clockSpeed } = values
    await getAPI.post('/computer_store/product/add/', {
      category: category.value,
      data: {
        name: name,
        brand: brand,
        series: series,
        price: price,
        architecture: architecture,
        cores: cores,
        clockSpeed: clockSpeed,
      }
    })
  }

  async function gpuSubmit(values, { setErrors }) {
    const { name, brand, series, price, memory_capacity, memory_type, clock_speed } = values
    await getAPI.post('/computer_store/product/add/', {
      category: category.value,
      data: {
        name: name,
        brand: brand,
        series: series,
        price: price,
        memory_capacity: memory_capacity,
        memory_type: memory_type,
        clock_speed: clock_speed,
      }
    })
  }

  async function onSubmit(values, { setErrors }) {
    if (category.value == 'cpu')
      await cpuSubmit(values, { setErrors })
    else if (category.value == 'gpu')
      await gpuSubmit(values, { setErrors })
    router.push('/')
  }
</script>

<template>
  <div>
    <Form @submit="onSubmit" v-slot="{ errors, isSubmitting }">
        <FormField label="Name" name="name" type="text" :error="errors.name" />
        <FormField label="Brand" name="brand" type="text" :error="errors.brand" />
        <FormField label="Series" name="series" type="text" :error="errors.series" />
        <FormField label="Price" name="price" type="number" :error="errors.price" />

        <Field name="category" as="select" v-model="category">
          <option value="cpu">CPU</option>
          <option value="gpu">GPU</option>
        </Field>
        
        <FormField label="Architecture" name="architecture" type="text" :error="errors.architecture" v-if="category == 'cpu'"/>
        <FormField label="Cores" name="cores" type="number" :error="errors.cores" v-if="category == 'cpu'"/>
        <FormField label="Clock Speed" name="clockSpeed" type="number" :error="errors.clockSpeed" v-if="category == 'cpu'"/>

        <FormField label="Memory Capacity (GB)" name="memory_capacity" type="number" :error="errors.memory_capacity" v-if="category == 'gpu'"/>
        <FormField label="Memory Type" name="memory_type" type="text" :error="errors.memory_type" v-if="category == 'gpu'"/>
        <FormField label="Clock Speed" name="clock_speed" type="number" :error="errors.clock_speed" v-if="category == 'gpu'"/>

        <div class="form-group">
          <button class="btn btn-primary" :disabled="isSubmitting">
            <span v-show="isSubmitting" class="spinner-border spinner-border-sm mr-1"></span>
            Add
          </button>
        </div>
        <div v-if="errors.apiError" class="alert alert-danger mt-3 mb-0">{{errors.apiError}}</div>
      </Form>
  </div>
</template>