# kprompt/kprompt

⭐ 43 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/kprompt/kprompt) · [官网](https://kprompt.ai) · 组织维护

**Kubernetes 的自然语言运维 CLI：把指令变成可审批的安全计划**

面向 Kubernetes 运维者的 CLI 工具，把自然语言提示转为带类型标注的计划（PlanResult：动作、diff、风险、影响范围），经用户 y/N 或 --approve 审批后才执行；毁灭类指令被硬性拒绝。支持 13 个 LLM 提供商（本地 Ollama 零成本或 BYOK 云端），内置 AI SRE 命令（investigate/why/timeline/impact）、可选的 propose-only 集群观察 Agent，以及 Helm、Prometheus、Grafana、Argo 等 Day-2 集成。自我声明为实验性软件，建议先在非生产集群使用。提供 curl 安装脚本、Homebrew 与 Go 源码构建三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言 → 类型化计划（动作、diff、风险、影响范围），审批后才执行
- 毁灭类（wipe-class）指令无论何种标志均硬性拒绝
- 13 个 LLM 提供商支持，含本地 Ollama（$0）与任意 OpenAI 兼容端点（BYOK）
- 可选 propose-only 集群观察 Agent 与 --output json 的 CI 集成

## 适用场景

- 用自然语言执行 Kubernetes 读写与变更操作，先审计划再应用
- 通过 investigate/why/timeline/impact 做根因分析
- 在 CI 中用 PlanResult JSON 做 jq 门禁与 GitOps PR
- 零成本用本地 Ollama 驱动，不上传集群凭证

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L17: kprompt turns natural language into **reviewable Kubernetes actions**. Every mutation becomes a typed **plan** — ac
> L39: - 🔌 **Your LLM, your keys** — 13 supported providers including local Ollama (`$0`), major clouds (BYOK), and any Op
> L77: |**AI Runtime**|A full loop: observe → reason → plan → validate → approve → execute → learn|

## 星数曲线

```mermaid
xychart-beta
    title "kprompt/kprompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5f47e009be74` · [字段定义](../../DATASET.md)*
