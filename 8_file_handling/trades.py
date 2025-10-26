
import datetime

class Trade:
    def __init__(self,
                 transaction_time,
                 orderId,
                 parentOderId,
                 symbol,
                 price,
                 qty) -> None:
        
        self.transaction_time = transaction_time
        self.orderId = orderId
        self.parentOderId = parentOderId
        self.symbol = symbol
        self.price = price
        self.qty = qty
        self.child_trades = []        

    def __str__(self) -> str:
        return f"{self.transaction_time},{self.orderId},{self.parentOderId},{self.symbol},{self.price},{self.qty}"        

def parse_header(line):
    header = {}
    for index, part in enumerate(line.split(",")):
        header[part] = index
    return header



def load_trades(file_path):
    trades = {}
    file = open(file_path, 'r')
    header = {}
    for index, line in enumerate(file):
        if index == 0: # header.
            header = parse_header(line.strip('\n'))
            continue
        line = line.strip('\n')
        parts = line.split(',')
        # trade = Trade(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
        trade = Trade( parts[header['Transaction_Time']],
                      parts[header['OrderId']],
                      parts[header['ParentOrderId']],
                      parts[header['Symbol']],
                      parts[header['Price']],
                      parts[header['Qty']])
        
        trades[trade.orderId] = trade
        if trade.parentOderId in trades:
            child_trades = trades[trade.parentOderId].child_trades
            child_trades.append(trade)

    return trades


def parse_date_time(tstr):
    try:
        hr, min, sec = tstr.split(":")
        time_obj = datetime.time(int(hr), int(min), int(sec))
        return datetime.datetime.combine(datetime.date.today(), time_obj)
    except Exception as e:
        print(e)
        return None
    
def calculate_secs(child_time, parent_time):
    if child_time is None or parent_time is None:
        return 'N/A'
    else:
        secs = (child_time - parent_time).total_seconds()
        return f'{secs:.0f}'
            

def calculate_time_metrics(trades, out_file):

    file = open(out_file, 'w')
    file.write(f'OrderId,ParentOrderId,Symbol,Price,Qty,TimeInSeconds\n')
    for trade in trades.values():
        if len(trade.child_trades) == 0:
            continue
        parent_transaction_time = parse_date_time(trade.transaction_time)
        # print(f"OrderID: {trade.orderId}")
        for child in trade.child_trades:
            child_transaction_time = parse_date_time(child.transaction_time)
            secs = calculate_secs(child_transaction_time, parent_transaction_time)            
            # print(f"OrderID:{child.orderId}, Time differnce in secs:{secs:.0f}")
            file.write(f'{child.orderId},{trade.orderId},{trade.symbol},{child.price},{child.qty},{secs}\n')



def main():
    # read the file.
    trades = load_trades('8_file_handling\\equity_trades.csv')
    calculate_time_metrics(trades, "8_file_handling\\order_latency.csv")    


if __name__ == '__main__':
    main()