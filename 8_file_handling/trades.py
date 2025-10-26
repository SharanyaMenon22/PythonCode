
import datetime

class Trade:
    def __init__(self,
                 transaction_time,
                 order_id,
                 parent_order_id,
                 symbol,
                 price,
                 qty) -> None:
        
        self.transaction_time = transaction_time
        self.order_id = order_id
        self.parent_order_id = parent_order_id
        self.symbol = symbol
        self.price = price
        self.qty = qty
        self.child_trades = []        

    def __str__(self) -> str:
        s = (
            f'{self.transaction_time},'
            f'{self.order_id},'
            f'{self.parent_order_id},'
            f'{self.symbol},'
            f'{self.price},'
            f'{self.qty}'
        )
        return s.strip()

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
        
        trades[trade.order_id] = trade
        if trade.parent_order_id in trades:
            child_trades = trades[trade.parent_order_id].child_trades
            child_trades.append(trade)

    return trades


def parse_date_time(trade):
    try:
        tstr = trade.transaction_time
         # "14:30:15"
        hr, minutes, sec = tstr.split(":")
        time_obj = datetime.time(int(hr), int(minutes), int(sec))
        return datetime.datetime.combine(datetime.date.today(), time_obj)
    except (AttributeError, ValueError, TypeError) as e:
        # tstr was None, malformed, or conversion failed; return None to indicate parse failure
        print(f"Error parsing transaction time for the trade: '{trade}': {e}")
        return None
    
def calculate_secs(child_time, parent_time):
    if child_time is None or parent_time is None:
        return 'N/A'
    else:
        secs = (child_time - parent_time).total_seconds()
        return f'{secs:.0f}'
            

def calculate_time_metrics(trades, out_file):

    file = open(out_file, 'w')
    file.write('OrderId,ParentOrderId,Symbol,Price,Qty,TimeInSeconds\n')
    for trade in trades.values():
        if len(trade.child_trades) == 0:
            continue
        parent_transaction_time = parse_date_time(trade)
        # print(f"OrderID: {trade.orderId}")
        for child in trade.child_trades:
            child_transaction_time = parse_date_time(child)
            secs = calculate_secs(child_transaction_time, parent_transaction_time)            
            # print(f"OrderID:{child.orderId}, Time differnce in secs:{secs:.0f}")
            
            s = (
                f'{child.order_id},'
                f'{trade.order_id},'
                f'{trade.symbol},'
                f'{child.price},'
                f'{child.qty},'
                f'{secs}\n'
            )

            file.write(s)                        



def main():
    # read the file.
    trades = load_trades('8_file_handling\\equity_trades.csv')
    calculate_time_metrics(trades, "8_file_handling\\order_latency.csv")    


if __name__ == '__main__':
    main()