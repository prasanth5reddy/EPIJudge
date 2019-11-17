from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # DP : let A[i][j] be the number of combinations with scores s[0]...s[i] that result in final score of j
    # Time complexity = O(sn) where n = final_score and s = len(individual_play_scores)
    # Space complexity = O(sn)
    dp = [[1] + [0] * final_score] * len(individual_play_scores)
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            w_out = dp[i - 1][j] if i >= 0 else 0
            w = dp[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0
            dp[i][j] = w_out + w
    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
