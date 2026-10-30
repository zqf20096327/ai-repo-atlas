# granth-agarwal/codectx

⭐ 28 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/granth-agarwal/codectx) · [官网](https://codectx.granth.tech) · 个人维护

**为 AI agent 编译代码库上下文的 CLI：图排序+分层压缩输出**

Python 编写的 CLI 工具，将仓库编译为单个 CONTEXT.md 供 LLM 推理使用。机制：构建依赖图，按 fan-in 中心性、git 提交频率与入口点距离打分，前 15% 文件生成 AST 结构化摘要、随后 30% 保留签名、其余单行描述，并在 token 预算内优先纳入高分文件。支持 9 种语言（tree-sitter 自动检测）、缓存增量运行与 Docker 运行；要求 Python 3.10+。基准显示 5 个 Python 仓库平均 token 缩减 76%。

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

- 依赖图 + fan-in/git 频率/入口点距离的文件评分
- 三层压缩：结构化摘要/签名/单行描述，约 10% token 成本
- 9 种语言支持，tree-sitter 自动检测
- 仓库级缓存与 no-op 跳过，支持语义嵌入缓存

## 适用场景

- 把大代码库压缩成单个 markdown 文档喂给 AI agent
- 在 128k 上下文窗口内让 agent 理解整个仓库结构
- 按 debug/feature/refactor 等任务画像生成定向上下文

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: A CLI tool that compiles repository context for AI agents — ranking files by importance, compressing them into struc
> L19: 1. Scans the repository and builds a dependency graph

## 星数曲线

```mermaid
xychart-beta
    title "granth-agarwal/codectx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bfbe43bd2dec` · [字段定义](../../DATASET.md)*
