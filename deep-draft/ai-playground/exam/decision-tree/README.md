# Decision Tree 

- Version 1 Doesn't implement `min_samples_split`
- Version 2 Implements it
- The parameter `data` expects an `MxN` numpy array where 
- M is the number of samples and N-1 is the number of features of the each sample
- The last column of each row is an integer which indicates the label of that sample 
- All features are assumed to be floats/numbers
- The parameters `min_samples_leaf`, `min_samples_split`, `max_depth`
- are supposed to prevent overfitting
- `max_depth` is the maximum height of the tree
- If a branch has less than or equal to `min_sample_leaf` number of labels 
- then it will be a leaf node and will not create a new branch 
- If a branch has less than or equal to `min_samples_split` it will also 
- not split anymore. Usually, this is implemented when `depth` is set no `None`
- as with `SKLearn` package. However, in our case we never assume that `depth` with be 
- to a value other than an integer. 
- The predict function and evaluation methods were also purposely not implemented
- Only the "Gini Index" was used to measure the purity or how well the split is compared to other splits. 
- Of course there are other ways to measure but they are not implemented here.

```
def recursive_build_tree(node, min_samples_leaf, min_samples_split, max_depth, depth):
    left_branch, right_branch = node['two_branches']
    del(node['two_branches'])

    if len(left_branch) == 0 and len(right_branch) != 0:
        label = leaf_node_label(right_branch)
        node['left_label'] = label
        node['right_label'] = label
        return
    
    if len(left_branch) != 0 and len(right_branch) == 0:
        label = leaf_node_label(left_branch)
        node['left_label'] = label
        node['right_label'] = label
        return

    # left_branch and right_branch cannot be zero anymore
    # at this point
    if depth >= max_depth:
        node['left_label'] = leaf_node_label(left_branch) 
        node['right_label'] = leaf_node_label(right_branch)
        return
    
    if len(left_branch) <= min_samples_leaf:
        node['left_label'] = leaf_node_label(left_branch)
    else:
        if len(left_branch) > min_samples_split:
            node['left_label'] = select_best_split(left_branch)
            recursive_build_tree(node['left_label'], min_samples_leaf, 
                                 min_samples_split, max_depth, depth + 1)

    if len(right_branch) <= min_samples_leaf:
        node['right_label'] = leaf_node_label(right_branch)
    else:
        if len(left_branch) > min_samples_split:
            node['right_label'] = select_best_split(right_branch)
            recursive_build_tree(node['right_label'], min_samples_leaf,
                                 min_samples_split, max_depth, depth + 1)

def decisionTree(data, max_depth, min_samples_leaf=1, min_samples_split=1):
    root = select_best_split(data)
    recursive_build_tree(root, min_samples_leaf, min_samples_split, max_depth, 1)
    return root
```
