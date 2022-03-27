<script>
    import {Router} from 'svelte-hash-router';
</script>
<main>
    <div class="head">The jobs available</div>
    <div class="full">
    <a href="#/thanks">
    <div class="card">
        <div class="name">Senior engineer</div>
        <div class="score">Zoho</div>
    </div>
    <div class="card">
        <div class="name">Junior engineer</div>
        <div class="score">Freshworks</div>
    </div>
    <div class="card">
        <div class="name">Architect</div>
        <div class="score">Polygon</div>
    </div>
    <div class="card">
        <div class="name">Creator</div>
        <div class="score">Dhruv</div>
    </div>
    <div class="card">
        <div class="name"> Asst. engineer</div>
        <div class="score">Postman</div>
    </div>
    <div class="card">
        <div class="name">Technical Staff</div>
        <div class="score">Swiggy</div>
    </div>
    <div class="card">
        <div class="name">Content Writer</div>
        <div class="score">Razorpay</div>
    </div>
    <div class="card">
        <div class="name">Marketer</div>
        <div class="score">Dream11</div>
    </div>
    <div class="card">
        <div class="name">Product manager</div>
        <div class="score">Zoho</div>
    </div>
    <div class="card">
        <div class="name">Project engineer</div>
        <div class="score">Orangescope</div>
    </div>
    <div class="card">
        <div class="name">Project manager</div>
        <div class="score">Zerodha</div>
    </div>
    <div class="card">
        <div class="name">Technical HR</div>
        <div class="score">Zoho</div>
    </div>
    <div class="card">
        <div class="name">Senior engineer</div>
        <div class="score">Zoho</div>
    </div>
    <div class="card">
        <div class="name">Junior engineer</div>
        <div class="score">Freshworks</div>
    </div>
    <div class="card">
        <div class="name">Architect</div>
        <div class="score">Polygon</div>
    </div>
    <div class="card">
        <div class="name">Creator</div>
        <div class="score">Dhruv</div>
    </div>
    <div class="card">
        <div class="name"> Asst. engineer</div>
        <div class="score">Postman</div>
    </div>
    <div class="card">
        <div class="name">Technical Staff</div>
        <div class="score">Swiggy</div>
    </div>
    <div class="card">
        <div class="name">Content Writer</div>
        <div class="score">Razorpay</div>
    </div>
    <div class="card">
        <div class="name">Marketer</div>
        <div class="score">Dream11</div>
    </div>
    <div class="card">
        <div class="name">Product manager</div>
        <div class="score">Zoho</div>
    </div>
    <div class="card">
        <div class="name">Project engineer</div>
        <div class="score">Orangescope</div>
    </div>
    <div class="card">
        <div class="name">Project manager</div>
        <div class="score">Zerodha</div>
    </div>
    <div class="card">
        <div class="name">Technical HR</div>
        <div class="score">Zoho</div>
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
        background: rgb(136, 94, 17);
    }
</style>