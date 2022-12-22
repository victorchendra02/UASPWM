<template>
    <div class="aaa">
        <div class="bbb">
            <br /><br /><br />
            <br /><br /><br />

            <h1>Please Login</h1>
            <div class="form-floating mb-3 mt-5">
                <input v-model="username" type="text" class="form-control" id="floatingInput" placeholder="name@example.com" />
                <label for="floatingInput">Username</label>
            </div>
            <div class="form-floating">
                <input v-model="pass" type="password" class="form-control" id="floatingPassword" placeholder="Password" />
                <label for="floatingPassword">Password</label>
            </div>

            <button @click="goToDashboard()" type="button" class="btn btn-outline-primary btn-lg vic mt-4">Login →</button>

            <br /><br /><br />
            <h4 class="merah" v-if="e_usrname_n_pass != ''">{{ e_usrname_n_pass }}</h4>
            <h4 class="merah" v-if="e_usrname != ''">{{ e_usrname }}</h4>
            <h4 class="merah" v-if="e_pass != ''">{{ e_pass }}</h4>

            <h4 class="merah" v-if="w_usrname != ''">{{ w_usrname }}</h4>
            <h4 class="merah" v-if="w_pass != ''">{{ w_pass }}</h4>

            <h4 class="merah" v-if="dumb != ''">{{ dumb }}</h4>

            <h4 class="merah" v-if="match_clerk.length != 0">{{ match_clerk }}</h4>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Login",
    data() {
        return {
            username: "",
            pass: "",
            users: [],
            match_clerk: [],

            e_usrname_n_pass: "",
            e_usrname: "",
            e_pass: "",

            w_usrname: "",
            w_pass: "",

            dumb: "",
        };
    },
    methods: {
        goToDashboard() {
            this.e_usrname = "";
            this.e_pass = "";
            this.e_usrname_n_pass = "";

            this.w_usrname = "";
            this.w_pass = "";

            this.dumb = "";

            // empty error
            if (this.username === "") {
                if (this.pass === "") {
                    this.e_usrname_n_pass = "Please fill the username & password!";
                    return;
                }
                this.e_usrname = "Please fill the username!";
                return;
            }
            if (this.pass === "") {
                this.e_pass = "Please fill the password!";
                return;
            }

            // wrong login error
            let is_usrname_found = false;
            let is_pass_found = false;
            for (let i = 0; i < this.users.length; i++) {
                if (this.users[i].username === this.username) {
                    is_usrname_found = true;
                    if (this.users[i].password === this.pass) {
                        is_pass_found = true;
                        this.match_clerk.push(this.users[i]);
                        break;
                    }
                }
            }

            // Wrong username
            if (is_usrname_found === false) {
                this.w_usrname = "Wrong username!";
                return;
            }

            // Wrong password
            if (is_usrname_found) {
                if (is_pass_found === false) {
                    this.w_pass = "Invalid password!";
                    return;
                }
                // Match with database
                this.dumb = "MATCH!";
                window.localStorage.setItem("clerk", JSON.stringify(this.match_clerk));

                // redirect to dashboard
                this.$router.push({
                    path: "/dashboard",
                    // query: {
                    //     clerk: JSON.stringify(this.match_clerk),
                    // },
                });
            }
        },
    },
    created() {
        axios
            .get("http://127.0.0.1:5000/clerks")
            .then((data) => (this.users = data.data))
            .catch((err) => console.log(err.message));
    },
};
</script>

<style>
.aaa {
    display: flex;
    justify-content: center;
    align-content: center;
    text-align: center;
    /* width: 500px; */
}
.bbb {
    /* background-color: aqua; */
    width: 400px;
}
.vic {
    width: 90%;
}
.merah {
    color: #dc3545;
}
</style>
