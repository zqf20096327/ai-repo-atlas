# Clawland-AI/Geneclaw

⭐ 46 · Python · MIT · 推送 2026-02-18 · [GitHub](https://github.com/Clawland-AI/Geneclaw) · [官网](https://geneclaw.ai) · 组织维护

**自进化 AI agent 框架：观察失败、提议并安全应用修复**

基于 HKUDS/nanobot 构建的自进化引擎，通过 Geneclaw Evolution Protocol (GEP) 让 agent 记录 JSONL 事件、诊断失败根因（启发式 + 可选 LLM 辅助）、生成带 unified diff 与风险等级的结构化修复提案，并在 5 层安全门（路径白/黑名单、diff 大小、密钥扫描、危险代码模式检测）与 Git 分支测试回滚机制下应用。默认全 dry-run，应用需显式 --apply 与配置开关。提供 autopilot 多轮进化、Streamlit 只读仪表盘与 123 项测试。面向需要在受控条件下实现 agent 自我改进的开发者。

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

- 失败观察→诊断→提案→安全应用的闭环自进化流程
- 5 层安全门（白/黑名单、diff 限制、密钥扫描、危险代码模式）
- Git 分支应用补丁 + pytest 验证 + 失败自动回滚
- 默认 dry-run，应用需显式 --apply 且 allowApplyDefault=true

## 适用场景

- 让 agent 在白名单路径内自动修复自身代码缺陷
- 审计与可视化 agent 的进化提案与事件时间线
- 在受控门控下运行多轮自动进化（autopilot）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14:  Built on nanobot — adds closed-loop self-improvement via the Geneclaw Evolution Protocol (GEP)
> L16: **Geneclaw** extends the ultra-lightweight nanobot AI agent with a **self-evolution engine** — enabling the agent t
> L29: |**Gatekeeper**|5-layer safety validation (allowlist, denylist, diff size, secret scan, code pattern detection)|

## 星数曲线

```mermaid
xychart-beta
    title "Clawland-AI/Geneclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f73eccab854d` · [字段定义](../../DATASET.md)*
