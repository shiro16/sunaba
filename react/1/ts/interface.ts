interface Color {
    readonly rgb: string; // readonly は変更不可
    opacity: number;
    name?: string;  // ? は省略可
}
const turquoise: Color = { rgb: '00afcc', opacity: 1 };
turquoise.name = 'Turquoise Blue';
//turquoise.rgb = '03c1ff';
console.log(turquoise);

interface Status {
    level: number;
    maxHP: number;
    maxMP: number;
    [attr: string]: number;
}

const myStatus: Status = {
    level: 99,
    maxHP: 999,
    maxMP: 999,
    attack: 999,
    defense: 999,
};

console.log(myStatus);