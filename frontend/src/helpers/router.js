import { createRouter, createWebHistory } from 'vue-router';

import { useAuthStore } from '@/stores';
import { HomeView, RegisterView, LoginView, ProductView, AddProductView, ProfileView, AboutView, CartView, CheckoutView } from '@/views';


export const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    linkActiveClass: 'active',
    routes: [
        { path: '/',                                    component: HomeView },
        { path: '/register/',                           component: RegisterView },
        { path: '/login/',                              component: LoginView },
        { path: '/product/:id/',    name: 'product',    component: ProductView },
        { path: '/product/add/',                        component: AddProductView },
        { path: '/profile/',                            component: ProfileView },
        { path: '/about/',                              component: AboutView },
        { path: '/cart/',                               component: CartView },
        { path: '/cart/checkout/',                      component: CheckoutView }
    ]
});

router.beforeEach(async (to) => {
    const auth = useAuthStore();
    const nonPublicPages = ['/profile'];
    const authRequired = nonPublicPages.includes(to.path);

    if (authRequired && !auth.user) {
        auth.returnUrl = to.fullPath;
        return '/login';
    }
});
