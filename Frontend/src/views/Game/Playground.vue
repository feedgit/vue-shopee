<template>
  <div class="battle-scene">
    <div class="box-top-left">
      <h2 class="pokemon">{{opponentPokemon}}</h2>
      <div class="hp-bar-top">
        <div v-bind:style="opponentHpBar" class="hp-bar-fill"></div>
      </div>
      <h4 class="level">Lvl. {{opponentLevel}}</h4>
    </div>
    <div class="box-top-right">
      <img v-if="opponentAlive" v-bind:src="opponentPokemonSrc" class="pokemon-top" />
    </div>
     <div class="box-bottom-left">
       <img v-if="userAlive" v-bind:src="userPokemonSrc" class="pokemon-bottom" />
    </div>
    <div class="box-bottom-right">
       <h2 class="pokemon"> {{userPokemon}}</h2>
      <div class="hp-bar-bottom">
        <div v-bind:style="userHpBar" class="hp-bar-fill"></div>
      </div>
      <h4 class="level">Lvl. {{userLevel}}</h4>
      <h4 class="hp">{{userHP}}/{{startUserHP}}</h4>
    </div>
    <div class="bottom-menu">
      <div class="battle-text text-box-left">
        {{battleText}}
      </div>
        <div class="text-box-right">
        <div v-if="optionsOn" id="battleOptions">
          <h4 v-on:click="processOption(1)" class="battle-text-top-left">{{battleOptions[0]}}</h4>
  <h4 v-on:click="processOption(2)" class="battle-text-top-right">{{battleOptions[1]}}</h4>
  <h4 v-on:click="processOption(3)" class="battle-text-bottom-left">{{battleOptions[2]}}</h4>
  <h4 v-on:click="processOption(4)" class="battle-text-bottom-right">{{battleOptions[3]}}</h4>
          </div>
       <div v-if="fightOn" id="fightOptions">
  <h4 v-on:click="processAttack(1)" class="battle-text-top-left">{{fightOptions[0]}}</h4>
  <h4 v-on:click="processAttack(2)" class="battle-text-top-right">{{fightOptions[1]}}</h4>
  <h4 v-on:click="processAttack(3)" class="battle-text-bottom-left">{{fightOptions[2]}}</h4>
  <h4 v-on:click="processAttack(4)" class="battle-text-bottom-right">{{fightOptions[3]}}</h4>
          </div>
       <div v-if="endOn" id="endOptions">
         <h4 v-on:click="resetBattle" class="battle-text-top-left">{{endOptions[0]}}</h4>
  <h4 class="battle-text-top-right">{{endOptions[1]}}</h4>
       </div>

      </div>
    </div>


  </div>
</template>

<script>
export default {
  data () {
    return {
       userPokemonSrc: "http://guidesmedia.ign.com/guides/059687/images/blackwhite/pokemans_006.gif",
       opponentPokemonSrc: "http://pre01.deviantart.net/959a/th/pre/f/2016/075/4/6/095_onix_by_rayo123000-d9vbjj3.png",
       userPokemon: "Charizard",
       opponentPokemon: "Onyx",
       userAlive: true,
       opponentAlive: true,
       opponentFill: 100,
       userFill: 100,
       userHP: 100,
       startUserHP: 100,
       opponentHP: 100,
       userLevel: 50,
       opponentLevel: 50,
       battleText: "What will Charizard do?",
       battleOptions: ["Fight", "Pokemon", "Item", "Run"],
       userAttackDamage: [15,40,50,25],
       opponentAttacks: ["Tackle", "Iron Tail", "Rock Slide", "Slam"],
       opponentAttackDamage: [15,40,50,25],
       fightOptions: ["Scratch", "Fly", "Flamethrower", "Ember"],
       endOptions: ["Yes", "No"],
       fightOn: false,
       optionsOn: true,
       endOn: false,
    userHpBar: {
      width: "100%"
    },
    opponentHpBar: {
      width: "100%"
    }
   }
  },
  methods:{
    processOption: function(option){
      switch(option){
        case 1:
          //handle fight
          this.optionsOn = false
          this.fightOn = true
        break;
        case 2:
          //handle pokemon
          setTimeout(() => {
          this.battleText = "What will " + this.userPokemon + " do?"
      }, 2000);

          this.battleText = "You're our only hope " + this.userPokemon + "!"

        break;
        case 3:
          //handle item
          setTimeout(() => {
          this.battleText = "What will " + this.userPokemon + " do?"
      }, 2000);
          this.battleText = "No items in bag."
        break;
        case 4:
          //handle run
          setTimeout(() => {
          this.battleText = "What will " + this.userPokemon + " do?"
      }, 2000);
          this.battleText = "Can't escape."
        break;
      }
    },
    processAttack: function(attack){
      switch(attack){
        case 1:
          //handle scratch
          this.opponentHP -= this.userAttackDamage[attack-1]
          //edit if HP !== 0
          this.opponentFill -= (this.userAttackDamage[attack-1])
          if(this.opponentFill <= 0){
            this.opponentHpBar.width = "0%"
          } else{
            this.opponentHpBar.width = this.opponentFill + "%"
          }
          if(this.checkOpponentHp()){
            this.battleText = this.opponentPokemon + " fainted! Play again?"
            this.processFaint(1)
          } else if(this.checkOpponentHp() === false) {

              setTimeout(() => {
              this.processOpponentAttack()
              }, 2000);

            this.battleText = this.userPokemon + " used " + this.fightOptions[attack-1] + "!"
            //call opponent attack function
          setTimeout(() => {
            if(this.userAlive){
              setTimeout(() => {this.battleText = "What will " + this.userPokemon + " do?"
              }, 2000);
            }
           }, 2000);
          }
        break;
        case 2:
          //handle fly
           this.opponentHP -= this.userAttackDamage[attack-1]
           //edit if HP !== 0
          this.opponentFill -= (this.userAttackDamage[attack-1])
          if(this.opponentFill <= 0){
            this.opponentHpBar.width = "0%"
          } else{
            this.opponentHpBar.width = this.opponentFill + "%"
          }
            if(this.checkOpponentHp()){
            this.battleText = this.opponentPokemon + " fainted! Play again?"
            this.processFaint(1)
          } else if(this.checkOpponentHp() === false) {

              setTimeout(() => {
              this.processOpponentAttack()
              }, 2000);

            this.battleText = this.userPokemon + " used " + this.fightOptions[attack-1] + "!"
            //call opponent attack function
          setTimeout(() => {
            if(this.userAlive){
              setTimeout(() => {this.battleText = "What will " + this.userPokemon + " do?"
              }, 2000);
            }
           }, 2000);
          }
        break;
        case 3:
          //handle flamethrower
           this.opponentHP -= this.userAttackDamage[attack-1]
           //edit if HP !== 0
          this.opponentFill -= (this.userAttackDamage[attack-1])
          if(this.opponentFill <= 0){
            this.opponentHpBar.width = "0%"
          } else{
            this.opponentHpBar.width = this.opponentFill + "%"
          }
            if(this.checkOpponentHp()){
            this.battleText = this.opponentPokemon + " fainted! Play again?"
            this.processFaint(1)
          } else if(this.checkOpponentHp() === false) {

              setTimeout(() => {
              this.processOpponentAttack()
              }, 2000);

            this.battleText = this.userPokemon + " used " + this.fightOptions[attack-1] + "!"
            //call opponent attack function
          setTimeout(() => {
            if(this.userAlive){
              setTimeout(() => {this.battleText = "What will " + this.userPokemon + " do?"
              }, 2000);
            }
           }, 2000);
          }
        break;
        case 4:
          //handle ember
           this.opponentHP -= this.userAttackDamage[attack-1]
           //edit if HP !== 0
          this.opponentFill -= (this.userAttackDamage[attack-1])
          if(this.opponentFill <= 0){
            this.opponentHpBar.width = "0%"
          } else{
            this.opponentHpBar.width = this.opponentFill + "%"
          }
          if(this.checkOpponentHp()){
            this.battleText = this.opponentPokemon + " fainted! Play again?"
            this.processFaint(1)
          } else if(this.checkOpponentHp() === false) {

              setTimeout(() => {
              this.processOpponentAttack()
              }, 2000);

            this.battleText = this.userPokemon + " used " + this.fightOptions[attack-1] + "!"
            //call opponent attack function
          setTimeout(() => {
            if(this.userAlive){
              setTimeout(() => {this.battleText = "What will " + this.userPokemon + " do?"
              }, 2000);
            }
           }, 2000);
          }
        break;
      }
    },
    checkOpponentHp: function(){
      if(this.opponentHP <= 0){
        //fainted
        return true

      } else{
        //battle continues
        return false
      }
    },
    processFaint: function(pokemon){
      this.fightOn = false
      this.endOn = true;
      if(pokemon === 1){
        this.opponentAlive = false
      } else {
        this.userHP = 0
        this.userAlive = false
      }
    },
    processOpponentAttack: function(){
      //generate random number
      var random = Math.floor((Math.random() * 4) + 1)
      //do damage to user
      this.userHP -=  this.opponentAttackDamage[random-1]
      this.userFill -= (this.opponentAttackDamage[random-1])
      if(this.userFill <= 0){
        this.userHpBar.width = "0%"
      } else{
        this.userHpBar.width = this.userFill + "%"
      }
       if(this.checkUserHp()){
         //add battle text
         this.battleText = this.userPokemon + " fainted! Play again?"
         this.processFaint(2)
       } else if(this.checkOpponentHp() === false) {
         //continue battle
         this.battleText = this.opponentPokemon + " used " + this.opponentAttacks[random-1]  + "!"
         this.fightOn = false
         this.optionsOn = true
       }
    },
    checkUserHp: function(){
       if(this.userHP <= 0){
        //fainted
        return true

      } else{
        //battle continues
        return false
      }
    },
    resetBattle: function(){
      //reset data to start new game
      this.endOn = false;
      this.fightOn = false;
      this.optionsOn = true;
      this.battleText = "What will Charizard do?"
      this.userAlive = true
      this.opponentAlive = true
      this.userHP = 100
      this.opponentHP = 100
      this.userFill = 100
      this.opponentFill = 100
      this.userHpBar.width = "100%"
      this.opponentHpBar.width = "100%"
    }
  }

}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');

@import url('https://fonts.googleapis.com/css?family=PT+Sans+Narrow');
.title{
  position: relative;
  margin-top: 10px;
  color: white;
  text-align: center;
  font-size: 28px;
  text-transform: uppercase;
  font-family: "Roboto Condensed";
}

.battle-scene{
  position: relative;
  margin: auto;
  display: block;
  margin-top: 3%;
  width: 600px;
  height: 420px;
  background: #F8F8F8;
  z-index: 1;
}

.box-top-left{
  position: absolute;
  width: 40%;
  height: 15%;
  border-radius: 10px;
  top: 8%;
  left: 8%;
  background: #F8F8D8;
  border: 6px solid #506860;
}

.hp-bar-top{
  position: absolute;
  bottom: 16%;
  height: 20%;
  width: 70%;
  left: 10%;
  border-radius: 20px;
  background: grey;
  opacity: 0.5;
}

.hp-bar-bottom{
  position: absolute;
  bottom: 32%;
  height: 20%;
  width: 70%;
  left: 10%;
  border-radius: 20px;
  background: grey;
  opacity: 0.5;
}

.hp-bar-fill{
  position: absolute;
  height: 100%;
  border-radius: 20px;
  background: #FF8800;
}

.box-top-right{
  position: absolute;
  width: 40%;
  height: 25%;
  border-radius: 50%;
  top: 25%;
  right: 8%;
  background: #E0E0E0;
}

.pokemon-top{
  height: 150%;
  width: 50%;
  position: absolute;
  top: -80%;
  left: 25%;
}

.pokemon-bottom{
  height: 150%;
  width: 50%;
  position: absolute;
  top: -75%;
  left: 25%;
}


.box-bottom-left{
 position: absolute;
  width: 40%;
  height: 25%;
  border-radius: 50%;
  bottom: 15%;
  left: 8%;
  background: #E0E0E0;
}

.box-bottom-right{
  position: absolute;
  width: 38%;
  height: 20%;
  border-radius: 10px;
  bottom:20%;
  right: 8%;
  background: #F8F8D8;
  border: 6px solid #506860;
  z-index: 2;
}

.pokemon{
  text-align: left;
  margin-left: 10%;
  margin-top: 5%;
  opacity: 0.7;
  font-size: 18px;
  font-family: "Roboto Condensed";
}

.level{
  position: absolute;
  right: 8%;
  top: -11%;
  opacity: 0.7;
  font-size: 16px;
  font-family: "Roboto Condensed";
}

.hp{
  position: absolute;
  right: 8%;
  bottom: -20%;
  opacity: 0.7;
  font-size: 16px;
  font-family: "Roboto Condensed";
}

.bottom-menu{
  position: absolute;
  width: 98%;
  bottom: 0%;
  height: 19%;
  background: #285068;
  z-index: 1;
  border: solid 6px #CEB46D;
}

.text-box-left{
  position: absolute;
  width: 50%;
  left: 0%;
  height: 95%;

}

.text-box-right{
  position: absolute;
  width: 40%;
  top: -6%;
  right: -1%;
  height: 98%;
  background: #F8F8F8;
  border: solid 6px #6F677F;

}

.battle-text{
  margin-top: 3%;
  margin-left: 5%;
  opacity: 0.95;
  font-size: 18px;
  color: white;
  text-align: left;
  font-family: "PT Sans Narrow";
}

.battle-text-top-left{
  opacity: 0.95;
  position: absolute;
  font-size: 22px;
  color: #333333;
  top: -30%;
  left: 10%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

.battle-text-bottom-left{
  opacity: 0.95;
  position: absolute;
  font-size: 22px;
  color: #333333;
  bottom: -30%;
  left: 10%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

.battle-text-top-right{
  opacity: 0.95;
  position: absolute;
  font-size: 22px;
  color: #333333;
  top: -30%;
  right: 21%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

.battle-text-bottom-right{
  opacity: 0.95;
  position: absolute;
  font-size: 22px;
  color: #333333;
  bottom: -30%;
  right: 20%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

@media all and (max-width: 600px) {
 .battle-scene{
  position: relative;
  margin: auto;
  display: block;
  margin-top: 3%;
  width: 400px;
  height: 280px;
  background: #F8F8F8;
  z-index: 1;
}

  .title{
  position: absolute;
  top: -33%;
  left: 7.5%;
  color: white;
  text-align: center;
  font-size: 22px;
  text-transform: uppercase;
  font-family: "Roboto Condensed";
}

  .pokemon{
  text-align: left;
  margin-left: 11%;
  margin-top: 5%;
  opacity: 0.7;
  font-size: 14px;
  font-family: "Roboto Condensed";
}


.level{
  position: absolute;
  right: 5%;
  top: -13%;
  opacity: 0.7;
  font-size: 10px;
  font-family: "Roboto Condensed";
}

  .hp{
  position: absolute;
  right: 8%;
  bottom: -20%;
  opacity: 0.7;
  font-size: 11px;
  font-family: "Roboto Condensed";
}


.battle-text-top-left{
  opacity: 0.95;
  position: absolute;
  font-size: 14px;
  color: #333333;
  top: -30%;
  left: 10%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

.battle-text-bottom-left{
  opacity: 0.95;
  position: absolute;
  font-size: 14px;
  color: #333333;
  bottom: -30%;
  left: 10%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

.battle-text-top-right{
  opacity: 0.95;
  position: absolute;
  font-size: 14px;
  color: #333333;
  top: -30%;
  right: 21%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

.battle-text-bottom-right{
  opacity: 0.95;
  position: absolute;
  font-size: 14px;
  color: #333333;
  bottom: -30%;
  right: 20%;
  text-align: left;
  font-family: "PT Sans Narrow";
  cursor: pointer;
}

  .battle-text{
  margin-top: 1%;
  margin-left: 5%;
  opacity: 0.95;
  font-size: 10px;
  color: white;
  text-align: left;
  font-family: "PT Sans Narrow";
}



}

</style>
