<template>
    <div>
        <vk-modal :show="this.show">
            <vk-modal-close @click="closeModal"></vk-modal-close>
            <vk-modal-title>Login</vk-modal-title> 
            <form>
                <input class="uk-textarea" type="text"  placeholder="Email" v-model="email">
                <input class="uk-textarea" type="text" placeholder="Password" v-model="password">
            </form>
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
      password:''
    }
  },
  methods: {
    showModal() {
        console.log("in show modal")
        this.show=true
    },
    closeModal() {
        console.log("in close modal")
        this.show=false
    },
    async submitCreds(){
        const path = 'http://localhost:8000/userAuth';
        const creds = { email: this.email, password: this.password};
        console.log(this.email + " and " + this.password)
        const response = await axios.post(path, creds)
          .then((res) => { 
            // this.mainCards = JSON.parse(JSON.stringify(res.data));
            console.log(res)
            // this.generateCards();
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
