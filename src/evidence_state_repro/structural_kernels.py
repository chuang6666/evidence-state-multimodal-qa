"""Unchanged numerical kernels used for the frozen structural comparison."""
import numpy as np

def binary_ap_auc(y,s):
    """Standard threshold-group AP and pairwise AUC with half credit for ties."""
    order=np.argsort(-s,kind='stable')
    yy=y[order]; ss=s[order]
    end=np.r_[np.flatnonzero(np.diff(ss)!=0),len(ss)-1]
    tp=np.cumsum(yy)[end]
    fp=end+1-tp
    dpos=np.diff(np.r_[0,tp]); dneg=np.diff(np.r_[0,fp])
    ap=np.sum(dpos*(tp/(end+1)))/tp[-1]
    # Descending groups: each positive outranks all negatives below its group.
    auc=np.sum(dpos*(fp[-1]-fp+0.5*dneg))/(tp[-1]*fp[-1])
    return float(ap),float(auc)

def metrics(y,s,q):
    order=np.lexsort((q,-s))
    return np.array([y[order[:220]].sum()/220, y[order[:220]].sum()/y.sum(),
                     *binary_ap_auc(y,s)],float)
