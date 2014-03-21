from models import LotteryNumber, LotteryResult

def winnings(lottery_Number, lottery_result):
    lottoNum = set([lottery_Number.number1,
    			lottery_Number.number2,
    			lottery_Number.number3,
    			lottery_Number.number4,
    			lottery_Number.number5])

    resultNum = ([lottery_result.number1,
    			lottery_result.number2,
    			lottery_result.number3,
    			lottery_result.number4,
    			lottery_result.number5])

    return (lottoNum.intersection(resultNum), set([lottery_Number.ball]).intersection(set([lottery_result.ball])))
