# bubblelabai/BubbleLab

⭐ 1,097 · TypeScript · Apache-2.0 · 推送 2026-04-30 · [GitHub](https://github.com/bubblelabai/BubbleLab) · [官网](https://bubblelab.ai/) · 组织维护

**开源工作流引擎：供团队在 Slack 内用 AI 助手自动化运维工作**

Bubble Lab 平台的开源核心工作流引擎，可独立运行、托管和扩展。提供工作流执行运行时、agent 与集成原语（Bubbles）、本地工作流 studio、执行追踪与日志、CLI 工具和可导出工作流。面向使用 Bubble Lab 平台的团队、需要自托管自动化基础设施的组织及构建自定义 agent 的开发者。AI 助手 Pearl 的流程生成默认使用 gemini-3.0-pro，需 GOOGLE_API_KEY，较弱模型未充分测试。TypeScript 编写，Apache 2.0 许可。截至 2026 年 1 月不再接受代码贡献与 PR，但继续接受 bug 报告与功能请求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作流执行运行时与 Bubbles（工具/节点）组合机制
- 本地 Bubble Studio 可运行、编辑和执行工作流
- npx create-bubblelab-app CLI 脚手架含示例模板（reddit-scraper 等）
- 内置执行追踪、日志与性能统计

## 适用场景

- 自托管团队自动化工作流基础设施
- 在本地构建、编辑和运行 agent 工作流
- 将工作流嵌入自己的产品中部署
- 通过 CLI 快速创建含模板的可定制 agent 项目

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L30: This repository contains the **open-core workflow engine that powers the Bubble Lab platform**.
> L76: - Workflow execution runtime
> L107: **⚠️ Note:** To create flow with pearl (our ai assistant), you'll need API keys (GOOGLE_API_KEY). By default gemin

## 星数曲线

```mermaid
xychart-beta
    title "bubblelabai/BubbleLab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 1096 --> 1099
    line [1098, 1097]
```

2026-10-18 1,098 → 2026-10-22 1,097（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5fcea7512826` · [字段定义](../../DATASET.md)*
