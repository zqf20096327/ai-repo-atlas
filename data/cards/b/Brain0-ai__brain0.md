# Brain0-ai/brain0

⭐ 317 · Rust · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/Brain0-ai/brain0) · 组织维护

**AI 编码的黑盒审计工具：把每个 commit 关联到背后的 agent 意图**

面向使用 Codex / Claude Code 等编码代理的开发者：被动读取 git 历史与 agent 落盘的会话转录，构建 commit→prompt→函数级符号的决策图谱，提供 drift（声明 vs 实改）检测、DLP 敏感读取审计、证据驱动的风险评分、GUI 图谱浏览与 MCP 查询通道（context/blame/debug/audit），以及 Ed25519/in-toto 签名溯源与审计报告。无需 hooks、不改动仓库；离线优先，默认本地确定性摘要与 feature-hash 嵌入，Ollama 可选增强。以 npx 一条命令运行，硬性依赖仅 Node.js ≥ 20。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 被动读取 git 与 agent 转录构建 commit 到 prompt 的决策图谱，零集成
- drift 检测（agent 声明 vs 实际 diff）与 DLP 敏感读取审计（记录路径与密钥种类，不存值）
- 先验+后验证据融合的风险评分与可下钻 GUI 图谱
- MCP 查询通道与 Ed25519/in-toto 签名溯源、加密存储、防篡改审计日志

## 适用场景

- 排查某个 bug 由哪条 prompt 引入、根因定位
- 审计 agent 会话是否读取了 .env 等敏感文件（DLP、pre-commit 阻断）
- 每日 triage：按风险排序查看过去 24h 各 agent 的改动
- 让编码代理在改代码前通过 MCP 查询文件的风险与意图历史

## 场景标签

`代码审查` `LLM 可观测性` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L22: brain0 **passively** builds a decision graph of your repository: every **commit** linked to
> L25: green → red. No hooks, no agent cooperation, no code changes: it reads git and the
> L125: The same graph is a query channel your coding agent can call **before touching code**:

## 星数曲线

```mermaid
xychart-beta
    title "Brain0-ai/brain0 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 322 --> 325
    line [323, 324, 324]
```

2026-10-18 323 → 2026-10-22 324（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3d9f62fc5a0a` · [字段定义](../../DATASET.md)*
