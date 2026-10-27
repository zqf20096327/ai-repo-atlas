# ansumandas441/mathematical-discovery-engine

⭐ 36 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/ansumandas441/mathematical-discovery-engine) · 个人维护

**把数学证明转为图上寻路的 LLM 定理发现引擎**

将数学知识编码为 15,941 节点、26,614 条边的有向知识图（含 4,135 公理、5,055 定理、1,223 证明技法），把证明问题重构为图上路径搜索：编排 LLM 解析问题并按启发式打分选择技法，多个 worker LLM 并行尝试单技法应用，剪枝器依据不可能性定理（Abel-Ruffini、Gödel、Turing）删除不可行分支。支持三种 worker 模式：免费 dry-run（mock worker）、Claude Code 订阅 CLI 子进程、Anthropic API 直调；图以 5 MB JSON 随仓库分发，无需数据库。提供检查点与断点续跑机制，并有浏览器端 3D 图可视化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15,941 节点 / 26,614 边 / 1,223 证明技法的数学知识图，随仓库以 JSON 分发
- 编排 LLM 选技法 + worker LLM 并行应用 + 基于不可能性定理的硬剪枝搜索循环
- 三种 worker 模式：免费 dry-run / Claude Code 订阅 CLI / Anthropic API
- 问题注册表 + 逐级 attempt ledger 的断点续跑与检查点机制

## 适用场景

- 对给定数学猜想运行自动化证明搜索并输出搜索树
- 浏览数学知识图，查看定理之间的技法推导关系（3D 交互可视化）
- 用 dry-run 模式零成本测试搜索逻辑与图结构

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L25: This repository **encodes the structure of mathematical knowledge as a graph and uses it to discover new theorems a
> L35: 3. **Proposes and implements a discovery engine.** Mathematical proof is reframed as **path-finding through this fi

## 星数曲线

```mermaid
xychart-beta
    title "ansumandas441/mathematical-discovery-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `89004b8c36b1` · [字段定义](../../DATASET.md)*
