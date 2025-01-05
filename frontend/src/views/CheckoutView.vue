<script setup>

    import { Form } from 'vee-validate'
    import FormField from './FormField.vue'
    import { getAPI, router } from '@/helpers'
    import * as Notify from 'notifyjs'

    function showNotification() {
        const notification = new Notify('Order registered', {
            body: 'Your order was processed successfully!',
        })
        notification.show()
    }

    async function onSubmit(values, { setErrors }) {
        const { address, phone } = values
        const response = await getAPI.post('/computer_store/cart/checkout/', {
            address: address,
            phone: phone,
        })

        console.log(response)

        if (response.status == 200) {
            window.location = response.data.url
        } else {
            setErrors({ apiError: response.data.detail })
        }
    }

</script>

<template>
    <div>
        <Form @submit="onSubmit" v-slot="{ errors, isSubmitting }">
            <FormField label="Address" name="address" type="text" :error="errors.address" />
            <FormField label="Phone" name="phone" type="text" :error="errors.phone" />
            <div class="form-group">
                <button class="btn btn-primary" :disabled="isSubmitting">
                    <span v-show="isSubmitting" class="spinner-border spinner-border-sm mr-1"></span>
                    Order
                </button>
            </div>
            <div v-if="errors.apiError" class="alert alert-danger mt-3 mb-0">{{errors.apiError}}</div>
        </Form>
    </div>
</template>
