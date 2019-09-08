import java.util.*;

int checkHeight(TreeNode root){
    if (root.left == null && root.right == null){
        return 1;
    }
    int leftHeight = checkHeight(root.left);
    int rightHeight = checkHeight(root.right);
    if (leftHeight == Integer.MIN_VALUE || rightHeight == Integer.MIN_VALUE)
        return Integer.MIN_VALUE;
    int heightDiff = Math.abs(rightHeight - leftHeight);
    if (neightDiff > 1){
        return Integer.MIN_VALUE;
    } else{
        return Math.max(leftHeight, rightHeight) + 1;
    }
}