<template>
    <!-- <div class="border-bottom border-2 border-danger" style="height: 6rem"> -->
    <div class="mb-2" style="height: 8rem">
        <h5 class="fw-bold">Jacob's Breakfast <i class="fas fa-utensils"></i></h5>

        <div class="lee">
            <table style="width: 100%">
                <tbody>
                    <tr>
                        <th>Id clerk:</th>
                        <td></td>
                        <td></td>
                        <td class="ree pe-4">{{ clerk[0].id_clerk }}</td>
                    </tr>
                    <tr>
                        <th>Clerk name:</th>
                        <td></td>
                        <td></td>
                        <td class="ree pe-4">{{ clerk[0].username }}</td>
                    </tr>
                    <tr>
                        <th>Date:</th>
                        <td class="ree pe-2">{{ day_name }}, {{ day }}-{{ month }}-{{ year }}</td>
                        <th>Time:</th>
                        <td class="ree pe-4">{{ hour }}:{{ minute }}:{{ second }}</td>
                    </tr>
                </tbody>
            </table>
            <hr style="width: 343px;">
        </div>
    </div>
</template>

<script>
export default {
    name: "HeaderInvoice",
    data() {
        return {
            clerk: JSON.parse(window.localStorage.getItem("clerk")),
            year: "",
            month: "",
            day: "",
            day_name: "",
            hour: "",
            minute: "",
            second: "",
        };
    },
    created() {
        const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        setInterval(() => {
            const today = new Date();
            this.year = today.getFullYear();
            this.month = today.getMonth() + 1; // Add 1 to get a 1-based month (1-12)
            this.day = today.getDate();
            this.day_name = dayNames[today.getDay()];
            this.hour = today.getHours();
            this.minute = today.getMinutes();
            this.second = today.getSeconds();
        }, 1000);
    },
};
</script>

<style scoped>
.lee {
    text-align: left;
}
.ree {
    text-align: right;
}
</style>
