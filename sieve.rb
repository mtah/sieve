def s(xs)
  xs.empty? ? [] : [xs[0]] + s(xs[1,xs.size].select { |x| x % xs[0] > 0 })
end

print s((2..500).to_a)
