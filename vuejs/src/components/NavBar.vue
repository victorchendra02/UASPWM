<template>
    <!-- Navbar -->
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-info p-3">
            <div class="container-fluid">
                <span @click="home()" class="navbar-brand yabgtlh"><i class="fa-solid fa-cash-register pe-2"></i> Point of Sale</span>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item ps-4">
                            <span class="yabgtlh" @click="reportSale()">Report Sale <i class="fa-regular fa-flag"></i></span>
                        </li>
                    </ul>

                    <button @click="logout()" class="btn btn-danger">Logout <i class="fa-solid fa-arrow-right-from-bracket ps-2"></i></button>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: "NavBar",
    data() {
        return {};
    },
    methods: {
        logout() {
            window.localStorage.clear();
            console.log("localStorage has been clear!");
            this.$router.push({
                path: "/",
            });
        },
        reportSale() {
            this.$router.push({
                path: "/report",
            });
        },
        home() {
            this.$router.push({
                path: "/dashboard",
            });
        },
    },
    // created() {},
};
</script>

<style scoped>
span.yabgtlh:hover {
    cursor: pointer;
    color: rgb(244, 244, 244);
}
</style>
