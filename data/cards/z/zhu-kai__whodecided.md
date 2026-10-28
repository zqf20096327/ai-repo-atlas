# zhu-kai/whodecided

⭐ 22 · TypeScript · MIT · 推送 2026-07-16 · [GitHub](https://github.com/zhu-kai/whodecided) · 个人维护 · 中文 README

**审计 AI 编程代理未询问决策并形成可复核台账的 CLI**

面向使用 Claude Code / Codex 的开发者的命令行工具：用一次 LLM 调用（通过用户已认证的 claude/codex CLI）把代理会话记录提炼成一屏决策台账，附理由与转写证据；确定性信号按风险排序供 Approve/Reject 复核，裁决写入 .wdd/ 下的仅追加账本，批准的规则落到 CLAUDE.md/AGENTS.md，wdd gate 可在 pre-push/CI 阻断未复核决策。无服务器、无数据库、无 API key，单依赖 yaml，证据做密钥脱敏后本地持久化。

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

- LLM 提炼会话为决策台账，附 why 与转写证据（脱敏持久化）
- 风险评分排序（silent × hard-to-undo × churn）与削弱测试检测
- 裁决写入仅追加 jsonl 账本，批准规则同步到 CLAUDE.md/AGENTS.md
- wdd gate 提供合并门禁退出码，支持 pre-push/CI

## 适用场景

- 复核 AI 编程代理在会话中未询问做出的隐式决策
- 把人工裁决变成代理下次遵循的先例规则
- 在 CI/pre-push 阻断未复核的隐式决策进入主干

## 场景标签

 · 领域:开发者工具/AI 代理治理

## 证据(README 行号)

> L23: 1. **Distill** - one LLM pass (your own `claude` / `codex` CLI) turns session transcripts into a one-screen ledger 
> L25: 3. **Rule** - Approve or Reject each (`j/k` + `a/r`); rulings write straight to an append-only ledger in `.wdd/`.
> L26: 4. **Ratchet** - approved rules land in `CLAUDE.md` / `AGENTS.md`, `wdd gate` blocks unreviewed silent decisions fr

## 星数曲线

```mermaid
xychart-beta
    title "zhu-kai/whodecided 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f1ca22386dfc` · [字段定义](../../DATASET.md)*
