from pathlib import Path

from oj import Problem


PROBLEM_TITLE = 'art'

DIR_PATH = Path(__file__).parent
DIR_NAME = PROBLEM_TITLE
ZIP_NAME = PROBLEM_TITLE+'.zip'


lines = [
    '#########################################',
    '#           ..          :..             #',
    '#         .#@@%=      .@@@@@%#.         #',
    '#        +@%%%%@@*    *@@#=@%@:         #',
    '#       .%@%@%@##+    %@@@%@%%          #',
    '#         =+@%@%**.  .=*@%@*+:          #',
    '#        =@@@%%@@%:  #@@%%@@#           #',
    '#         .:*@%@=-----=@%@#*-           #',
    '#         .=+@@%:.   .:@@%+=:           #',
    '#       -+-             .   :++:        #',
    '# .+===-:                      :-=====  #',
    '# :*     :                          :+  #',
    '#   #+===-                    =+=-=+-   #',
    '#  :*                              #    #',
    '#  #.                              -=   #',
    '#  %           :@= ..  %*          .#   #',
    '# *:            . -+%=:.            +-  #',
    '# %                *=+              .#  #',
    '# %                            .     %  #',
    '#########################################',
]


p = Problem(PROBLEM_TITLE)

p.testcases['1'].output.write('\n'.join(lines))

p.extract_as_dir(DIR_PATH / DIR_NAME)
p.extract_as_zip(DIR_PATH / ZIP_NAME)
