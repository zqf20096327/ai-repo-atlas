# Vineetpandey0/Context-Sync

⭐ 25 · JavaScript · MIT · 推送 2026-04-05 · [GitHub](https://github.com/Vineetpandey0/Context-Sync) · 个人维护

**Chrome 扩展：跨 Claude/ChatGPT/Gemini/DeepSeek 保存并迁移 AI 对话上下文**

面向 AI 工具重度用户的浏览器扩展：通过 DOM 观察器在 Claude、ChatGPT、Gemini、DeepSeek 页面后台自动抓取对话，存于本地 chrome.storage（上限 50 条），在统一弹窗中跨平台检索、复制或下载为 JSON capsule；并向各平台工具栏注入 Export 按钮，实现一键把上下文注入另一 AI 并自动提交。可选接入 Gemini 2.5 Flash 做压缩（代码块不压缩），不填 API key 则全部本地运行。未上架 Chrome Web Store，需开发者模式加载源码安装。

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

- MutationObserver 后台自动抓取四个 AI 平台的对话并本地存储
- 向各平台工具栏注入 Export 按钮，一键跨平台注入上下文并自动提交（4×3 发送矩阵）
- 可选 Gemini 2.5 Flash 压缩管线：代码块永不压缩，短消息跳过
- 无云端、无注册，不填 API key 时数据全部留在本地

## 适用场景

- 达到用量限制或平台故障时，把长对话完整迁移到另一个 AI 继续
- 统一查看和检索散落在多个 AI 平台的历史对话
- 把对话导出为 JSON 或纯文本备份留存

## 场景标签

 · 领域:AI 工作流/浏览器工具

## 证据(README 行号)

> L65: 1. **Silently watches** your conversations on Claude, ChatGPT, Gemini, and DeepSeek using DOM observers
> L97: |Send context to another AI (opens tab + auto-injects + auto-submits)|✅ Live|
> L269: 4. **Click a target AI** — a new tab opens, the context is typed into the input, and the Send button is automatica

## 星数曲线

```mermaid
xychart-beta
    title "Vineetpandey0/Context-Sync 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `406dc79ed9b3` · [字段定义](../../DATASET.md)*
