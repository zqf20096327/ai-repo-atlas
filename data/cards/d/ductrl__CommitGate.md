# ductrl/CommitGate

⭐ 15 · Python · MIT · 推送 2026-07-19 · [GitHub](https://github.com/ductrl/CommitGate) · 个人维护

**AI 加持的 Git pre-commit/pre-push 安全门禁，拦截泄密提交**

以 Git 钩子形式运行的本地安全工具：在 commit 或 push 时将变更交给 Gitleaks 与可选的 AI Reviewer 双通道扫描，合并结果后给出 allow/warn/block 判定，block 时中止提交或推送，也可用 commitgate scan 手动扫描。AI 部分支持 OpenAI 兼容 API（OpenAI/Gemini/DeepSeek/Kimi/Groq）或本地登录的 CLI agent（Claude Code/Codex/Antigravity），也可关闭 AI 仅用 Gitleaks。需注意启用 AI 时 diff 会被发送到所配置的提供商，非隔离方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gitleaks 正则扫描 + AI Reviewer 代码理解的双通道合并判定
- allow/warn/block 三态结果与可配置 block_severity 阈值
- 支持 OpenAI 兼容 API 与 CLI agent 两种 AI 接入，或关闭 AI 仅用 Gitleaks
- commitgate init 一键生成配置并安装 pre-commit/pre-push 钩子

## 适用场景

- 在提交前拦截误写入的密钥与高风险代码
- 团队共享 commitgate.yaml 统一门禁策略
- 不连外网时关闭 AI 仅用 Gitleaks 做本地扫描

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: CommitGate scans your changes and **blocks them** before secrets or risky code ever reach your history.
> L127: **Option C: No AI** (Gitleaks only)
> L131:   enabled: false

## 星数曲线

```mermaid
xychart-beta
    title "ductrl/CommitGate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b1664b8bc785` · [字段定义](../../DATASET.md)*
