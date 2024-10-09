function romanToInt(s: string): number {
    let hashtable = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };
	
    let result = 0;

    for (let i = 0; i < s.length; i++) {
        if (i + 1 < s.length && hashtable[s[i]] < hashtable[s[i + 1]]) {
            result -= hashtable[s[i]];
        } else {
            result += hashtable[s[i]];
        }
    }

    return result;
};