<template>
    <div class="toolbar" role="banner">
        <span id="welcome">{{ msg }}</span>
        <div class="spacer"></div>
        <vk-button size="small" class="menu-button" type="primary">500</vk-button>
        <vk-button size="small" class="menu-button" type="primary">400</vk-button>
        <vk-button size="small" class="menu-button" type="primary" @click="doSomething">doSomething</vk-button>
        <vk-button size="small" class="menu-button" type="primary" @click="$refs.childModal.showModal()">Login</vk-button>
        <router-link id="create-account" to="/createaccount">
          <vk-button size="small" class="menu-button" type="primary">Create Account</vk-button>
        </router-link>
        <login-modal ref="childModal"></login-modal>
        <div class="icon-div">
          <!-- <vk-menu id="menu-icon"></vk-menu> -->
          <img @click="showDropdown" ref="sandwichIcon" id="menu-icon2" src="../assets/icons8-menu.svg"/>
          <vk-drop animation="slide-top-small" position="top-right" mode="click" ref="dropMenu">
            <vk-navbar-nav-dropdown-nav align="right" navbar-aligned="true" id="nav-dropdown">
              <vk-nav-item title="500"></vk-nav-item>
              <vk-nav-item title="400"></vk-nav-item>
              <vk-nav-item title="Login"></vk-nav-item>
              <vk-nav-item title="Create Account"></vk-nav-item>
            </vk-navbar-nav-dropdown-nav>
          </vk-drop>
        </div>
    </div>

</template>

<script>
import '@vuikit/theme';
import { Button, ButtonLink} from '../../node_modules/vuikit/lib/button';
import { Icon, IconButton } from '../../node_modules/vuikit/lib/icon';
import { IconMenu } from '@vuikit/icons';
import { Drop } from '../../node_modules/vuikit/lib/drop';
import { NavbarNavItem, NavbarNavDropdownNav } from '../../node_modules/vuikit/lib/navbar';
import LoginModal from './LoginModal.vue';
export default {
  name: 'TopToolbar',
  components: {
      LoginModal,
      VkButton: Button,
      VkButtonLink: ButtonLink,
      VkMenu: IconMenu,
      VkIcon: Icon,
      VkIconButton: IconButton,
      VkDrop: Drop,
      VkNavItem: NavbarNavItem, 
      VkNavbarNavDropdownNav: NavbarNavDropdownNav 
  },
  data () {
    return {
      msg: 'Talk Tungsten 2 Me',
      dropDisplayed: false,
    }
  },
  created(){
    window.addEventListener("resize", this.trackResize);
  },
  destroyed(){
    window.removeEventListener("resize", this.trackResize);

  },
  methods: {
    doSomething() {
      this.msg= 'TopToolbar!;'
    },
    showDropdown(){
      console.log("in show dropdown");
      this.dropDisplayed = (this.dropDisplayed ? false : true);
    },
    trackResize(){
      // console.log(window.innerWidth);
      if(window.innerWidth > 650 && this.dropDisplayed){
        this.$refs.sandwichIcon.click();
        console.log("flipping display")
      }
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.spacer {
  flex: 1;
}

.toolbar {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background-image: linear-gradient(#1a46a5, #289128);
  color: white;
  font-weight: 600;
}

.icon-div{
  display: none;
}

.menu-button{
  margin-right: 2%;
}

#welcome{
  margin-left: 3%;
  font-size: 18px;
}

@media only screen and (max-width: 650px){
  .menu-button{
    display: none;
  }

  .icon-div{
    display: block;
    right: 0;
    position: absolute;
  }

  #menu-icon{
    width: 20%;
    height: 30%;
  }
  #menu-icon2{
    cursor: pointer;
    position: relative;
    width: 30px;
    height: 30px;
    padding: 2px;
    right: 3vw;
  }

  #create-account{

  }

  #nav-dropdown{
    position: absolute;
    background: rgb(225, 241, 225);
    /* width: 20vw;
    right: 0px; */
    right: 0px;
    top: 60px;
  }

}
</style>
