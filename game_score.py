class Ranking:

  def __init__(self, scores = []):
    self.__scores = scores

  def getRanking(self):
    return self.__scores

  def getHighestScore(self):
    if len(self.__scores) == 0:
      raise ValueError('There are no scores in the ranking')

    return max(self.__scores)

  def getBestScores(self, limit=1):
    if limit <= 0:
      raise ValueError('Invalid limit')

    if len(self.__scores) == 0:
      raise ValueError('There are no scores in the ranking')

    scoresLength = len(self.__scores)

    if limit > scoresLength:
      limit = scoresLength
    
    scores = self.__scores.copy()
    scores.sort()
    return scores[:limit]

  def addScore(self, score):
    if (type(score) == list):
      self.__scores += score
    else:
      self.__scores.append(score)

  def getLatestScore(self):
    return self.__scores[-1]

if __name__ == '__main__':
  # s = Ranking()
  s = Ranking([200, 300, 400])

  s.addScore(250)
  s.addScore([210, 360])

  print(s.getHighestScore())
  print(s.getBestScores(3))
  print(s.getLatestScore())
  print(s.getRanking())
