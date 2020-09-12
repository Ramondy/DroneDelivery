# NOT IMPLEMENTED YET

# def fastMaxVal(toConsider, avail, memo = {}):
#     """Assumes toConsider a list of items, avail a weight, memo used by recursive calls
#     Returns a tuples of the total value of a solution to the 0/1 knapsack
#     problem and the items of that solution"""
#     if (len(toConsider), avail) in memo:
#         result = memo[(len(toConsider), avail)]
#     elif toConsider == [] or avail == 0:
#         result = (0, ())
#     elif toConsider[0].get_cost() > avail:
#         # Explore right branch only
#         result = maxVal(toConsider[1:], avail, memo)
#     else:
#         nextItem = toConsider[0]
#         # Explore left branch
#         withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.get_cost(), memo)
#         withVal += nextItem.get_value()
#         # Explore right branch
#         withoutVal, withoutToTake = maxVal(toConsider[1:], avail, memo)
#         # Explore better branch
#         if withVal > withoutVal:
#             result = (withVal, withToTake + (nextItem,))
#         else:
#             result = (withoutVal, withoutToTake)
#     memo[(len(toConsider), avail)] = result
#     return result