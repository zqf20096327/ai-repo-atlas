# oscaar90/OpsGuard-AI

⭐ 17 · Python · AGPL-3.0 · 推送 2026-09-22 · [GitHub](https://github.com/oscaar90/OpsGuard-AI) · 个人维护

**面向 GitHub PR 的 AI 安全门禁：本地规则+LLM 语义审查**

作为 GitHub Action 安装的两阶段安全门禁：Gate 1 在本地用确定性规则毫秒级检测硬编码密钥（AWS/GitHub/Stripe 密钥、私钥等）；Gate 2 将 diff 发送至 LLM 做语义审查，识别 SQL 注入、开发者后门、认证绕过、供应链抢注与 AI 生成的不安全逻辑。LLM 调用通过 OpenRouter API 进行，AI 出错时返回 BLOCK（fail-closed），大 diff 会被截断以控制成本与延迟。面向使用 GitHub Actions 作 CI 门禁、无专职 AppSec 人员的团队。本地运行可 git clone 后用 poetry 安装并 CLI 扫描。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gate 1 本地确定性检测 + Gate 2 LLM 语义审查的两阶段架构
- LLM 失败时 fail-closed 返回 BLOCK 而非 APPROVE
- 规则集中配置于 opsguard.yml，可自定义已知坏模式
- 提供本地 CLI（poetry run opsguard scan）与 fixture 测试样例

## 适用场景

- 在 GitHub Actions 上合并前拦截含漏洞或后门的 PR
- 审查 Copilot/Cursor 等 AI 生成代码引入的不安全逻辑
- 检测硬编码密钥与供应链抢注并阻断流水线

## 场景标签

`代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L23: - **Gate 2** sends the diff to an LLM for contextual review of logic flaws and subtle vulnerabilities.
> L46: OpsGuard lets Gate 1 pass, sends the diff to Gate 2, and blocks the PR with a semantic finding:
> L85: Git Diff -> Gate 1: Local Regex -> Gate 2: LLM Review -> APPROVE / BLOCK

## 星数曲线

```mermaid
xychart-beta
    title "oscaar90/OpsGuard-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e4bac8db826b` · [字段定义](../../DATASET.md)*
