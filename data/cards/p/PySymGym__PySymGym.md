# PySymGym/PySymGym

⭐ 16 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/PySymGym/PySymGym) · [官网](https://pysymgym.github.io/PySymGym/) · 组织维护

**训练符号执行引擎路径选择器的 Python 基础设施**

面向符号执行引擎的机器学习训练基础设施：构建 SVM 与映射数据、运行训练流程并进行 Python 测试与 lint。项目使用 git 子模块组织源码，通过 poetry（指定版本 2.2.1）安装环境；GPU 使用需按宿主设备手动安装对应版本的 torch 与 torch_geometric。文档覆盖架构、用法、集成、数据集与 API 参考。主题标签涉及图神经网络与符号执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 构建 SVM 与映射数据并运行训练
- 源码以 git 子模块形式组织，poetry 管理依赖
- GPU 路径需手动安装匹配宿主设备的 torch/torch_geometric
- 文档包含架构、集成、数据集与开发者指南

## 适用场景

- 为符号执行引擎训练路径选择模型
- 复用其数据集与训练流程做路径选择研究
- 集成到已有符号执行工具中作为选择组件

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: Build SVM-s and maps, and run training
> L7: Python infrastructure to train path selectors for symbolic execution engines.

## 星数曲线

```mermaid
xychart-beta
    title "PySymGym/PySymGym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `93b6100ae32e` · [字段定义](../../DATASET.md)*
