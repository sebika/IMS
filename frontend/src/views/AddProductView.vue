<script setup>
  import { ref } from 'vue'
  import { Form, Field } from 'vee-validate';
  import { getAPI } from '@/helpers'

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
        clockSpeed: clockSpeed
      }
    })
  }

  async function onSubmit(values, { setErrors }) {
    if (category.value == 'cpu') {
      await cpuSubmit(values, { setErrors })
    }
  }
</script>

<template>
  <div>
    <Form @submit="onSubmit" v-slot="{ errors, isSubmitting }">
        <div class="form-group">
          <label>Name</label>
          <Field name="name" type="text" class="form-control" :class="{ 'is-invalid': errors.name }" />
          <div class="invalid-feedback">{{errors.name}}</div>
        </div>
        <div class="form-group">
          <label>Brand</label>
          <Field name="brand" type="text" class="form-control" :class="{ 'is-invalid': errors.brand }" />
          <div class="invalid-feedback">{{errors.brand}}</div>
        </div>
        <div class="form-group">
          <label>Series</label>
          <Field name="series" type="text" class="form-control" :class="{ 'is-invalid': errors.series }" />
          <div class="invalid-feedback">{{errors.series}}</div>
        </div>
        <div class="form-group">
          <label>Price</label>
          <Field name="price" type="text" class="form-control" :class="{ 'is-invalid': errors.price }" />
          <div class="invalid-feedback">{{errors.price}}</div>
        </div>

        <Field name="category" as="select" v-model="category">
          <option value="cpu">CPU</option>
          <option value="gpu">GPU</option>
        </Field>

        <div class="form-group" v-if="category == 'cpu'">
          <label>Architecture</label>
          <Field name="architecture" type="text" class="form-control" :class="{ 'is-invalid': errors.architecture }" />
          <div class="invalid-feedback">{{errors.architecture}}</div>
        </div>
        <div class="form-group" v-if="category == 'cpu'">
          <label>Cores</label>
          <Field name="cores" type="text" class="form-control" :class="{ 'is-invalid': errors.cores }" />
          <div class="invalid-feedback">{{errors.cores}}</div>
        </div>
        <div class="form-group" v-if="category == 'cpu'">
          <label>Clock speed</label>
          <Field name="clockSpeed" type="text" class="form-control" :class="{ 'is-invalid': errors.clockSpeed }" />
          <div class="invalid-feedback">{{errors.clockSpeed}}</div>
        </div>

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