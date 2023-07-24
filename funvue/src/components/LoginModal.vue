<template>
    <div>
        <vk-modal :show="this.show">
            <vk-modal-close @click="closeModal"></vk-modal-close>
            <vk-modal-title>Login</vk-modal-title> 
            <form>
                <input class="uk-textarea" type="text"  placeholder="Email" v-model="email">
                <input class="uk-textarea" type="password" placeholder="Password" v-model="password" >
                <p :style="styleObject" id="incorrect">Incorrect password or username</p>
            </form>
             <vk-button @click="checkTestRoute">Check Test Route</vk-button>
            <vk-button @click="submitCreds">Submit</vk-button>
        </vk-modal>
    </div>
</template>

<script>
import axios from 'axios';
import { Modal, ModalClose, ModalTitle } from '../../node_modules/vuikit/lib/modal';
import { Button, ButtonLink } from '../../node_modules/vuikit/lib/button';
export default {
  name: 'LoginModal',
  components: {
    VkModal:Modal,
    VkModalClose: ModalClose,
    VkModalTitle: ModalTitle,
    VkButton: Button,
    VkButtonLink: ButtonLink
  },
  data () {
    return {
        msg: 'Welcome to Your Vue.js App',
        show: false,
        email: '',
        password:'',
        styleObject: {
            display: 'none',
            color:'red'
        },
    }
  },
  methods: {
    showModal() {
        console.log("in show modal");
        this.show=true;
    },
    closeModal() {
        console.log("in close modal");
        this.show=false;
        this.email= '';
        this.password= '';
        this.styleObject.display = 'none';

    },
    badCreds(){ 
        console.log("badcredshere");
        this.styleObject.display = 'inline';
    },
    async submitCreds(){
        const path = this.$hostname + '/userAuth';
        console.log(this.email)
        const response = await axios.post(path, {}, 
          {
            auth: {
              username: this.email,
              password: this.password
            },
            withCredentials: true
          }
          )
          .then((res) => { 
            console.log(res);
            this.closeModal();
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            this.badCreds();
            // reject(error);
          });
    },
    async checkTestRoute(){
        console.log("inCheckTest")
        const path = this.$hostname + '/testRoute';
        // const response = await axios.post(path, {withCredentials: true})
        const response = await axios.get(path, {withCredentials: true})
        // const response = await axios.post(path, creds)
          .then((res) => { 
            console.log(res)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
