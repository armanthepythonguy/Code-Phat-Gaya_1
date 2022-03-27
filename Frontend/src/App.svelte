<script>
	import { routes, Router } from 'svelte-hash-router';
	import Footer from "./Footer.svelte";
	import Nav from "./Nav.svelte";
	import Dash1 from "./Dash1.svelte";
	import Dash2 from "./Dash2.svelte";
	import Alink from "./Alink.svelte";
	import Login from "./Login.svelte";
	import Reg from "./Reg.svelte";
	routes.set({
		'/':Alink,
		'/dash1':Dash1,
		'/dash2':Dash2
	}) 
</script>
<main>
	<Reg/>
</main>
<style>
	main{
		position: relative;
	}
	.foot{
		position: absolute;
		left: 0px;
		bottom: 0px;

	}
</style>