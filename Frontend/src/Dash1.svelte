<script>
    import {Router} from 'svelte-hash-router';
</script>
<main>
    <div class="head">The global leaderboard</div>
    <div class="full">
    <a href="#/dash2">
    <div class="card">
        <div class="name">Ramanathan Srinivasan</div>
        <div class="score">760</div>
    </div>
    <div class="card">
        <div class="name">Ahmed Azad</div>
        <div class="score">627</div>
    </div>
    <div class="card">
        <div class="name">Arman Aurbindo</div>
        <div class="score">699</div>
    </div>
    <div class="card">
        <div class="name">Chidam</div>
        <div class="score">760</div>
    </div>
    <div class="card">
        <div class="name">Subramanian </div>
        <div class="score">525</div>
    </div>
    <div class="card">
        <div class="name">Vishal</div>
        <div class="score">383</div>
    </div>
    <div class="card">
        <div class="name">Balaji</div>
        <div class="score">779</div>
    </div>
    <div class="card">
        <div class="name">Raguvendra</div>
        <div class="score">884</div>
    </div>
    <div class="card">
        <div class="name">Kamath</div>
        <div class="score">475</div>
    </div>
    <div class="card">
        <div class="name">Komasetti</div>
        <div class="score">621</div>
    </div>
    <div class="card">
        <div class="name">Tiwari</div>
        <div class="score">750</div>
    </div>
    <div class="card">
        <div class="name">Sharma</div>
        <div class="score">499</div>
    </div>
    <div class="card">
        <div class="name">Yadav</div>
        <div class="score">89</div>
    </div>
    </a>
    <Router/>
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