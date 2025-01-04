import axios from 'axios'
import { useAuthStore } from '@/stores'

const getAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    timeout: 1000,
})
getAPI.interceptors.request.use(function (config) {
    const authStore = useAuthStore()
    if (authStore.user) {
        // console.log(config.url)
        // if (config.url != "/computer_store/token/" && config.url != "/computer_store/token/refresh/")
        config.headers.Authorization = `Bearer ${authStore.accessToken}`;
    }

    return config;
})

// getAPI.interceptors.response.use(
//     (res) => {
//       return res;
//     },
//     async (err) => {
//       const authStore = useAuthStore()
//       const originalConfig = err.config;
//       console.log("1")
//       if (originalConfig.url !== "/computer_store/register/" && originalConfig.url !== "/computer_store/token/" && err.response) {
//         console.log(err.response)
//         // Access Token was expired
//         if (err.response.status === 401 && !originalConfig._retry) {
//           originalConfig._retry = true;
//           console.log("3")
//           try {
//             const rs = await getAPI.post("/computer_store/token/refresh/")
//             // , {
//             //   refreshToken: authStore.refreshToken,
//             // });

//             const { accessToken } = rs.data;
//             console.log(rs)

//             authStore.updateAccessToken(accessToken);
//             // store.dispatch('auth/refreshToken', accessToken);
//             // TokenService.updateLocalAccessToken(accessToken);

//             return getAPI(originalConfig);
//           } catch (_error) {
//             // router.go('/logout')
//             return Promise.reject(_error);
//           }
//         }
//       }

//       return Promise.reject(err);
//     }
// )

export { getAPI }
