<script setup>
    import { Field } from 'vee-validate';

    const props = defineProps({
        'label': String,
        'type': String,
        'error': String,
        'name': String,
    })
</script>

<template>
    <div class="form-group">
        <label>{{ props.label }}</label>
        <Field :name="props.name" :type="props.type" class="form-control" :class="{ 'is-invalid': props.error }" />
        <div class="invalid-feedback">{{ props.error }}</div>
    </div>
</template>