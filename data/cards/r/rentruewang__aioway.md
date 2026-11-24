# rentruewang/aioway

⭐ 1,821 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/rentruewang/aioway) · [官网](https://aioway.rentruewang.com/) · 个人维护

**面向开发者的深度学习算法优化编译器，构建白盒可解释模型**

Aioway 自述为深度学习算法的优化编译器：将机器学习模型/算法视为指令并据此构建 pipeline。机制上基于规则优化（相对神经架构搜索的搜索式优化），自动检测任务与可用资源以选择算法和模型，产出白盒（可解释）模型，支持部分模型升级与跨机器扩展，提供 SQL 风格关系代数与 Python 库两种接口，可用自定义 PyTorch 扩展。项目处于 v0.1.0 发布前的开发阶段，README 自述多数功能已完成但尚未打磨。构建于 koila 分支之上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将模型/算法视为指令的优化编译器架构
- 基于规则的优化路径与资源感知的算法/模型选择
- 白盒可解释模型，支持部分升级与跨机器扩展
- SQL 风格关系代数与 Python 库双接口

## 适用场景

- 希望以规则化方式自动选择算法与模型构建训练 pipeline
- 需要可解释、可部分升级的模型构建流程
- 基于 PyTorch 定制扩展算法构建能力

## 场景标签

 · 领域:深度学习/开发框架

## 证据(README 行号)

> L11: > Aioway is an optimizing compiler for deep learning algorithms.
> L25: - 🔥 Extensible with custom pytorch.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `817615772a85` · [字段定义](../../DATASET.md)*
