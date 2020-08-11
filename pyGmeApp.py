import random
import curses

with open("snkDebug.txt", "a") as fi:

    s = curses.initscr()
    fi.write(f"s value = {s} \n")
    curses.curs_set(0)
    sh, sw = s.getmaxyx()
    fi.write(f"sh value:- {sh} \n")
    fi.write(f"sw value:- {sw} \n")
    w = curses.newwin(sh, sw, 0, 0)
    fi.write(f"w:- {w} \n")
    w.keypad(1)
    w.timeout(100)
    fi.write(f"w :- {w} \n")
    snk_x = int(sw/4)
    fi.write(f"snk_x:- {snk_x} \n")
    snk_y = int(sh/2)
    fi.write(f"snk_y:- {snk_y} \n")
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    fi.write(f"Snake val :- {snake} \n")
    food = [int(sh/2), int(sw/2)]
    fi.write(f"food val :- {food} \n")
    fi.write(f"food[0] :- {food[0]} \n")
    fi.write(f"food[1] :- {food[1]} \n")
    w.addch(food[0], food[1], curses.ACS_PI)
    fi.write(f"w :- {w} \n")
    key = 454
    prevKey = key
    fi.write(f"curses.KEY_RIGHT:- {key} \n")
    while True:
        next_key = w.getch()
        fi.write(f"Entered while loop \n")
        fi.write(f"next_key:- {next_key} \n")
        key = key if next_key == -1 else next_key
        
        
        fi.write(f"Key :-{key} \n")
        fi.write(f"Before if condition:-----\n")
        fi.write(f"snake :- {snake} \n")
        fi.write(f"snake[0][0].....{snake[0][0]} \n")
        fi.write(f"[0, sh]......{[0, sh]} \n")
        fi.write(f"OR.... \n")
        fi.write(f"snake[0][1]......{snake[0][1]} \n")
        fi.write(f"[0, sw]......{[0, sw]} \n")
        fi.write(f"OR.... \n")
        fi.write(f"snake[0].......{snake[0]} \n")
        fi.write(f"snake[1:]......{snake[1:]} \n")
        if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
            fi.write(f"After if condition entered:---- \n")
            fi.write(f"snake[0][0].....{snake[0][0]} \n")
            fi.write(f"[0, sh]......{[0, sh]} \n")
            fi.write(f"OR.... \n")
            fi.write(f"snake[0][1]......{snake[0][1]} \n")
            fi.write(f"[0, sw]......{[0, sw]} \n")
            fi.write(f"OR.... \n")
            fi.write(f"snake[0].......{snake[0]} \n")
            fi.write(f"snake[1:]......{snake[1:]} \n")
            fi.write(f"in if where key :- {key} \n")
            curses.endwin()
            quit()

        new_head = [snake[0][0], snake[0][1]]
        fi.write(f"new_head :- {new_head} \n")
        fi.write("Key Decision")
        fi.write(f"{key} == {curses.KEY_DOWN}\n")
        fi.write(f"{key} == {curses.KEY_UP}\n")
        fi.write(f"{key} == {curses.KEY_LEFT}\n")
        fi.write(f"{key} == {curses.KEY_RIGHT}\n")
        if key == 456:
            fi.write(f"curses.KEY_DOWN :- {key} \n")
            new_head[0] += 1
            fi.write(f"new_head[0] :- {new_head[0]} \n")
        if key == 450:
            fi.write(f"curses.KEY_UP :- {key} \n")
            new_head[0] -= 1
            fi.write(f"new_head[0] :- {new_head[0]} \n")
        if key == 452:
            fi.write(f"curses.KEY_LEFT :- {key} \n")
            new_head[1] -= 1
            fi.write(f"new_head[1] :- {new_head[1]} \n")
        if key == 454:
            fi.write(f"curses.KEY_RIGHT :- {key} \n")
            new_head[1] += 1
            fi.write(f"new_head[1] :- {new_head[1]} \n")
        
        fi.write(f"key :- {key} \n")
        snake.insert(0, new_head)
        fi.write(f"new_head {new_head} \n")
        fi.write(f"snake :- {snake} \n")
        fi.write(f"food :- {food} \n")
        if snake[0] == food:
            food = None
            while food is None:
                fi.write(f"entered one more while condition")
                nf = [
                    random.randint(1, sh-1),
                    random.randint(1, sw-1)
                ]
                fi.write(f"nf :- {nf} \n")
                food = nf if nf not in snake else None
                fi.write(f"food :- {food} \n")
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            fi.write(f"tail value: {tail}\n")
            w.addch(tail[0], tail[1], ' ')
        fi.write(f"int(snake[0][0])  {int(snake[0][0])} \n")
        fi.write(f"int(snake[0][1]) {int(snake[0][1])} \n")
        fi.write(f"curses.ACS_CKBOARD  {curses.ACS_CKBOARD} \n")
        prevKey = key
        fi.write(f"prevKey :-{prevKey} \n")
        fi.write(f"---------------------------------------------- \n")
        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

