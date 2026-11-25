# V1ki/dsh-plugin-subscriptions

⭐ 633 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/V1ki/dsh-plugin-subscriptions) · 个人维护

**把 ChatGPT/Claude/Grok 订阅接入 DeepSeek Harness 的插件**

面向 DeepSeek Harness（DSH）的插件，将用户已有的 ChatGPT (Codex)、Claude、Grok (X Premium)、GitHub Copilot、Google Antigravity 订阅转换为 DSH 的 LLM provider，无需 API key：多数通过 Web UI 的 OAuth 登录，Claude 可从现有 Claude Code 会话导入凭据，令牌存储在本地（0600 权限）并自动刷新。提供订阅/模型显示名管理、推理力度与速度选择、配额百分比展示、图像/视频生成工具调用，以及本地保存的用量仪表盘（26 周热力图、配额周期图表）；不存储提示词、凭据或逐请求日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OAuth 登录接入 ChatGPT/Claude/Grok/Copilot/Antigravity 订阅，无需 API key
- 本地令牌存储（~/.dsh/ 下，mode 0600）并自动刷新
- 订阅用量仪表盘：KPI 卡片、26 周热力图、配额周期双轴图
- image_generate/video_generate 工具支持按 provider 选择后端并内联展示

## 适用场景

- 在 DSH 会话模型选择器中使用已有订阅的模型目录
- 查看各订阅账号的配额窗口与用量趋势
- 在对话中按 provider 生成图像/视频并内联预览

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Use your **ChatGPT (Codex)**, **Claude**, **Grok (X Premium)**, **GitHub Copilot**, and **Google Antigravity** subsc
> L35: Logged-in providers join the session model picker with their live model catalogs:
> L86: ## Providers

## 星数曲线

```mermaid
xychart-beta
    title "V1ki/dsh-plugin-subscriptions 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 479 --> 647
    line [493, 499, 504, 507, 509, 518, 527, 531, 537, 539, 545, 504, 574, 584, 594, 599, 603, 605, 608, 618, 620, 622, 628, 629, 630, 632, 633]
```

2026-10-23 493 → 2026-11-25 633（+140）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `00b39af518f9` · [字段定义](../../DATASET.md)*
