package com.github.dozaza;

//给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
//
// 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
//
// 你可以假设 nums1 和 nums2 不会同时为空。
//
// 示例 1:
//
// nums1 = [1, 3]
//nums2 = [2]
//
//则中位数是 2.0
//
//
// 示例 2:
//
// nums1 = [1, 2]
//nums2 = [3, 4]
//
//则中位数是 (2 + 3)/2 = 2.5
//
//

import java.util.HashMap;
import java.util.Map;

public class Question_0004 {

    public static void main(String[] args) {
        int[] nums1 = {2};
        int[] nums2 = {};

        double res = findMedianSortedArrays(nums1, nums2);
        System.out.println(res);
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;

        if (m == 0) {
            if (n % 2 == 1) {
                return nums2[n/2];
            } else {
                return (nums2[n/2 - 1] + nums2[n/2]) / 2.0;
            }
        } else if (n == 0) {
            if (m % 2 == 1) {
                return nums1[m/2];
            } else {
                return (nums1[m/2 - 1] + nums1[m/2]) / 2.0;
            }
        }

        int mid = (m + n) / 2;
        boolean isEven = (m + n) % 2 == 0;
        int[] midData = {0, 0};

        int i = 0;
        int j = 0;
        while (i < m && j < n) {
            boolean inNums1 = nums1[i] < nums2[j];

            int count = i + j;
            midData = updateMidData(nums1, nums2, mid, isEven, i, j, inNums1, count, midData);

            if (count == mid) {
                return (midData[0] + midData[1]) / 2.0;
            }

            if (inNums1) {
                i++;
            } else {
                j++;
            }
        }

        while (i < m) {
            int count = i + j;
            midData = updateMidData(nums1, nums2, mid, isEven, i, j, true, count, midData);
            if (count == mid) {
                return (midData[0] + midData[1]) / 2.0;
            }

            i++;
        }

        while (j < n) {
            int count = i + j;
            midData = updateMidData(nums1, nums2, mid, isEven, i, j, false, count, midData);
            if (count == mid) {
                return (midData[0] + midData[1]) / 2.0;
            }

            j++;
        }

        throw new RuntimeException("Error");
    }

    private static int[] updateMidData(int[] nums1, int[] nums2, int mid, boolean isEven,
                                       int i, int j, boolean inNums1, int count, int[] midData) {
        if (isEven) {
            if (count == (mid - 1)) {
                if (inNums1) {
                    midData[0] = nums1[i];
                } else {
                    midData[0] = nums2[j];
                }
            } else if (count == mid) {
                if (inNums1) {
                    midData[1] = nums1[i];
                } else {
                    midData[1] = nums2[j];
                }
            }
        } else {
            if (count == mid) {
                if (inNums1) {
                    midData[0] = nums1[i];
                } else {
                    midData[0] = nums2[j];
                }
                midData[1] = midData[0];
            }
        }

        return midData;
    }


}
