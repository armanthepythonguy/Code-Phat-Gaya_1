<script>
  import Dash1 from "./Dash1-DESKTOP-H9VE4JI.svelte"
  let count=0;
  let count1=0;
  function counter(){
    count+=1
  }
  function counter1(){
    count1-=1
  }
</script>
<main>
  <div class="main">
  <div class="glass">
  </div>
  <div class="full">
    <div class="meter">
    <meter value="760" high="1000" max="1000" min="0"></meter></div>
    <div class="points">
      760
    </div>
  <div class="name">
    Ramanuja 
  </div>
  <div class="icons">
    <div class="img">
    <a href=""><img src="./img/icons8-codechef.svg" alt=""></a>
    <a href=""><img src="./img/icons8-github.svg" alt=""></a>
    <a href=""><img src="./img/icons8-leetcode.png" alt=""></a>
    </div>
  </div>
  <div class="counter">
    <div class="col1"><button on:click={counter}><img src="./img/icons8-up48.png" alt="up"></button>{count}</div>
    <div class="col2"><button on:click={counter1}><img src="./img/icons8-down48.png" alt="down"></button>{count1}</div>
  </div>
</div>
</div>
<Dash1/>
</main>
<style>

  .job .hmm{
    font-family: "robo";
  }
  .col2 button{
    background: transparent ;
  }
  .col1 button{
    background: transparent;
  }
  .counter{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr;
  }
  .col1{
    display: grid;
    place-items: center;
    grid-area: 1/1/2/2;
    background: green;
  }
  .col2{
    display: grid;
    place-items: center;
    grid-area: 1/2/2/3;
    background: rgb(160, 19, 19);

  }
  .icons{
    display: grid;
    place-items: center;
  }
  .img img{
    padding: 2rem;
  }
  .name {
    font-family: "ele";
    font-size: 3rem;
    display: grid;
    justify-items: center;
  }
  .points {
    font-family: "robo";
    font-size: 3rem;
    display: grid;
    place-items: center;
  }
  meter{
    width: 20vw;
    height: 4vw;
    grid-area: 1/1/2/2;
  }
  .meter{
    display: grid;
    place-items: center;
  }
  .main{
    position: relative;
    height: 84vh;
    background: wheat;
    display: grid;
    place-items: center;
  }
  .glass{
    height: 76vh;
    width: 80vw;
    background: black;
    border-radius: 2rem;
    opacity: 0.3;
  }
  .full{
    display: grid;
    grid-template-rows: repeat(5,1fr);
    grid-template-columns: 1fr;
    position: absolute;
    top: 4vh;
    left: 10vw;
    height: 76vh;
    width: 80vw;
  }

</style>