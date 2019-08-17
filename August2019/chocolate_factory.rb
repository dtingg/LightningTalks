# Chocolate Factory Program
# Tracks manufacturing and sales of chocolate bars at the factory during a week

# Introduce the program to the user
puts "Welcome to Dianna's Chocolate Factory Program!"
puts 'The factory is open for manufacturing and sales three days a week.'
puts 'It produces and sells both organic milk chocolate and dark chocolate bars.'
puts "\nPlease enter the following information."

# Make an array to keep track of all the days
factory_days = []

# Number of days per week that the factory is open
operating_days = 3

# Create a custom class to hold information about each day
class Day
  attr_accessor :name, :milk_prod, :dark_prod, :milk_sold, :dark_sold,
                :milk_prod_cost, :milk_sell_price, :dark_prod_cost, :dark_sell_price

  def initialize(name, milk_prod, dark_prod, milk_sold, dark_sold)
    @name = name
    @milk_prod = milk_prod
    @dark_prod = dark_prod
    @milk_sold = milk_sold
    @dark_sold = dark_sold
    @milk_prod_cost = 2.00
    @milk_sell_price = 3.00
    @dark_prod_cost = 3.00
    @dark_sell_price = 5.00
  end

  # Calculate daily revenue (income from sales) for milk and dark chocolate
  def calc_revenue
    milk_rev = milk_sold * milk_sell_price
    dark_rev = dark_sold * dark_sell_price
    milk_rev + dark_rev
  end

  # Calculate daily production cost for milk and dark chocolate
  def calc_prod_cost
    milk_cost = milk_prod * milk_prod_cost
    dark_cost = dark_prod * dark_prod_cost
    milk_cost + dark_cost
  end

  # Calculate daily profit (revenue - production cost) for milk and dark chocolate
  def calc_profit
    calc_revenue - calc_prod_cost
  end
end

# Make sure that the user enters an integer
def check_input
  Integer(gets.chomp)
rescue ArgumentError
  print 'Error. Please enter an integer: '
  retry
end

# Get user input for each day
(1..operating_days).each do |i|
  puts "\nDay #{i}"

  print 'Number of milk chocolate bars produced: '
  milk_prod = check_input

  print 'Number of dark chocolate bars produced: '
  dark_prod = check_input

  print 'Number of milk chocolate bars sold: '
  milk_sold = check_input

  print 'Number of dark chocolate bars sold: '
  dark_sold = check_input

  # Create a new instance of the Day class
  factory_days.push(Day.new("Day #{i}", milk_prod, dark_prod, milk_sold, dark_sold))
end

puts "\nWEEKLY SUMMARY"
puts 'Total revenue for each day:'

# Print total revenue for each day.
factory_days.each do |day|
  printf("%s: $%.2f\n", day.name, day.calc_revenue)
end

# Find which days had the highest production cost
prod_costs = {}

factory_days.each do |day|
  prod_costs[day.name] = day.calc_prod_cost
end

max_prod_cost = prod_costs.values.max

max_prod_days = prod_costs.select do |_day, cost|
  cost == max_prod_cost
end

printf("\nThe highest production cost of $%.2f was on %s.\n",
       max_prod_cost, max_prod_days.keys.join(', '))

# Find the least number of milk chocolate bars sold and which days
daily_milk_sold = {}

factory_days.each do |day|
  daily_milk_sold[day.name] = day.milk_sold
end

lowest_milk_sold = daily_milk_sold.values.min

lowest_milk_days = daily_milk_sold.select do |_day, bars|
  bars == lowest_milk_sold
end

printf("The least number of milk chocolate bars sold was %d on %s.\n",
       lowest_milk_sold, lowest_milk_days.keys.join(', '))

# Find the average profit per day of the week
daily_profits = []

factory_days.each do |day|
  daily_profits.push(day.calc_profit)
end

printf("Average profit per day of the week: $%.2f\n", daily_profits.sum / operating_days)

# Figure out the total cost of production for the week
total_prod_cost = 0.0

factory_days.each do |day|
  total_prod_cost += day.calc_prod_cost
end

printf("Total cost of production for the week: $%.2f\n", total_prod_cost)

# Figure out total revenue for dark chocolate during the week
total_rev_dark = 0.0

factory_days.each do |day|
  total_rev_dark += day.dark_sold * day.dark_sell_price
end

printf("Total revenue earned by selling dark chocolate for the week: $%.2f\n", total_rev_dark)

# Find difference between revenue amounts for milk and dark chocolate bars
weekly_milk_rev = 0.0
weekly_dark_rev = 0.0

factory_days.each do |day|
  weekly_milk_rev += day.milk_sold * day.milk_sell_price
  weekly_dark_rev += day.dark_sold * day.dark_sell_price
end

print 'During the week, the factory earned '

result = weekly_milk_rev <=> weekly_dark_rev

case result
when -1
  printf("$%.2f more revenue from selling dark chocolate bars than from selling milk chocolate bars.\n",
         weekly_dark_rev - weekly_milk_rev)
when 0
  print "the same amount of revenue from selling milk chocolate and dark chocolate bars.\n"
when 1
  printf("$%.2f more revenue from selling milk chocolate bars than from selling dark chocolate bars.\n",
         weekly_milk_rev - weekly_dark_rev)
else
  print 'an unknown amount of revenue.'
end

puts "\nThank you for using Dianna's Chocolate Factory Program!"
