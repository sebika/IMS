import { defineStore } from 'pinia'
import { router, getAPI } from '@/helpers'
import VueJwtDecode from 'vue-jwt-decode';


export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    // initialize state from local storage to enable user to stay logged in
    user: JSON.parse(localStorage.getItem('user')),
    returnUrl: null
  }),
  getters: {
    accessToken: (state) => state.user.access
  },
  actions: {
    async register(email, password, first_name, last_name) {
      const response = await getAPI.post('/computer_store/register/', {
        email: email,
        password: password,
        first_name: first_name,
        last_name: last_name
      })
      if (response.status === 201)
        router.push('/login')
      else if (response.status === 400)
        console.log(response.data)
    },
    async login(email, password) {
      const response = await getAPI.post('/computer_store/token/', {
        email: email,
        password: password
      })

      // update pinia state
      this.user = response.data;
      this.user.is_staff = VueJwtDecode.decode(this.user.access).is_staff;

      // store user details and jwt in local storage to keep user logged in between page refreshes
      localStorage.setItem('user', JSON.stringify(this.user));

      // redirect to previous url or default to home page
      router.push(this.returnUrl || '/');
    },
    logout() {
      this.user = null;
      localStorage.removeItem('user');
      // router.push('/login');
    }
  }
})