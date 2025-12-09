full_dot = '●'
empty_dot = '○'
def create_character(character_name, strength, intelligence,charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string.'
    if len(character_name) > 10:
        return 'The character name is too long.'
    if " " in character_name:
        return 'The character name should not contain spaces.'
    
    stats = [strength, intelligence, charisma]

    if not all(isinstance(i, int) for i in stats):
        return 'All stats should be integers.'
    if not all(i>=1 for i in stats ):
        return'All stats should be no less than 1.'
    if not all(i <=4 for i in stats):
        return 'All stats should be no more than 4.'
    if sum(stats)!=7:
        return 'The character should start with 7 points.'
        
    def make_line(label,value):
        return label + " " + (full_dot * value) + (empty_dot *(10-value))
    return(
            character_name + "\n"+
            make_line("STR", strength) + "\n"+
            make_line("INT", intelligence) + "\n"+
            make_line("CHA", charisma) 
        )
print(create_character("ren",4,2,1))
