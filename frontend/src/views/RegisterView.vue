<script setup>
import { Form, Field } from 'vee-validate';
import { useAuthStore } from '@/stores';

function onSubmit(values, { setErrors }) {
  const authStore = useAuthStore();
  const { email, first_name, last_name, password } = values;

  return authStore.register(email, password, first_name, last_name)
      .catch(error => setErrors({ apiError: error }));
}
</script>

<template>
  <div>
    <div class="alert alert-info">
      Email: user1@example.com<br />
      Password: password
    </div>
    <h2>Login</h2>
    <Form @submit="onSubmit" v-slot="{ errors, isSubmitting }">
      <div class="form-group">
        <label>Email</label>
        <Field name="email" type="text" class="form-control" :class="{ 'is-invalid': errors.email }" />
        <div class="invalid-feedback">{{errors.email}}</div>
      </div>
      <div class="form-group">
        <label>First name</label>
        <Field name="first_name" type="text" class="form-control" :class="{ 'is-invalid': errors.first_name }" />
        <div class="invalid-feedback">{{errors.first_name}}</div>
      </div>
      <div class="form-group">
        <label>Last name</label>
        <Field name="last_name" type="text" class="form-control" :class="{ 'is-invalid': errors.last_name }" />
        <div class="invalid-feedback">{{errors.last_name}}</div>
      </div>
      <div class="form-group">
        <label>Password</label>
        <Field name="password" type="password" class="form-control" :class="{ 'is-invalid': errors.password }" />
        <div class="invalid-feedback">{{errors.password}}</div>
      </div>
      <div class="form-group">
        <button class="btn btn-primary" :disabled="isSubmitting">
          <span v-show="isSubmitting" class="spinner-border spinner-border-sm mr-1"></span>
          Register
        </button>
      </div>
      <div v-if="errors.apiError" class="alert alert-danger mt-3 mb-0">{{errors.apiError}}</div>
    </Form>
  </div>
</template>
