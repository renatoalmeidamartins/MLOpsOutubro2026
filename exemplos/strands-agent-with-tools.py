from strands import Agent, tool
from strands.vended_tools import file_editor
from strands_tools import generate_image

@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())

agent = Agent(tools=[letter_counter, file_editor, generate_image])
agent('E ai tudo bem??')
agent('Desenhe a logo da VW num estilo de salvador Dali')
agent('Quantas letras R tem aqui nesta frase: "o rato roeu a roupa do rei de roma"? Escreva a resposta no arquivo answer.txt. Desenhe o numero da resposta num alfabeto infantil')