<template>
    <!-- <div class="border-2 border-danger"> -->
    <div>
        <!-- InvoiceBody -->
        <div style="height: 22rem; overflow: auto; text-align: left">
            <ol>
                <li v-for="(x, index) in this.cart" :key="index">
                    <span class="me-3">{{ x.product_name }}</span>
                    <span class="me-4">{{ x.qty }}</span>
                    <span class="me-4">{{ x.price.toLocaleString("id-ID") }}</span>
                    <span class="me-4 fw-bold">Rp {{ x.sub_total.toLocaleString("id-ID") }}</span>
                    <div class="pe-4" style="text-align: right">
                        <button @click="addQty(x)" class="btn btn-success btn-sm mt-1 mb-3 mx-2 akukesal"><i class="fas fa-plus"></i></button>
                        <button @click="decreaseQty(x)" class="btn btn-outline-danger btn-sm mt-1 mb-3 mx-2 akukesal"><i class="fas fa-minus"></i></button>
                    </div>
                </li>
            </ol>
        </div>
        <div class="py-2 text-start ps-3 fw-bold fs-5" >TOTAL: Rp {{ this.total.toLocaleString("id-ID") }}</div>

        <!-- Commands -->
        <!-- <div class="border-top border-2 border-danger pt-3" style="height: 6rem"> -->
        <div class="mt-2" style="height: 6rem">
            <button class="me-4 px-5 btn btn-success" @click="goToPayment()">Payment</button>
            <button class="ms-4 px-5 btn btn-outline-danger" @click="clearCart()">Cancel</button>
            <br />
        </div>
        <!-- <input type="text" v-model="username">
        <button @click="save_username()">Save</button> -->
    </div>
</template>

<script>
import CategoryProduct from "./CategoryProduct.vue";

export default {
    name: "InvoiceBody",
    components: {
        CategoryProduct,
    },
    data() {
        return {
            username: "Jacob",
            cart: [
                // ex. what will appended
                // {id_product: 1, category: "Goreng", price: 2000, product_name: "Ayam Goreng", sub_total: qty*price, qty: 1}
            ],
            total: 0,
        };
    },
    methods: {
        update_total_invoice() {
            let dumb = 0;
            for (let i = 0; i < this.cart.length; i++) {
                dumb = dumb + this.cart[i].sub_total;
            }
            this.total = dumb;
        },
        update_qty(p) {
            p.qty += 1;
        },
        update_subtotal(p) {
            p.sub_total = p.price * p.qty;
        },
        addtocart(p) {
            if (this.cart.length === 0) {
                this.cart.push(p);
                this.update_total_invoice();
            } else {
                let is_new = true;
                for (let i = 0; i < this.cart.length; i++) {
                    if (this.cart[i].id_product == p.id_product) {
                        // Increase qty
                        this.update_qty(p);
                        // Increase sub total of that item
                        this.update_subtotal(p);
                        // Update total invoice
                        this.update_total_invoice();
                        is_new = false;
                    }
                }
                if (is_new) this.cart.push(p);
                this.update_total_invoice();
            }
        },
        addQty(p) {
            this.update_qty(p);
            this.update_subtotal(p);
            this.update_total_invoice();
        },
        decreaseQty(p) {
            if (p.qty > 1) {
                p.qty -= 1;
                this.update_subtotal(p);
                this.update_total_invoice();

                return;
            }
        },
        clearCart() {
            this.cart = [];
            this.update_total_invoice();
        },
        goToPayment() {
            if (this.cart.length === 0) {
                alert("Your cart is empty!\nPlease add something to cart");
                return;
            }
            this.$router.push({
                path: "/payyy",
                query: {
                    payment_total: JSON.stringify(this.cart),
                    // payment_total: this.cart,
                },
            });
        },
        save_username() {
            console.log("saved", this.username);
            localStorage.setItem("username", this.username);
        },
    },
    mounted() {
        this.emitter.on("dari_component_lain", (pd) => {
            let p = {
                category: pd.category,
                id_product: pd.id_product,
                price: pd.price,
                product_name: pd.product_name,
                sub_total: pd.price,
                qty: 1,
            };
            this.addtocart(p);
        });
    },
};
</script>

<style>
.akukesal {
    width: 50px;
}
</style>
