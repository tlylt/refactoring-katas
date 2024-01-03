// Thoughts

// It is not exactly all nested conditionals, but the ones that show uneven
// distribution of work, meaning the if leg and the else leg doesn't happen
// roughly with the same possibility. If so, use early return to reduce the
// scope of the mutable variable, and utimately remove it.

// In many cases, the refactoring may involve reversing the
// conditionals while constructing the guard clause.

// If multiple branches return the same result,
// apply consolidate-conditional-expression with OR

function payAmount(employee, workHours) {
  if (employee.isSeparate) {
    return { amount: 0, reasonCode: 'SEP' };
  }

  if (employee.isRetired) {
    return { amount: 0, reasonCode: 'RET' };
  }

  // logic to compute amount
  payroll.preparePayment(employee.id);
  employee.startDate = payroll.startDate;
  const bonuses = employee.bonus(workHours) + payroll.benefit(employee);
  log.addBonuses(bonuses, employee);
  return computeRegularPayAmount(employee, bonuses);
}
