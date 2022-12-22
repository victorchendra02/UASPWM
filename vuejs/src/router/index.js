import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Payment from "../views/Payment.vue";
import ReportSale from "../views/ReportSale.vue";
import Login from "../views/Login.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "login",
            component: Login,
        },
        {
            path: "/dashboard",
            name: "dashboard",
            component: Dashboard,
        },
        {
            path: "/payyy",
            name: "payment",
            component: Payment,
        },
        {
            path: "/report",
            name: "report",
            component: ReportSale,
        },
    ],
});

export default router;
