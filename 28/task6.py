from typing import List


def MassVote(N: int, Votes: List[int]) -> str:
    """Receives the input number of candidates N >= 1 and an array containing N
    votes cast for the corresponding candidates.
    At the output, a line with the winner is formed.
    """
    total_votes = sum(Votes)
    max_votes = max(Votes)
    if max_votes / total_votes > 0.5:
        return f"majority winner {Votes.index(max_votes) + 1}"
    elif max_votes * 2 > total_votes:
        return f"minority winner {Votes.index(max_votes) + 1}"
    else:
        max_vote_count = Votes.count(max_votes)
        if max_vote_count == 1:
            return f"minority winner {Votes.index(max_votes) + 1}"
        else:
            return "no winner"
