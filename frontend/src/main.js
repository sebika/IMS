import { createApp } from 'vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import { store } from '@/stores'
import { router } from '@/helpers';

import App from './App.vue'


const app = createApp(App)

app.use(store);
app.use(router);

router.isReady().then(() => {
  app.mount("#app");
});
