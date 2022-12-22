<template>
    <div class="border-top border-2 border-danger pt-4">
        <button class="btn btn-warning adminz" @click="goToReportSale()">Report Sale!</button>
    </div>
</template>

<script>
export default {
    name: "AdminCommands",
    methods: {
        goToReportSale() {
            this.$router.push({
                path: "/report",
                query: {},
            });
        },
    },
};
</script>

<style scoped>
.adminz {
    width: 320px;
}
</style>
