<template>
    <div>
        <NavBar />
        <div class="container-fluid text-center">
            <br /><br /><br /><br /><br />

            <div style="width: 610px; margin-left: auto; margin-right: auto">
                <table class="table table-striped">
                    <tbody>
                        <tr>
                            <th>ID</th>
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
            <!-- <ol>
                <li v-for="(x, index) in this.tt" :key="index">
                    <span class="me-3">{{ x.id_invoice }}</span>
                    <span class="me-4">{{ x.username }}</span>
                    <span class="me-4">{{ x.date }}</span>
                    <span class="me-4">Rp {{ x.total.toLocaleString("id-ID") }}</span>
                </li>
            </ol> -->
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
    },
};
</script>

<style scoped></style>
