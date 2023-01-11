import argparse
from HttpLogProcessor import HttpLogProcessor


class Main:

  def __init__(self):
    self.parser = argparse.ArgumentParser(description='Process some HTTP log files.')
    self.parser.add_argument('--lines', metavar='file', type=str, help='count the number of lines in a file')
    self.parser.add_argument('--status_codes', metavar='file', type=str, help='count the number of status codes in a file')
    self.parser.add_argument('--traffic', metavar='file', type=str, help='sum the traffic in bytes for all requests in a file')
    self.parser.add_argument('--unique_clients', metavar='file', type=str, help='Count the number of unique IP adresses')
    self.parser.add_argument('--most_active_clients', metavar='file', type=str, help='Calculate the top 3 most active IP addresses')
    self.parser.add_argument('--most_visited_paths', metavar='file', type=str, help='Calculate the top 3 most visited URLs')

  def run(self):
    args = self.parser.parse_args()
    
    if not args.lines or args.status_codes or args.traffic:
      raise Exception('Please provide an argument!')
    
    if args.lines:
      parser = HttpLogProcessor(args.lines)
      print(f'Number of lines in {args.lines}: {parser.get_total_lines()}')
    
    if args.traffic:
      parser = HttpLogProcessor(args.traffic)
      print(f'Total traffic in bytes in {args.traffic}: {parser.get_total_traffic()}')
    
    if args.status_codes:
      parser = HttpLogProcessor(args.status_codes)
      print(f'Number of status codes in {args.status_codes}: {parser.get_status_code_count()}')

    if args.unique_clients:
      parser = HttpLogProcessor(args.status_codes)
      print(f'Number of unique clients in {args.status_codes}: {parser.get_status_code_count()}')
      
    if args.most_active_clients:
      parser = HttpLogProcessor(args.status_codes)
      print(f'Number of most active clients in {args.status_codes}: {parser.get_status_code_count()}')
      
    if args.most_visited_paths:
      parser = HttpLogProcessor(args.status_codes)
      print(f'Most  in {args.status_codes}: {parser.get_status_code_count()}')

    
if __name__ == "__main__":
  main = Main()
  main.run()
