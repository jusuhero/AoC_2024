$lines = Get-Content "inputs/day1"

$left = @(); $right = @()

foreach($line in $lines)
{
  $parts = $line -split '\s+'
  $left += $parts[0]; $right += $parts[1]
}

$total_p1 = 0; $total_p2 = 0
$left = $left | Sort-Object; $right = $right | Sort-Object 

for($i = 0; $i -lt $left.Count; $i++)
{
  $total_p1 += [math]::Abs($left[$i] - $right[$i])
}

foreach($num in $left)
{
  $count = ($right | Where-Object { $_ -eq $num }).Count
  $similarity = [int]$num * $count 
  $total_p2 += $similarity
}

Write-Output "Lösung Part 1: $total_p1 `nLösung Part 2: $total_p2"
