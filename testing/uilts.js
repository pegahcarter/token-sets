
const formatAllocation = (allocation) => {
  allocationBigNumber = new BigNumber(allocation)
  const allocationInWei = web3.utils.toWei(allocationBigNumber.toString(), 'ether');
  return new BigNumber(allocationInWei);
};
