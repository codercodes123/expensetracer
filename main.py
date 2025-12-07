"""
Real-Time Expense Tracker - Premium Banking Dashboard
AI for Bharat Week 2: Lazy Automation Submission
Built with Kiro Agent - The Ultimate Expense Tracker!
"""

import re
import time
import os
from datetime import datetime, timedelta
from collections import defaultdict

FILE_PATH = "expenses_raw.txt"
POLL_INTERVAL = 2


class C:
    G = "\033[92m"
    R = "\033[91m"
    Y = "\033[93m"
    B = "\033[94m"
    CY = "\033[96m"
    W = "\033[97m"
    M = "\033[95m"
    BD = "\033[1m"
    DM = "\033[2m"
    RS = "\033[0m"
    BG_G = "\033[42m"
    BG_R = "\033[41m"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def beep():
    if os.name == 'nt':
        try:
            import winsound
            winsound.Beep(800, 100)
            winsound.Beep(1000, 100)
        except:
            pass


def parse_amount(text):
    m = re.search(r'(?:Rs\.?|INR)\s*(\d+(?:,\d{3})*(?:\.\d{1,2})?)', text, re.I)
    return float(m.group(1).replace(',', '')) if m else None


def get_type(text):
    t = text.lower()
    if 'debited' in t or 'debit' in t:
        return 'debit'
    if 'credited' in t or 'credit' in t:
        return 'credit'
    return None


def get_merchant(text):
    for p in [r'(?:to|from)\s+([A-Z][A-Za-z0-9\s]+?)(?:\s+on|\s+Ref|\.)', r'(?:to|from)\s+([A-Z][A-Za-z0-9\s]{2,18})']:
        m = re.search(p, text, re.I)
        if m:
            name = re.sub(r'\s+(PVT|LTD|INDIA).*$', '', m.group(1).strip(), flags=re.I)
            return name[:15].title()
    return "Unknown"


def parse_line(line):
    try:
        line = line.strip()
        if not line:
            return None
        parts = line.split(',', 2)
        if len(parts) < 3:
            return None
        ts = datetime.strptime(parts[0].strip(), '%Y-%m-%d %H:%M:%S')
        amt = parse_amount(parts[2])
        typ = get_type(parts[2])
        if not amt or not typ:
            return None
        return (ts, parts[1].strip(), amt, typ, get_merchant(parts[2]))
    except:
        return None


def load(path):
    txns = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                p = parse_line(line)
                if p:
                    txns.append(p)
    except:
        pass
    return txns


def daily_data(txns):
    d = defaultdict(lambda: {'cr': 0.0, 'dr': 0.0})
    for ts, _, amt, typ, _ in txns:
        k = ts.strftime('%Y-%m-%d')
        if typ == 'credit':
            d[k]['cr'] += amt
        else:
            d[k]['dr'] += amt
    return dict(d)


def get_savings_comparison(txns):
    today = datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    dd = daily_data(txns)
    today_spent = dd.get(today, {}).get('dr', 0.0)
    yesterday_spent = dd.get(yesterday, {}).get('dr', 0.0)
    has_today = today in dd
    has_yesterday = yesterday in dd
    return today_spent, yesterday_spent, has_today, has_yesterday


def print_savings_quote(txns):
    today_spent, yesterday_spent, has_today, has_yesterday = get_savings_comparison(txns)
    print()
    if not has_yesterday:
        print(f"  {C.Y}This is your first day — Let's make it a good one!{C.RS}")
    elif today_spent < yesterday_spent:
        diff = yesterday_spent - today_spent
        print(f"  {C.G}Congratulations! You have saved Rs.{diff:,.2f} compared to yesterday!{C.RS}")
    elif today_spent == yesterday_spent:
        print(f"  {C.Y}Same spending as yesterday — Stay consistent!{C.RS}")
    else:
        diff = today_spent - yesterday_spent
        print(f"  {C.R}You have spent Rs.{diff:,.2f} more than yesterday — Tomorrow can be better!{C.RS}")


def dashboard(txns, new_tx=None):
    clear()
    
    tot_cr = sum(t[2] for t in txns if t[3] == 'credit')
    tot_dr = sum(t[2] for t in txns if t[3] == 'debit')
    net = tot_cr - tot_dr
    cnt_cr = sum(1 for t in txns if t[3] == 'credit')
    cnt_dr = sum(1 for t in txns if t[3] == 'debit')
    
    W = 78
    
    # HEADER
    print()
    print(f"{C.CY}+{'='*W}+{C.RS}")
    print(f"{C.CY}|{C.RS}{C.BD}{C.W}{'REAL-TIME EXPENSE TRACKER':^78}{C.RS}{C.CY}|{C.RS}")
    print(f"{C.CY}|{C.RS}{C.Y}{'Bank of Maharashtra - Premium Dashboard':^78}{C.RS}{C.CY}|{C.RS}")
    print(f"{C.CY}+{'='*W}+{C.RS}")
    
    # STATUS
    print(f"\n  {C.G}[LIVE]{C.RS} Watching...  Updated: {datetime.now().strftime('%H:%M:%S')}")
    
    # NEW TRANSACTION ALERT
    if new_tx:
        beep()
        ts, _, amt, typ, merch = new_tx
        if typ == 'credit':
            print(f"\n  {C.BG_G}{C.W}{C.BD} +++ NEW CREDIT RECEIVED! +++ {C.RS}")
            print(f"  {C.G}+Rs.{amt:,.2f} from {merch}{C.RS}")
        else:
            print(f"\n  {C.BG_R}{C.W}{C.BD} !!! NEW DEBIT ALERT !!! {C.RS}")
            print(f"  {C.R}-Rs.{amt:,.2f} to {merch}{C.RS}")
    
    # ACCOUNT SUMMARY
    print(f"\n{C.CY}+{'-'*W}+{C.RS}")
    print(f"{C.CY}|{C.RS}  {C.BD}ACCOUNT SUMMARY{C.RS}{' '*61}{C.CY}|{C.RS}")
    print(f"{C.CY}+{'-'*W}+{C.RS}")
    
    print(f"\n  {C.G}TOTAL RECEIVED{C.RS}        {C.R}TOTAL SPENT{C.RS}           {C.CY}NET BALANCE{C.RS}")
    print(f"  {C.G}{C.BD}Rs.{tot_cr:>13,.2f}{C.RS}      {C.R}{C.BD}Rs.{tot_dr:>13,.2f}{C.RS}      ", end="")
    if net >= 0:
        print(f"{C.G}{C.BD}+Rs.{net:>12,.2f}{C.RS}")
    else:
        print(f"{C.R}{C.BD}-Rs.{abs(net):>12,.2f}{C.RS}")
    
    print(f"  {C.DM}({cnt_cr} credits){C.RS}             {C.DM}({cnt_dr} debits){C.RS}              ", end="")
    print(f"{C.G}PROFIT!{C.RS}" if net >= 0 else f"{C.R}DEFICIT{C.RS}")
    
    # DAILY BREAKDOWN
    dd = daily_data(txns)
    today = datetime.now().strftime('%Y-%m-%d')
    dates = sorted(dd.keys(), reverse=True)[:7]
    
    print(f"\n{C.CY}+{'-'*W}+{C.RS}")
    print(f"{C.CY}|{C.RS}  {C.BD}DAILY BREAKDOWN{C.RS}{' '*61}{C.CY}|{C.RS}")
    print(f"{C.CY}+{'-'*W}+{C.RS}")
    print()
    
    for dt in dates:
        data = dd[dt]
        if dt == today:
            dt_label = f"{C.Y}TODAY{C.RS}"
        else:
            dt_label = datetime.strptime(dt, '%Y-%m-%d').strftime('%d %b')
        
        parts = []
        if data['dr'] > 0:
            parts.append(f"{C.R}Rs.{data['dr']:,.2f} Spent{C.RS}")
        if data['cr'] > 0:
            parts.append(f"{C.G}Rs.{data['cr']:,.2f} Received{C.RS}")
        
        if parts:
            print(f"  {dt_label}: {' / '.join(parts)}")
        else:
            print(f"  {dt_label}: No transactions")
    
    # RECENT TRANSACTIONS
    recent = sorted(txns, key=lambda x: x[0], reverse=True)[:7]
    
    print(f"\n{C.CY}+{'-'*W}+{C.RS}")
    print(f"{C.CY}|{C.RS}  {C.BD}RECENT TRANSACTIONS{C.RS}{' '*57}{C.CY}|{C.RS}")
    print(f"{C.CY}+{'-'*W}+{C.RS}")
    print()
    
    for ts, _, amt, typ, merch in recent:
        tm = ts.strftime('%d %b %H:%M')
        is_new = new_tx and ts == new_tx[0]
        new_badge = f" {C.Y}*NEW*{C.RS}" if is_new else ""
        
        if typ == 'credit':
            print(f"  {tm}  {C.G}+Rs.{amt:,.2f}{C.RS} from {merch}{new_badge}")
        else:
            print(f"  {tm}  {C.R}-Rs.{amt:,.2f}{C.RS} to {merch}{new_badge}")
    
    # SAVINGS QUOTE
    print_savings_quote(txns)
    
    # FOOTER
    print(f"\n{C.CY}+{'='*W}+{C.RS}")
    if net > 0:
        print(f"{C.CY}|{C.RS}  {C.G}You're saving Rs.{net:,.2f} this period! Keep it up!{C.RS}{' '*20}{C.CY}|{C.RS}")
    else:
        print(f"{C.CY}|{C.RS}  {C.Y}Tip: Review spending to find savings opportunities.{C.RS}{' '*24}{C.CY}|{C.RS}")
    print(f"{C.CY}+{'-'*W}+{C.RS}")
    print(f"{C.CY}|{C.RS}  Total: {len(txns)} txns  |  Bank of Maharashtra  |  Powered by Kiro{' '*17}{C.CY}|{C.RS}")
    print(f"{C.CY}+{'='*W}+{C.RS}")
    print(f"\n  {C.DM}Press Ctrl+C to exit | Auto-refresh: {POLL_INTERVAL}s{C.RS}\n")


def watch(path):
    print(f"\n  {C.CY}Starting Expense Tracker...{C.RS}")
    time.sleep(1)
    
    txns = load(path)
    last = len(txns)
    dashboard(txns)
    
    try:
        while True:
            time.sleep(POLL_INTERVAL)
            curr = load(path)
            
            if len(curr) > last:
                new = curr[-1]
                last = len(curr)
                txns = curr
                dashboard(txns, new)
            elif len(curr) != last:
                last = len(curr)
                txns = curr
                dashboard(txns)
                
    except KeyboardInterrupt:
        print(f"\n\n  {C.Y}Goodbye!{C.RS}")
        if txns:
            tc = sum(t[2] for t in txns if t[3] == 'credit')
            td = sum(t[2] for t in txns if t[3] == 'debit')
            print(f"\n  {C.BD}Final:{C.RS} {C.G}+Rs.{tc:,.2f}{C.RS} | {C.R}-Rs.{td:,.2f}{C.RS} | Net: Rs.{tc-td:,.2f}")
        print()


if __name__ == "__main__":
    watch(FILE_PATH)

# Dashboard built by Kiro Agent for AI for Bharat Week 2 - Lazy Automation
