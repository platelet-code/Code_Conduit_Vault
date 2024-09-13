def can_win_nim(stones: List[int]) -> bool:
    ret = 0
    for stone in stones:
        ret ^= stone
    return ret != 0


def can_first_player_win(stairs: List[int]) -> bool:
    ret = 0
    for i, stair in enumerate(stairs):
        if i % 2 == 0:
            ret ^= stair
    return ret != 0


def nim_game(allowed_moves: List[int], piles: List[int]) -> bool:
    @lru_cache(None)
    def sg(x: int) -> int:
        if x == 0:
            return 0
            
        possible_moves = [move for move in allowed_moves if x >= move]
        next_states = [sg(x - move) for move in possible_moves]
        
        mex = 0
        while mex in next_states:
            mex += 1
            
        return mex

    return reduce(lambda x, y: x ^ y, (sg(pile) for pile in piles), 0) != 0


def nim_game(piles: List[int]) -> bool:
    @lru_cache(None)
    def sg(x: int) -> int:
        if x == 0:
            return 0
        seen = set(sg(i) ^ sg(j) for i in range(x) for j in range(i + 1))
        
        mex = 0
        while mex in seen:
            mex += 1
        return mex

    return reduce(lambda x, y: x ^ y, (sg(pile) for pile in piles), 0) != 0
