<template>
    <div>
        <NavBar />
        <div class="container-fluid text-center p-4">
            <div class="row">
                <!-- Kiri -->
                <div class="col-3 border-end border-1 border-danger pe-0">
                    <HeaderInvoice />
                    <InvoiceBody />
                    <!-- <Commands /> -->
                </div>

                <!-- Kanan -->
                <div class="col-9 border-start border-1 border-danger ps-0">
                    <CategoryProduct />
                    <AdminCommands />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import CategoryProduct from "@/components/CategoryProduct.vue";
import AdminCommands from "@/components/AdminCommands.vue";

import HeaderInvoice from "@/components/HeaderInvoice.vue";
import InvoiceBody from "@/components/InvoiceBody.vue";
// import Commands from "@/components/Commands.vue";

export default {
    name: "Dashboard",
    components: {
        NavBar,
        CategoryProduct,
        AdminCommands,
        HeaderInvoice,
        InvoiceBody,
        // Commands,
    },
    methods: {
        chek() {
            if (window.localStorage.getItem("clerk") === null) {
                this.$router.push({
                    path: "/",
                });
            }
        },
    },
    created() {
        this.chek();
    },
};
</script>

<style></style>
