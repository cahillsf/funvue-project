<template>
    <div id="mainGrid">
        <form>
            <fieldset class="uk-fieldset">
                <div>
                    <legend class="uk-legend">Create your Funvue Account</legend>
                </div>
                <div class="uk-margin name">
                    <input class="uk-input" type="text" placeholder="First name">
                </div>
                <div class="uk-margin name">
                    <input class="uk-input" type="text" placeholder="Last name">
                </div>
                <div id="email">
                    <input class="uk-input" type="text" placeholder="Email address">
                </div>
                <div class="uk-margin password">
                    <input class="uk-input" type="text" placeholder="Password">
                </div>
                <div class="uk-margin password">
                    <input class="uk-input" type="text" placeholder="Confirm password">
                </div>
                <vk-button size="small" class="menu-button" type="primary">Cancel</vk-button>
                <vk-button size="small" class="menu-button" type="primary">Create Account</vk-button>
            </fieldset>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
import TopToolbar from './TopToolbar.vue';
import { Button, ButtonLink} from '../../node_modules/vuikit/lib/button';

export default {
    name: 'CreateAccount',
    components: { 
        TopToolbar, 
        VkButton: Button,
        VkButtonLink: ButtonLink
    },
    data () {
        return {
        msg: 'Welcome to Your Vue.js App'
        }
    },
    methods: {
        doSomething() {
        this.msg= 'another page hahahahahahahaha!';
        },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

form{
    position: absolute;
    border-radius: 25px;
    border: 2px solid #289128;
    padding: 20px;
    width: 80vw;

}

fieldset{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}

legend{
    position: relative;
    left: 1px;
    grid-row: 1;
}

.menu-button{
    grid-row: 5;
    margin: 2%;
}

.name{
    grid-row: 2;
}

.password{
    grid-row: 4;
}

.uk-margin{
    margin: 2%;
}

.uk-input{
    margin: 2%;
}

#mainGrid{
    position: relative;
    display: grid;
    justify-items: center;
}

#email{
    grid-row: 3;
    grid-column: 1/3;
}

</style>
