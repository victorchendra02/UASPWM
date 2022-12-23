<template>
    <div>
        <NavBar />
        <div class="container-fluid text-center">
            <br /><br /><br /><br /><br />
            <div style="width: 610px; margin-left: auto; margin-right: auto">
                <table class="table table-striped">
                    <tbody>
                        <tr>
                            <th>ID INVOICE</th>
                            <th style="width: 140px; text-align: left">USERNAME</th>
                            <th style="width: 250px">DATETIME</th>
                            <!-- <th></th> -->
                            <th colspan="2">TOTAL</th>
                        </tr>
                        <tr v-for="(x, index) in this.tt" :key="index">
                            <td>{{ x.id_invoice }}</td>
                            <td style="text-align: left">{{ x.username }}</td>
                            <td>{{ x.date }}</td>
                            <td>Rp</td>
                            <td style="text-align: right">{{ x.total.toString().toLocaleString("id-ID") }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <br /><br /><br /><br /><br />

            <div style="width: 610px; margin-left: auto; margin-right: auto">
                <table class="table table-striped">
                    <tbody>
                        <tr>
                            <th>ID INVOICE</th>
                            <th style="width: 160px; text-align: left">PRODUCT NAME</th>
                            <th style="width: 20px">QUANTITY</th>
                            <!-- <th></th> -->
                            <th colspan="2">SUB_TOTAL</th>
                        </tr>
                        <tr v-for="(x, index) in this.aa" :key="index">
                            <td>{{ x.id_invoice }}</td>
                            <td style="text-align: left">{{ x.product_name }}</td>
                            <td>{{ x.quantity }}</td>
                            <td>Rp</td>
                            <td style="text-align: right">{{ x.sub_total.toString().toLocaleString("id-ID") }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <br /><br /><br /><br /><br />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import NavBar from "@/components/NavBar.vue";

export default {
    name: "ReportSale",
    components: {
        NavBar,
    },
    data() {
        return {
            tt: [],
            aa: [],
        };
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
        axios
            .get("http://127.0.0.1:5000/report")
            .then((data) => (this.tt = data.data))
            .catch((err) => console.log(err.message));
        axios
            .get("http://127.0.0.1:5000/itulah")
            .then((data) => (this.aa = data.data))
            .catch((err) => console.log(err.message));
    },
};
</script>

<style scoped></style>
