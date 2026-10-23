# siboehm/lleaves

⭐ 484 · Python · MIT · 推送 2026-01-01 · [GitHub](https://github.com/siboehm/lleaves) · [官网](https://lleaves.readthedocs.io/en/latest/) · 个人维护

**将训练好的 LightGBM 模型编译为机器码以加速预测**

基于 LLVM 的 LightGBM 决策树编译器：读取训练好的 LightGBM 模型文件，编译为优化机器码，宣称预测加速 ≥10x；接口为 LightGBM.Booster 的子集，可作为 drop-in 替换。支持低延迟单行预测与高吞吐批量预测；编译结果可缓存为 ELF/Mach-O 二进制文件避免重复编译，也可链接生成二进制以消除 Python 开销。依赖仅 llvmlite 与 numpy（LLVM 静态链接）。仅支持 Linux 和 macOS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LightGBM 模型转优化机器码，宣称预测加速 ≥10x
- 接口为 LightGBM.Booster 的子集，drop-in 替换
- 编译结果可缓存为 ELF/Mach-O 文件，支持 C 链接调用
- 依赖仅 llvmlite 与 numpy，LLVM 静态链接

## 适用场景

- 上线模型需要更快的 LightGBM 批量预测
- 低延迟单行预测场景中减少推理耗时
- 研究复现中引用并加速 NYC-taxi 等数据集推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: A LLVM-based compiler for LightGBM decision trees.
> L8: `lleaves` converts trained LightGBM models to optimized machine code, speeding-up prediction by ≥10x.

## 星数曲线

```mermaid
xychart-beta
    title "siboehm/lleaves 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 482 --> 485
    line [483, 484, 484]
```

2026-10-18 483 → 2026-10-23 484（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e834d6265c7a` · [字段定义](../../DATASET.md)*
