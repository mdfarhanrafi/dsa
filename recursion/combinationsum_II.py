from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    ds = []
    candidates.sort()

    def findCombination(ind: int, target: int):
        if target == 0:
            print(ds)
            ans.append(ds[:])
            return
        for i in range(ind, len(candidates)):
            print(f"{ind} -> {i} ->  {len(candidates)}")
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            findCombination(i + 1, target - candidates[i])
            ds.pop()

    findCombination(0, target)
    return ans


if __name__ == "__main__":
    v = [1, 1, 1, 2, 2]
    comb = combinationSum2(v, 4)
    print(*comb)
