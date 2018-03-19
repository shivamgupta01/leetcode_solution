
## Insert for train Table

# minutes = 122
# train_no = 1
#
# while (minutes<=1260):
#     if (minutes%60 == 0):
#         train_type = "express";
#     else:
#         train_type="regular"
#     print "('"+"SB"+('{:02d}{:02d}'.format(*divmod(minutes, 60)))+"',"+str(100)+"),"
#
#     minutes = minutes + 15
#     train_no = train_no + 1




train_no = 1

while(train_no<=122):
    print "(" + str(train_no) +","+"5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5"+",5),"
    train_no = train_no+1


# train_no = 1
#
# while (train_no <= 122):
#     print "`" + str(train_no) + "` INT NULL,"
#     train_no = train_no + 1
#
#







#
#
# while (minutes<=1260):
#     if (minutes%60 == 0):
#
#         train_type = "express";
#     else:
#         train_type="regular"
#     print "("+ str(train_no) +",'"+"NB"+('{:02d}{:02d}'.format(*divmod(minutes, 60)))+"','" +str(('{:02d}:{:02d}'.format(*divmod(minutes, 60))))+"','active','"+train_type+"'),"
#     minutes = minutes + 15
#     train_no = train_no + 1
#
#
# #Insert For Schedule Table
# minutes = 360
# interval = []
# while (minutes<=1260):
#     interval.append(minutes)
#     minutes = minutes+15
#
# station = 26
#
# train_no = 62
# for z in interval:
#     temp_time = z
#     station = 26
#     if temp_time%60 != 0:
#        while(station>1):
#             print "(" + str(train_no) + ",'" + str(station) + "','" + ('{:02d}:{:02d}'.format(*divmod(temp_time, 60))) + "'),"
#             temp_time = temp_time + 8
#             station = station -1
#
#     else:
#         while (station > 1):
#             print "(" + str(train_no) + ",'" + str(station) + "','" + ('{:02d}:{:02d}'.format(*divmod(temp_time, 60))) + "'),"
#             temp_time = temp_time + 28
#             station = station -5
#
#     train_no = train_no + 1
#
#
# # Insert for station table
# station_id = 1
# station_name = 97
# while (station_id<=26):
#     print "(" + str(station_id)+",'" +str(unichr(station_name))+"'),"
#     station_name = station_name + 1
#     station_id =station_id + 1
#
#
#

