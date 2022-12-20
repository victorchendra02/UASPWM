<script>
import axios from "axios";

export default {
    name: "Content",
    data() {
        return {
            active_indx: 0,
            category: [],
            products: [],
        };
    },
    methods: {
        get_category() {
            axios
                .get("http://127.0.0.1:5000/category")
                .then((data) => (this.category = data.data))
                .catch((err) => console.log(err.message));
        },
        get_products(cate) {
            axios
                .get("http://127.0.0.1:5000/spec_prod/" + cate)
                .then((data) => (this.products = data.data))
                .catch((err) => console.log(err.message));
        },
        add_to_cart(product) {
            this.emitter.emit("dari_component_lain", product);
            // console.log(product.img_path);
        },
    },
    mounted() {
        this.get_category();
        this.get_products("Goreng");
    },
};
</script>

<template>
    <!-- Content -->
    <div class="overflow-auto" style="height: 478px">
        <button class="me-3 btn btn-outline-primary" v-for="(cat, index) in this.category" @click="get_products(cat)" :key="index">
            {{ cat }}
        </button>
        <!-- <hr class="merah" /> -->
        <div class="container pt-2 ps-4">
            <div class="menu_makanan border border-2 p-2 rounded-3" v-for="(pp, index) in this.products" :key="index">
                <img :src="pp.img_path" alt="Product_image" class="gambar rounded-2" />
                <div class="mt-2 fw-bold">
                    {{ pp.product_name }}
                </div>
                <div>Rp {{ pp.price.toLocaleString("id-ID") }}</div>
                <div>
                    <button class="btn btn-outline-success mt-2" @click="add_to_cart(pp)">Add to cart <i class="fa-solid fa-cart-plus"></i></button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.gambar {
    width: 240px;
    aspect-ratio: 11/8;
    object-fit: cover;
}
.container {
    display: flex;
    gap: 28px;
}
.merah {
    border-top: 2px solid #dc3545;
}
</style>
