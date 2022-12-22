<template>
    <div>
        <NavBar />
        <div class="p-5">
            <ol>
                <li v-for="(x, index) in this.cart" :key="index">
                    <span class="me-3">{{ x.product_name }} </span>
                    <span class="me-4">{{ x.qty }}</span>
                    <span class="me-4">{{ x.price.toLocaleString("id-ID") }}</span>
                    <span class="me-4 fw-bold">Rp {{ x.sub_total.toLocaleString("id-ID") }}</span>
                </li>
            </ol>
            <br />
            <button class="apalah ms-5 btn btn-primary btn-lg" @click="submitForm()">Pay</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

import NavBar from "@/components/NavBar.vue";
import InvoiceBody from "@/components/InvoiceBody.vue";

export default {
    name: "Payment",
    components: {
        InvoiceBody,
        NavBar,
    },
    data() {
        return {
            // username: "",
            cart: [],
        };
    },
    methods: {
        submitForm() {
            console.log("MASUK SUBMIT");
            let a = [JSON.parse(window.localStorage.getItem("clerk"))[0].id_clerk]; // this is int type

            this.cart.push(a);

            axios
                .post("http://127.0.0.1:5000/submit", this.cart)
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error.message);
                });
            this.$router.push({
                path: "/dashboard",
            });
        },
    },
    mounted() {
        // this.username = localStorage.getItem("username");

        this.cart = JSON.parse(this.$route.query.payment_total);
        // console.log(this.$route.query.payment_total);
    },
};
</script>

<style scoped>
.apalah {
    width: 180px;
}
</style>
