class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to hold anagram groups
        anagrams = {}

        # Go through each word in the input list
        for word in strs:
            # Sort the word to create a key; all anagrams will have the same sorted form
            sorted_word = ''.join(sorted(word))

            # If this sorted form is already a key, append the word to its list
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                # Otherwise, start a new list with this word
                anagrams[sorted_word] = [word]

        # Convert the dictionary values to a list of lists (groups of anagrams)
        result = list(anagrams.values())

        return result
