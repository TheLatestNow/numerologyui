<script>
    export let grid = Array(3)
        .fill()
        .map(() => Array(3).fill(""));

    const CELESTIAL_BODIES = {
        "1": "Sun: King",
        "2": "Moon: Queen",
        "3": "Jupiter: Councellor",
        "4": "Pluto: Mysterious",
        "5": "Mercury: Prince",
        "6": "Venus: Devil's Guru",
        "7": "Neptune: Saint",
        "8": "Saturn: Judge",
        "9": "Mars: Commander",
    };
</script>

<table>
    {#each grid as row, i}
        <tr>
            {#each row as cell, j}
                <td class="cell">
                    {#each cell.split("") as digit}
                        <div class="celestial">
                            {digit}
                            <br />
                            {CELESTIAL_BODIES[digit]}
                        </div>
                    {/each}
                </td>
            {/each}
        </tr>
    {/each}
</table>

<style>
    table {
        margin: 2em auto;
        border-collapse: collapse;
    }
    td {
        width: 3em;
        height: 3em;
        border: 1px solid #ccc;
        text-align: center;
        vertical-align: middle;
        background-color: #f5f5f5;
        font-size: 1.5em;
        position: relative;
    }
    .celestial {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 0.5em;
        text-align: center;
    }
</style>