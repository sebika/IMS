import axios from 'axios'
import { useAuthStore } from '@/stores'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,
})
getAPI.interceptors.request.use(function (config) {
    const authStore = useAuthStore()
    if (authStore.user) {
        config.headers.Authorization = `Bearer ${authStore.accessToken}`;
    }

    return config;
})

export { getAPI }