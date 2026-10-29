# LSXPrime/ProseFlow

⭐ 76 · C# · AGPL-3.0 · 推送 2025-11-09 · [GitHub](https://github.com/LSXPrime/ProseFlow) · [官网](https://lsxprime.github.io/proseflow-web/) · 组织维护

**跨平台桌面 AI 文本处理器：任意应用中热键调用 LLM 处理文本**

面向终端用户的三平台（Windows/macOS/Linux）桌面应用，通过全局热键、悬浮球或拖放在任意应用中对选中文本执行校对、摘要、生成、转换等 AI 操作，支持模板化多步动作与占位符。混合引擎可连接 OpenAI/Groq/Anthropic/Google 及 OpenAI 兼容端点，也可用 GGUF 模型完全本地离线运行；提供官方微调小模型（1.5B/360M）与应用内下载。输出可替换原文、窗口审阅或 diff 对比。基于 .NET/Avalonia 构建，从官网或 GitHub Releases 下载安装包使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全局热键/悬浮球/拖放在任意应用中调用 AI 动作
- GGUF 模型 100% 本地离线运行，可自选 GPU 与线程数
- 接入 OpenAI/Groq/Anthropic/Google 及 OpenAI 兼容端点，多供应商自动回退
- 官方微调模型（1.5B/360M）与开源数据集 ProseFlow-Actions-v1（1,800+ 条）

## 适用场景

- 在编辑器、浏览器、办公软件中快速润色或改写选中文本
- 离线运行本地小模型处理文本，不上传数据
- 用模板化动作批量执行固定格式的文本生成任务
- 团队通过工作区同步共享动作与供应商配置

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L11: ProseFlow is a cross-platform desktop application that integrates powerful AI text processing into your daily workf
> L12: With a simple hotkey, you can access a menu of customizable AI actions to proofread, summarize, generate, or transf
> L89: * **Run 100% Locally & Offline:** Use **GGUF-compatible models** on your own hardware for maximum **privacy** and o
> L91: * **Connect to Cloud APIs:** Integrates with **OpenAI, Groq, Anthropic, Google**, and any **OpenAI-compatible endpo

## 星数曲线

```mermaid
xychart-beta
    title "LSXPrime/ProseFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-29 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1da8c76dbc09` · [字段定义](../../DATASET.md)*
