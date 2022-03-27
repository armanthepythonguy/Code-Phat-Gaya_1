<script>
    import Dash1 from './Dash1-DESKTOP-H9VE4JI.svelte';
    import {Router} from 'svelte-hash-router';
</script>
<main>
    <div class="full">
    <a href="#/postform">add new Post</a>
    </div>
    <Dash1/>
</main>
<style>
    .full{
        background: black;
        display: grid;
        place-items: center;
    }
    .full a{
        text-decoration: none;
        background: green;
        color: black;
        font-size: 1rem;
        padding: 1rem 2rem;
        font-family: "roboto";
        border-radius: 2rem;
    }
</style>