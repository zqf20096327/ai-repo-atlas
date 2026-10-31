# iterative/features

⭐ 14 · Shell · Apache-2.0 · 推送 2026-06-27 · [GitHub](https://github.com/iterative/features) · [官网](https://containers.dev/implementors/features/) · 组织维护

**面向机器学习/数据科学的开发容器 features 集合**

由 Iterative 维护的一组开发容器（devcontainer）features：在 devcontainer.json 中引用 ghcr.io 发布的 feature 即可为容器环境安装 DVC、nvtop（GPU 监控）等工具，每个 feature 附带自身的 README 说明引用方式与可用选项。面向使用 VS Code 开发容器或 GitHub Codespaces 的机器学习与数据科学开发者，用途是快速搭建可复现的开发环境。属于容器配置资产集合，非模型或应用本体。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 devcontainer feature 形式发布，ghcr.io 引用即装
- 提供 DVC 等 ML/数据科学工具的容器化安装
- 每个 feature 附 README 说明引用方式与选项

## 适用场景

- 在开发容器或 Codespaces 中快速加入 DVC
- 为 GPU 开发环境安装 nvtop 监控工具
- 标准化团队的 ML 开发容器配置

## 场景标签

 · 领域:开发工具/容器化

## 证据(README 行号)

> L3: A set of simple and reusable
> L6: E.g. to quickly add DVC to a development container,

## 星数曲线

```mermaid
xychart-beta
    title "iterative/features 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f338263b8dd7` · [字段定义](../../DATASET.md)*
