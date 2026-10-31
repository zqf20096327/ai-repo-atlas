# PyModel/jev-judge-mcp

⭐ 49 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/PyModel/jev-judge-mcp) · 组织维护

**给编码 agent 提供 15 个类型化判断工具的 MCP 服务器**

MCP 服务器，向 Claude Code、Codex、Cursor、OpenCode、Pi 等编码 agent 暴露 15 个基于 TypeSafe Jev 模型的判断工具（verify/screen/find/classify/rerank/decide/compare/extract/review/gate/score 等）。Agent 传入证据与可枚举问题，Jev 返回概率（记录的中位往返 464.6 ms），策略层将概率转为 auto/review/escalate 三种动作。适用于答案集合固定的检查；需生成新文本/代码的场景不适用。需 Python 3.12+、uv、POSIX 系统与 TypeSafe API key，经 uvx 从 PyPI 安装，也提供 git clone 开发路径与非 MCP 的 CLI 入口。

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

- 15 个判断工具：verify、screen、classify、rerank、decide、gate 等
- 模型输出概率，策略层转为 auto/review/escalate 三种动作
- 安装器自动配置 8 种 agent（Claude Code、Codex、Cursor、OpenCode、Pi 等）
- 提供非 MCP 客户端可用的 jev-judge-mcp judge / gate CLI 路径

## 适用场景

- 让 agent 核对 PR 描述或总结中的声明是否有出处
- 读取网页前筛查提示注入风险
- 对补丁做'是否完成'的门禁判定后再交付
- 批量路由工单或对搜索结果重排序

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: An MCP server that gives your coding agent fifteen judgment tools backed by TypeSafe's Jev model. The agent hands a
> L138: |Check that the agent's "done" matches the diff and the test log|`jev_gate`|one ship decision over the patch and e

## 星数曲线

```mermaid
xychart-beta
    title "PyModel/jev-judge-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-31 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e747e297059d` · [字段定义](../../DATASET.md)*
