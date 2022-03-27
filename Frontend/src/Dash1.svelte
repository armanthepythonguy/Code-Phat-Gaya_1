<script>
</script>
<main>
    <div class="head">The global leaderboard</div>
    <div class="full">
    <a href="">
    <div class="card">
        <div class="name">Ramanathan Srinivasan</div>
        <div class="score">760</div>
    </div>
    </a>

    </div>
</main>
<style>
    a{
        text-decoration: none;
        color: rgb(185, 149, 80);
    }
    .head{
        display: grid;
        place-items: center;
        padding: 3% 0% 2% 0%;
        color: wheat;
        font-size: 2rem;
        font-family: "robo";
        letter-spacing: 0.4vw;
    }
    .card{
        display: grid;
        grid-template-columns: repeat(3,1fr);
        grid-template-rows: 1fr;
        width: 95vw;
        height: 4vh;
        border: wheat solid 1px;
        margin-left: 2vw;
        margin-bottom: 2vh;
    }
    .card .name{
        font-family: "roboto";
        display: grid;
        place-items: center;
        grid-area: 1/1/2/3;}
    .card .score{
        font-family: "roboto";
        display: grid;
        place-items: center;
        grid-area: 1/3/2/4;
    }
    main{
        background: black;
    }
    .full{
        background: black;
        overflow-y: scroll;
        height: 71.5vh;
    }
    .full::-webkit-scrollbar{
        background: black;
    }
    .full::-webkit-scrollbar-thumb{
        background: wheat;
    }
</style>