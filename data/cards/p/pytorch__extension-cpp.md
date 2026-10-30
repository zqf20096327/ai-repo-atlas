# pytorch/extension-cpp

⭐ 1,203 · Python · 推送 2026-10-07 · [GitHub](https://github.com/pytorch/extension-cpp) · 组织维护

**PyTorch 官方 C++/CUDA 扩展编写示例仓库**

pytorch 组织维护的示例工程，含两个 C++/CUDA 扩展示例：extension_cpp 使用标准 ATen/LibTorch API，extension_cpp_stable 使用 LibTorch Stable ABI，使扩展无需为每个 PyTorch 版本重新编译即可在 >= 2.10.0 版本运行（需 PyTorch 2.10+）。两个示例均演示如何实现带自定义 CPU 与 CUDA 内核的 mymuladd 算子，通过 pip install --no-build-isolation -e . 源码构建并附测试脚本。面向需要编写 PyTorch 自定义算子扩展的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 mymuladd 自定义算子的标准 ATen 与 Stable ABI 两种实现
- Stable ABI 版本无需为每个 PyTorch 版本重新编译
- 含 CPU 与 CUDA 双内核示例
- 提供构建命令与测试脚本

## 适用场景

- 学习编写 PyTorch C++/CUDA 扩展
- 参考 Stable ABI 方式降低扩展的版本耦合维护成本
- 作为自定义算子工程的起始模板

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains two example C++/CUDA extensions for PyTorch:
> L18: Uses the LibTorch Stable ABI to ensure that the extension built can be run with any version

## 星数曲线

```mermaid
xychart-beta
    title "pytorch/extension-cpp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 1202 --> 1204
    line [1203, 1203]
```

2026-10-18 1,203 → 2026-10-30 1,203（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f4d71bf705fc` · [字段定义](../../DATASET.md)*
