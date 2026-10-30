# tanaikech/A2UI-for-Google-Apps-Script

⭐ 15 · MIT · 推送 2026-02-07 · [GitHub](https://github.com/tanaikech/A2UI-for-Google-Apps-Script) · [官网](https://medium.com/google-cloud/a2ui-for-google-apps-script-bcd0f37a3774) · 个人维护

**在 Google Apps Script 中实现 Google A2UI 协议的示例项目集**

将 Google 的 A2UI（Agent-to-User Interface）协议移植到 Google Apps Script 生态的示例集合：借助 Gemini API 在 Google Sheets 对话框、侧边栏与 Web App 中生成 AI 驱动的动态界面。提供 5 个可复制的示例电子表格项目，涵盖餐厅预订、预算模拟、日历同步、递归 UI 循环（按对话历史生成文件查看器/编辑器）与以 Sheets 为持久记忆的自适应测验。安装方式为复制示例表格并在 Apps Script 中填入 Gemini API Key，无外部服务器。限制：依赖 Google Workspace 与 Gemini API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个可直接复制到 Drive 的示例项目（Web App/对话框/侧边栏）
- 递归 UI 循环：Gemini 依据对话历史与 System Event 生成下一步界面
- 以 Google Sheets 作为持久记忆存储的自适应学习架构
- LLM 路由：由 Gemini 选择工具并生成 A2UI JSON 载荷

## 适用场景

- 在 Google Sheets 内构建 AI 生成的预订表单、编辑器等交互界面
- 让 agent 读写 Sheets/Calendar/Drive 完成多步任务
- 搭建按用户历史表现调整难度的自适应测验

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L9: This repository demonstrates how to implement Google's A2UI (Agent-to-User Interface) protocol entirely within the G
> L11: By porting the official concepts to GAS, this project enables developers to create dynamic, AI-generated interactiv
> L15: A2UI is a "secure-by-design" protocol that allows AI agents to generate rich user interfaces using a strict schema 

## 星数曲线

```mermaid
xychart-beta
    title "tanaikech/A2UI-for-Google-Apps-Script 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `90665a7af575` · [字段定义](../../DATASET.md)*
