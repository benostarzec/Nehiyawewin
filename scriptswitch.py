# -*- coding: UTF-8 -*-
#syll->rom

correspondences = {
    "ᐁ": "ê", "ᐃ": "i", "ᐅ": "o", "ᐊ": "a", "ᐄ": "î", "ᐆ": "ô", "ᐋ": "â",
    "ᐍ": "wê", "ᐏ": "wi", "ᐓ": "wo", "ᐘ": "wa", "ᐑ": "wî", "ᐕ": "wô", "ᐚ": "wâ", "ᐤ": "w",
    "ᐯ": "pê", "ᐱ": "pi", "ᐳ": "po", "ᐸ": "pa", "ᐲ": "pî", "ᐴ": "pô", "ᐹ": "pâ", "ᑊ": "p",
    "ᐻ": "pwê", "ᐽ": "pwi", "ᑁ": "pwo", "ᑅ": "pwa", "ᐿ": "pwî", "ᑃ": "pwô", "ᑇ": "pwâ",
    "ᑌ": "tê", "ᑎ": "ti", "ᑐ": "to", "ᑕ": "ta", "ᑏ": "tî", "ᑑ": "tô", "ᑖ": "tâ", "ᐟ": "t",
    "ᑘ": "twê", "ᑚ": "twi", "ᑞ": "to", "ᑢ": "ta", "ᑜ": "twî", "ᑠ": "tô", "ᑤ": "tâ",
    "ᑫ": "kê", "ᑭ": "ki", "ᑯ": "ko", "ᑲ": "ka", "ᑮ": "kî", "ᑰ": "kô", "ᑳ": "kâ", "ᐠ": "k",
    "ᑵ": "kwê", "ᑷ": "kwi", "ᑻ": "kwo", "ᑿ": "kwa", "ᑹ": "kwî", "ᑽ": "kwô", "ᒁ": "kwâ",
    "ᒉ": "cê", "ᒋ": "ci", "ᒍ": "co", "ᒐ": "ca", "ᒌ": "cî", "ᒎ": "cô", "ᒑ": "câ", "ᐨ": "c",
    "ᒓ": "cwê", "ᒕ": "cwi", "ᒙ": "cwo", "ᒝ": "cwa", "ᒗ": "cwî", "ᒛ": "cwô", "ᒟ": "cwâ",
    "ᒣ": "mê", "ᒥ": "mi", "ᒧ": "mo", "ᒪ": "ma", "ᒦ": "mî", "ᒨ": "mô", "ᒫ": "mâ", "ᒼ": "m",
    "ᒭ": "mwê", "ᒯ": "mwi", "ᒳ": "mwo", "ᒷ": "mwa", "ᒱ": "mwî", "ᒵ": "mwô", "ᒹ": "mwâ",
    "ᓀ": "nê", "ᓂ": "ni", "ᓄ": "no", "ᓇ": "na", "ᓃ": "nî", "ᓅ": "nô", "ᓈ": "nâ", "ᐣ": "n",
    "ᓊ": "nwê", "ᓌ": "nwa", "ᓎ": "nwâ",
    "ᓭ": "sê", "ᓯ": "si", "ᓱ": "so", "ᓴ": "sa", "ᓰ": "sî", "ᓲ": "sô", "ᓵ": "sâ", "ᐢ": "s",
    "ᓷ": "swê", "ᓹ": "swi", "ᓽ": "swo", "ᔁ": "swa", "ᓻ": "swî", "ᓿ": "swô", "ᔃ": "swâ",
    "ᔦ": "yê", "ᔨ": "yi", "ᔪ": "yo", "ᔭ": "ya", "ᔩ": "yî", "ᔫ": "yô", "ᔮ": "yâ", "ᕀ": "y", "ᐝ": "y",
    "ᔰ": "ywê", "ᔲ": "ywi", "ᔶ": "ywo", "ᔺ": "ywa", "ᔴ": "ywî", "ᔸ": "ywô", "ᔼ": "ywâ",
    "ᐦ": "h", "ᕽ": "hk", "ᓬ": "l", "ᕒ": "r", "᙮": "."
}

def breakdown(text, script):
    #text should be cree in syllabics or romanization, with circumflex for length
    #sourcelang should be "syll" or "rom"
    if script == "syll":
        splittext = []
        for char in text:
            splittext += char
        rom = ""
        for char in splittext:
            if char in correspondences:
                rom += correspondences[char]
            else:
                print(char)
                rom += char
        return rom

if __name__ == '__main__':
    text = "ᓀᐦᐃᔭᐍᒧᐏᐣ"
    print(text, "\n", breakdown(text, "syll"))
