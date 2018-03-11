# Pinterest t3

# You are working as a backend engineer for acme.com. Recently, various users started abusing the company's API server with a flood of requests, and your team has decided to limit the rate at which a user can access certain API endpoints.

# The domain api.acme.com is served by an application server, placed behind an Nginx frontend proxy. To study the effectiveness of various rate-limiting algorithms with realistic traffic, you have collected several Nginx access logfiles (available at /home/candidate/candidate_files/py/inputs), where Nginx records each request to the API server. The structure of the access logfile is described in /home/candidate/candidate_files/py/log_structure.txt.

# Although many rate-limiting algorithms exist, you are interested in a sliding-window strategy, which limits the number of API calls to a maximum of 15 requests per second, per IP address. This means that for an arbitrary window of one-second duration, the API server responds to 15 or fewer API requests, per IP address.

# Write a function rate_limit_traffic that simulates the sliding-window limiter described above. Specifically, the function accepts the path of the Nginx access logfile, and returns a list of integers representing the request_id of the requests that are rejected by the rate-limiter, e.g., [23, 24, 25, 70, 71, 73, 74].


# Additional requirements

# The duration of the sliding-window is exactly one second, and includes both extremes of the interval.

# Requests that are rejected also count towards the limit of 15 per second.

# Requests from the IP address 123.221.14.56 should never be rate-limited, because it's an IP used by the internal Acme crawler that indexes the site.

# Requests to any URL starting with /administrator/ should never be rate-limited, because they correspond to the administrator pages of the Acme site.


# Assumptions
# All entries in the log file will be chronologically ordered.
# There are no simultaneous requests.
# Requests to administrator pages do not count towards the limit of 15 per second for that ip.
# All fields described in log_structure.txt are guaranteed to be present, and have a valid value.
# The log_path supplied to the rate_limit_traffic function is guaranteed to point to a file that exists, and can be read.


# Answer:



# rate_limit_traffic

# """Write your solution in this file.

# You can execute and test your answer by pressing 'Try Answer' in the side panel,
# or by running `python test_answer.py <test_case_path>` on the command line.

# For example:
#     python test_answer.py inputs/large.json
# """

def rate_limit_traffic(log_path):
	"""Implement your solution here.

	Arguments:
	    log_path: String with path of Nginx access logfile.

	Returns:
	    A list of integers, representing the IDs of the rejected requests.
	"""
	rejected_requests = [] # this returns result 
	ip_ts_map 	= {}   # ip to time_stamp map
	request_ip_ts 	= []   # (request_id, rremote_ip_addr, time_stamps) considered only (admin and specific IPs ignored)
	
	with open(log_path) as f:
		for line in f:
			words = line.split()
			if ('123.221.14.56' == words[1]) or ("administrator" in words[4]): # skipping admin and specific IP.
				continue
			else:
				request_ip_ts.append([words[0], words[1], words[2]]) # request_id, remote_addr, time_stamp

	size = len(request_ip_ts)
	print ("Size is ", size)

	first_ts, current_ts, sz = 0, 0, []

	for i in range(0, size):
		request_ip_ts_tuple = request_ip_ts[i] # tuple: (request_id, remote_ip_addr, time_stamps)
		# print(request_ip_ts_tuple)

		request_id, remote_ip_addr, time_stamps = request_ip_ts_tuple[0], request_ip_ts_tuple[1], request_ip_ts_tuple[2]

		if remote_ip_addr not in ip_ts_map: # remote_ip_addr not in map
			ip_ts_map[remote_ip_addr] = []
			ip_ts_map[remote_ip_addr].append(time_stamps)
		
		else:
			if len(ip_ts_map[remote_ip_addr]) < 15:
				ip_ts_map[remote_ip_addr].append(time_stamps)
			
			else:

				first_ts = ip_ts_map[remote_ip_addr][0] 
				current_ts = time_stamps # time stamp

				sz = len(ip_ts_map[remote_ip_addr]) # 

				while ((float(current_ts) - float(first_ts)) >= 1) and sz > 0:
					ip_ts_map[remote_ip_addr].pop(0)
					first_ts = ip_ts_map[remote_ip_addr][0]	
					sz -= 1

				if len(ip_ts_map[remote_ip_addr]) >= 15:
					rejected_requests.append(int(request_id)) # request_id appended
					ip_ts_map[remote_ip_addr].append(time_stamps)
				
				else:
					ip_ts_map[remote_ip_addr].append(time_stamps)

	return rejected_requests

expected_out = [36, 38, 40, 42, 44, 45, 47, 48, 49, 51, 52, 54, 57, 58, 59, 61, 62, 67, 68, 69,
70, 72, 73, 76, 77, 79, 91, 94, 95, 96, 99, 100, 104, 105, 106, 107, 109, 114, 
118, 119, 122, 124, 125, 127, 128, 129, 134, 136, 138, 139, 140, 141, 142, 143, 
145, 147, 148, 149, 150, 152, 153, 157, 159, 163, 164, 165, 171, 172, 176, 177, 
183, 187, 188, 189, 190, 198, 201, 203, 207, 213, 214, 217, 220, 227]

print('Expected output: ', expected_out)
print('Expected length: ', len(expected_out))

log_path = "./large_log_path.log"
output = rate_limit_traffic(log_path)
print('Real output: ', output)
print('Real output length: ', len(output))
















