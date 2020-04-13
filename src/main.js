import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
// import store from "./store";

//importing bootstrap
import "bootstrap/dist/js/bootstrap";
import "bootstrap/dist/css/bootstrap.css";

import "@glidejs/glide/dist/css/glide.core.min.css";
import "@glidejs/glide/dist/css/glide.theme.min.css";

//importing fontawesome icons
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUserSecret,
  faChevronLeft,
  faChevronRight,
  faBars
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faUserSecret, faChevronRight, faChevronLeft, faBars);

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

//определяем пути
// import AdminLogin from "./components/AdminLogin";
import Admin from "./components/Admin";
import Client from "./components/Client";
Vue.use(VueRouter);
const router = new VueRouter({
  mode: "history",
  routes: [
    { path: "/admin", component: Admin },
    { path: "/", component: Client }
  ]
});

new Vue({
  router: router,
  render: h => h(App)
}).$mount("#app");
