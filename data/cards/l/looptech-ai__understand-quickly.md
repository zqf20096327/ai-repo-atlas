# looptech-ai/understand-quickly

⭐ 48 · JavaScript · Apache-2.0 · 推送 2026-09-17 · [GitHub](https://github.com/looptech-ai/understand-quickly) · [官网](https://looptech-ai.github.io/understand-quickly/) · 组织维护

**代码知识图谱公共注册表：AI agent 一次请求获取仓库结构**

面向 AI agent 与开发者的公开机器可读注册表：收录各开源仓库提交的代码知识图谱（描述文件、函数、模块及其连接的 JSON），注册表本身只存指针，图谱存于源仓库；每个 PR 运行 schema 校验，夜间同步并按 last_sha 缓存，状态含 pending/ok/invalid/dead 等十级。项目维护者可通过向导、CLI 或手动 PR 收录仓库；消费方可经 registry.json、.well-known 发现、MCP 服务器（list_repos/get_graph/search_concepts）或 Python SDK 获取。支持 understand-anything、GitNexus、code-review-graph、bundle 等格式，Apache 2.0 代码配独立数据许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图谱存于源仓库、注册表只存指针，一次 URL 拉取免认证免 SDK
- PR 时对 registry.json 与图谱体做 schema 校验，夜间同步 + repository_dispatch 即时刷新
- 支持 understand-anything/gitnexus/code-review-graph/bundle 等 5 类格式
- 分发渠道含 npm CLI、MCP 服务器、PyPI SDK、GitHub Action 与 Pages 浏览器

## 适用场景

- 让 Claude/Codex/Cursor 等 agent 通过 MCP 即时理解已收录的代码仓库
- 项目维护者把自家仓库的代码知识图谱收录进公共目录
- 构建代码检索/审查工具时按 URL 批量拉取经验证的仓库结构图

## 场景标签

`知识图谱` `精选清单` · 领域:知识与检索

## 证据(README 行号)

> L3: **A public, machine-readable registry of code-knowledge graphs.**
> L32: **It's a public directory of "map files" for codebases.** Each entry points at a JSON file (a *knowledge graph* or 
> L105: - **Storage:** graphs live in source repos. The registry stores only pointers.

## 星数曲线

```mermaid
xychart-beta
    title "looptech-ai/understand-quickly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-28 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f41d5d034c45` · [字段定义](../../DATASET.md)*
