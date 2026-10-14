# 1. Aşama: Orijinal versiyon
print("original version:")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# 2. Aşama: Daha az print() ile (\n kullanarak)
print("\nwith fewer 'print()' invocations:")
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

# 3. Aşama: 2 kat büyük ok (higher)
print("\nhigher:")
print("""        *
       * *
      *   *
     *     *
    *       *
   *         *
  *           *
 *             *
******     ******
     *     *
     *     *
     *     *
     *     *
     *     *
     *     *
     *******""")

# 4. Aşama: Yan yana iki büyük ok (doubled)
print("\ndoubled:")
print("""        *                       *
       * *                     * *
      *   *                   *   *
     *     *                 *     *
    *       *               *       *
   *         *             *         *
  *           *           *           *
 *             *         *             *
******     ******   ******     ******
     *     *             *     *
     *     *             *     *
     *     *             *     *
     *     *             *     *
     *     *             *     *
     *     *             *     *
     *******             *******""")
