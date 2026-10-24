# stillwater-sc/universal

⭐ 504 · C++ · MIT · 推送 2026-10-23 · [GitHub](https://github.com/stillwater-sc/universal) · 组织维护

**C++ 头文件数值类型库：为混合精度算法开发提供自定义算术类型**

Header-only C++ 模板库，提供可替换原生整数/浮点类型的算术插拔类型集合：包括 quarter/half/quad 浮点、bfloat16、TensorFloat、定点、posits、对数数系、区间与自适应精度数等，用于 AI、DSP、HPC 等领域的混合精度算法开发与优化。纯模板库无其他依赖，通过 CMake 构建，提供 Docker 容器、命令行检查工具、教育示例与各数系回归测试套件。有 JOSS 论文与 Zenodo DOI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 IEEE-754 替代与扩展类型：quarter/half/quad、bfloat16、posits、定点、对数数系等
- header-only 纯模板库，无其他依赖
- 提供 Docker 预装容器与命令行数值检查工具（ieee/quarter/half 等）
- 每个数系自带完整回归测试套件并接入 CI

## 适用场景

- 在 AI/DSP 算法中替换原生浮点以调整精度与动态范围
- 实验 bfloat16、posits 等替代数系的数值行为
- 检查开发环境中 IEEE 浮点的表示与截断方式

## 场景标签

 · 领域:数值计算/科学计算库

## 证据(README 行号)

> L17: The goal of the Universal Numbers Library is to offer alternatives to native integer and floating-point for mixed-p
> L21: The Universal Library is a ready-to-use header-only library that provides a plug-in replacement for native types an

## 星数曲线

```mermaid
xychart-beta
    title "stillwater-sc/universal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 503 --> 505
    line [504, 504]
```

2026-10-18 504 → 2026-10-24 504（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b4c1040c9146` · [字段定义](../../DATASET.md)*
