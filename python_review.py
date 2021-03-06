"""
Write a program that checks if a given year is a leap year

A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.

For example,

1999 is not a leap year 2000 is a leap year 2004 is a leap year

"""
from ipaddress import ip_address, IPv6Address, IPv4Address
import random
import string

def check_leap_year(year):

	# if the year is a century year
    if str(year).endswith("00") and year % 400 == 0:
        return True
    if year % 4 == 0:
        return True
    return False

years = [ random.randint(1000,5000) for i in range(20)]
for year in years:
    print(f'{year} {"is" if check_leap_year(year) else "is not"} a leap year')


# Write a program that finds the amount of vowels and consonants across all texts (aggregated total).
# Answer the following:
# do all the texts together have more consonants or vowels?
# consonants: B, C, D, F, G, J, K, L, M, N, P, Q, S, T, V, X, Z and often H, R, W, Y.
# vowels: AEIOU

TXT1 = 'A vowel is a syllabic speech sound pronounced without any stricture in the vocal tract. Vowels are one of the two principal classes of speech sounds, the other being the consonant. Vowels vary in quality, in loudness and also in quantity (length). They are usually voiced and are closely involved in prosodic variation such as tone, intonation and stress.\nThe word vowel comes from the Latin word vocalis, meaning "vocal" (i.e. relating to the voice). In English, the word vowel is commonly used to refer both to vowel sounds and to the written symbols that represent them (a, e, i, o, u, and sometimes y).'
TXT2 = 'In articulatory phonetics, a consonant is a speech sound that is articulated with complete or partial closure of the vocal tract. Examples are [p], pronounced with the lips; [t], pronounced with the front of the tongue; [k], pronounced with the back of the tongue; [h], pronounced in the throat; [f] and [s], pronounced by forcing air through a narrow channel (fricatives); and [m] and [n], which have air flowing through the nose (nasals). Contrasting with consonants are vowels.\nSince the number of speech sounds in the world\'s languages is much greater than the number of letters in any one alphabet, linguists have devised systems such as the International Phonetic Alphabet (IPA) to assign a unique and unambiguous symbol to each attested consonant. The English alphabet has fewer consonant letters than the English language has consonant sounds, so digraphs like ???ch???, ???sh???, ???th???, and ???ng??? are used to extend the alphabet, though some letters and digraphs represent more than one consonant. For example, the sound spelled ???th??? in "this" is a different consonant from the ???th??? sound in "thin". (In the IPA, these are [??] and [??], respectively.)\n\n'
TXT3 = 'An alphabet is a standardized set of basic written symbols or graphemes (called letters) that represent the phonemes of certain spoken languages. Not all writing systems represent language in this way; in a syllabary, each character represents a syllable, for instance, and logographic systems use characters to represent words, morphemes, or other semantic units.The first fully phonemic script, the Proto-Canaanite script, later known as the Phoenician alphabet, is considered to be the first alphabet, and is the ancestor of most modern alphabets, including Arabic, Cyrillic, Greek, Hebrew, Latin, and possibly Brahmic. It was created by Semitic-speaking workers and slaves in the Sinai Peninsula (as the Proto-Sinaitic script), by selecting a small number of hieroglyphs commonly seen in their Egyptian surroundings to describe the sounds, as opposed to the semantic values, of their own Canaanite language. Peter T. Daniels, however, distinguishes an abugida or alphasyllabary, a set of graphemes that represent consonantal base letters which diacritics modify to represent vowels (as in Devanagari and other South Asian scripts), an abjad, in which letters predominantly or exclusively represent consonants (as in the original Phoenician, Hebrew or Arabic), and an "alphabet", a set of graphemes that represent both vowels and consonants. In this narrow sense of the word the first true alphabet was the Greek alphabet, which was developed on the basis of the earlier Phoenician alphabet.\nOf the dozens of alphabets in use today, the most popular is the Latin alphabet, which was derived from the Greek, and which many languages modify by adding letters formed using diacritical marks.  While most alphabets have letters composed of lines (linear writing), there are also exceptions such as the alphabets used in Braille. The Khmer alphabet (for Cambodian) is the longest, with 74 letters.Alphabets are usually associated with a standard ordering of letters. This makes them useful for purposes of collation, specifically by allowing words to be sorted in alphabetical order. It also means that their letters can be used as an alternative method of "numbering" ordered items, in such contexts as numbered lists and number placements.'


def count_vowels_and_consonants(str1 = '', str2 = '', str3 = ''):
    str1 = TXT1.translate(str.maketrans('', '', string.punctuation)).lower()

    str2 = TXT2.translate(str.maketrans('', '', string.punctuation)).lower()

    str3 = TXT3.translate(str.maketrans('', '', string.punctuation)).lower()

    total_str = str1 + str2 + str3
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for x in total_str:
        if x in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    print(f'There are a total of {consonant_count} consonants, and {vowel_count} vowels')

    if consonant_count > vowel_count:
        print('There are more consonants than vowels')
    elif consonant_count == vowel_count:
        print('There are equal amounts of consonants and vowels')
    else:
        print('There are more vowels than consonants which is really weird')

count_vowels_and_consonants(TXT1, TXT2, TXT3)

# An IPv4 address has the following format: x . x . x . x where x is called an octet and must be a decimal value between 0 and 255. Octets are separated by periods. (0.0.0.0 - 255.255.255.255  (where each decimal point is 1-3 numbers between 0-9))

# An IPv6 (Normal) address has the following format: y : y : y : y : y : y : y : y where y is called a segment and can be any hexadecimal value between 0 and FFFF. The segments are separated by colons - not periods. (where y is four values that can be 0-9 or a-Z)

# ipv4 examples:
# - 19.117.63.126
# - 127.0.0.1
# ipv6 examples:
# - 2001 : db8: 3333 : 4444 : 5555 : 6666 : 7777 : 8888
# - 2001 : db8 : 3333 : 4444 : CCCC : DDDD : EEEE : FFFF
# Write a function  to determine if the ip address is a valid ip4 or a valid ip6.
newip = '19.117.63.258'
newip2 = '2001:0db8:0a0b:12f0:0000:0000:0000:0001'


def ipv4_or_ipv6(ip):
    try:
        if isinstance(ip_address(ip), IPv4Address):
            print("IPv4")
        if isinstance(ip_address(ip), IPv6Address):
            print("IPv6")
    except ValueError:
        print("Invalid IP Address")

ipv4_or_ipv6(newip2)
ipv4_or_ipv6(newip)
