<script>
    import { NumerologyCalculator } from '../utils/numerology';
    import LoshuGrid from './LoshuGrid.svelte';
    
    let firstName = '';
    let lastName = '';
    let dob = '';
    let gender = '';
    let labels = false;
  
    let psychicNumber = 0;
    let destinyNumber = 0;
    let kuaNumber = 0;
    let grid = {};
  
    const calculate = () => {
      const dobParts = dob.split('-').map(Number);
      psychicNumber = NumerologyCalculator.calculatePsychicNumber(dobParts[2]);
      destinyNumber = NumerologyCalculator.calculateDestinyNumber(dob);
      kuaNumber = NumerologyCalculator.calculateKuaNumber(dobParts[0], gender);
      grid = NumerologyCalculator.createLoshuGrid(dob, gender);
    };
  </script>  

<div>
    <h1>LoShu Grid</h1>

    <label>
        First Name:
        <input bind:value={firstName} type="text" />
    </label>

    <label>
        Last Name:
        <input bind:value={lastName} type="text" />
    </label>

    <label>
        Date of Birth:
        <input bind:value={dob} type="date" />
    </label>

    <label>
        Gender:
        <select bind:value={gender}>
            <option value="">--Please choose an option--</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select>
    </label>

    <label>
        <input bind:checked={labels} type="checkbox" />
        Horizontal and Vertical Planes
    </label>

    <button on:click={calculate}>Calculate</button>

    <div>
        <h2>Results</h2>
        <p>Psychic Number: {psychicNumber}</p>
        <p>Destiny Number: {destinyNumber}</p>
        <p>Kua Number: {kuaNumber}</p>
    </div>

    <LoshuGrid {grid} />
</div>
