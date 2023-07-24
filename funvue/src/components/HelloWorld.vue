<template>
  <div class="hello">
    <top-toolbar></top-toolbar>
    <h1>{{ msg }}</h1>
    <ul>
      <li>
        <button @click="doSomething">Change Message Please</button>
      </li>
      <li>
        <router-link to="/nextpage">Next Page Please</router-link>
      </li>
    </ul>
    
    <div id="mainGrid">
      <!-- loop through cards in js -->
      <vk-card v-for="card in cards" v-bind:key="card.id" v-bind:style="card.style" :data-aos="card.animation">
        <vk-card-title>
          {{ card.title }}
        </vk-card-title>
        <p>{{ card.msg }}</p>
      </vk-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TopToolbar from './TopToolbar.vue';
import { Card, CardTitle } from '../../node_modules/vuikit/lib/card';
export default {
  name: 'HelloWorld',
  components: {
    TopToolbar,
    VkCard: Card,
    VkCardTitle: CardTitle
  },
  data () {
    return {
      msg: 'Our Flagship Products',
      cardProps: {
        'grid-column': 0,
        'grid-row': 0
      },
      cards: [],
      mainCards: []
      }
    },
    created(){
        this.getCards();
        console.log("beforeCreate")
    },
    methods: {
      doSomething() {
        this.getCards();
      },
      generateCards() {
        //mainCards are the cards received from calling function getCards()

        let keys = Object.keys(this.mainCards);

        //loop through the provided cards adding the proper css to display
        //cards on alternate sides of the webpage with corresponding animation
        keys.forEach(key => {  
          let i = parseInt(key) + 1;
          //define the the style properties object
          let curProps = {
            gridColumn: 0,
            gridRow: 0
          }
          let curCard = Object.values(this.mainCards).find(el => el._id === parseInt(key));
          console.log(curCard);
          //grid row will correspond the index of the loop
          //as cards are displayed straight down the page
          curProps['gridRow'] = i;
          //column alternates page sides
          //even numbers on the right odd numbers on the left
          curProps['gridColumn'] = (i % 2 == 0)? 2 : 1;
          //assign grid props to card object
          curCard['style'] = curProps;
          //add complete card to cards array
          this.cards.push(curCard);
          console.log(curCard);
        })
        console.log(this.cards);
      },
      getCards() {
        const path = this.$hostname + '/cards';
        axios.get(path)
          .then((res) => { 
            this.mainCards = JSON.parse(JSON.stringify(res.data));
            this.generateCards();
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#mainGrid{
  position: relative;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  row-gap: 40%;
}
#secondCard{
    grid-column: 2;
    grid-row: 2;
}
#thirdCard{
    grid-column: 1;
    grid-row: 3;
}
#fourthCard{
    grid-column: 2;
    grid-row: 4;
}
#fifthCard{
    grid-column: 1;
    grid-row: 5;
}

</style>
