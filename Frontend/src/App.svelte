<script>
	import { routes, Router } from 'svelte-hash-router';
	import Footer from "./Footer.svelte";
	import Nav from "./Nav.svelte";
	import Price from "./Dash1.svelte";
	import Inspri from "./Dash2.svelte";
	import Ftrs from "./Alink.svelte";
	import Home from "./Login.svelte";
	import Thanks from "./Thanks.svelte";
	import Post from "./Post.svelte";
	import Postform from "./Postform.svelte";
	routes.set({
        '/': Home,
		'/alink':Ftrs,
		'/dash1':Price,
		'/dash2':Inspri,
        '/thanks':Thanks,
        '/post':Post,
        '/postform':Postform
	}) 
</script>
<main>
	<Nav/>
    <Router/>
    <Footer/>
</main>
<style>
	main{
		position: relative;}
</style>

