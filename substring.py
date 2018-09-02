

def maximal_matching_pair( s, substring_length, old_index=-1 ):
    '''
    find the first pair of matching substrings at least as long as the specified length
    '''
    if substring_length > len(s)/2:
        return (lensubstring_lengthgth, -1) # fail- futile to keep searching with this string

    head = s[:substring_length]
    tail = s[substring_length:]
    index = tail.find(head) 
    if index == -1:
        if substring_length > 2:
            return (substring_length-1, old_index) # success
        return (substring_length, index) # fail- failed on first 2 character substring attempt 
    
    return maximal_matching_pair(s, substring_length+1, index) # keep looking

def first_matching_substring_pair( s, start=0 ):
    '''
    returns the first matching substring pair of at least length 2 in the given string, 
    ignoring all characters of the string before the given start index 
    '''
    if start < 0:
        return () # invalid input: start must be non-negative

    if len(s[start:]) < 4:
        return () # fail: string too short to find matching substrings of minimal length 2

    minimal_substring_length = 2
    (length, distance) = maximal_matching_pair(s[start:], minimal_substring_length)
    if distance != -1:
        return (start, length, distance) # success
    
    return first_matching_substring_pair(s, start+1) # keep looking

def matching_substring_pairs( string ):
    '''
    returns a collection of consecutive substring pairs encoded as (start, length, distance) where
    * start is the index of the first character of the first substring of the matching substring pair,
    * length is the length of the substrings in the matching substring pair, and
    * distance is the distance from the end of the first substring to the begining of the second substring
    '''
    pairs = []
    pair = first_matching_substring_pair(string, 0)
    while pair:
        pairs.append(pair)
        (start, length, distance) = pair
        pair = first_matching_substring_pair(string, start+length)
    return pairs
    