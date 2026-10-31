# microsoft/openclaw-dev

⭐ 25 · Shell · MIT · 推送 2026-07-02 · [GitHub](https://github.com/microsoft/openclaw-dev) · 组织维护

**在 Azure 云端托管 OpenClaw 常驻 AI 助手的部署模板**

微软维护的实验性模板：把 OpenClaw agent 部署到 Azure Container Apps，接入 Azure OpenAI（Foundry Models，默认 gpt-5.4-mini，Managed Identity 免 API key），通过 Microsoft Teams、WebChat UI 等渠道访问，可在手机上使用。不安全的工具执行可卸载到一次性隔离沙箱。提供 devclaw CLI（封装 azd）一条命令部署，并附带 AI agent skill 让 GitHub Copilot Chat、Claude Code、Cursor 等代为部署。自述为 Alpha 阶段，明确不保证生产就绪；运行成本约每天 2-5 美元。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一条命令部署到 Azure Container Apps，Teams/WebChat 多渠道访问
- Managed Identity 免 API key（disableLocalAuth: true）
- 工具执行可卸载到一次性隔离 ACA 沙箱
- 附带 Agent Skills 格式技能，可让 AI agent 代为部署运维

## 适用场景

- 部署自己的常驻云端 AI 助手并从手机 Teams 使用
- 在隔离沙箱中安全运行不受信任的 shell/代码/浏览器任务
- 用自然语言让 Copilot/Claude Code 等 agent 完成部署与排障

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: Your own **always-on AI assistant**, running safely in the cloud and reachable from **Microsoft Teams on your phone*
> L117: - The **openclaw brain** runs on **Azure Container Apps** and calls **Azure OpenAI in Foundry Models** (default `g

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/openclaw-dev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2686b70d1319` · [字段定义](../../DATASET.md)*
