<script>
	import { calculatePsychicNumber, calculateDestinyNumber, calculateKuaNumber } from './numerology.js';
	import { generateLoshuGrid } from './loshu.js';
	import LoshuGrid from './LoshuGrid.svelte';
  
	let name = '';
	let dob = '';
	let gender = '';
	let psychicNumber;
	let destinyNumber;
	let kuaNumber;
	let grid;
  
	function calculate() {
	  const [year, month, day] = dob.split('-').map(Number);
	  psychicNumber = calculatePsychicNumber(day);
	  destinyNumber = calculateDestinyNumber(dob);
	  kuaNumber = calculateKuaNumber(year, gender);
  
	  grid = generateLoshuGrid(day, month, year, psychicNumber, destinyNumber, kuaNumber);
	}
</script>
  
  <!-- ... rest of the file remains the same ... -->
  
  
  <main>
	<h1>Loshu Grid Generator</h1>
	<form on:submit|preventDefault={calculate}>
	  <label for="name">Your Full Name:</label>
	  <input id="name" bind:value={name} type="text" required>
  
	  <label for="dob">Date of Birth:</label>
	  <input id="dob" bind:value={dob} type="date" required>
  
	  <label for="gender">Sex:</label>
	  <select id="gender" bind:value={gender} required>
		<option disabled value=""> -- select an option -- </option>
		<option>Male</option>
		<option>Female</option>
	  </select>
  
	  <button type="submit">Calculate</button>
	</form>
  
	{#if psychicNumber !== undefined}
	  <p>Psychic Number: {psychicNumber}</p>
	  <p>Destiny Number: {destinyNumber}</p>
	  <p>Kua Number: {kuaNumber}</p>

	  <LoshuGrid {grid} />
	{/if}
  </main>  