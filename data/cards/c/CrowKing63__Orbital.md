# CrowKing63/Orbital

⭐ 50 · C# · MIT · 推送 2026-11-02 · [GitHub](https://github.com/CrowKing63/Orbital) · [官网](https://crowking63.github.io/Orbital/) · 个人维护

**Windows 划词弹出的 AI 动作栏：翻译、总结、改写、自定义提示词**

一款轻量 Windows 托盘应用，全局监听鼠标与键盘，当用户在任意应用中选中文字时在光标上方弹出动作条，可执行翻译、摘要、改写、搜索或自定义提示词动作。支持五种触发方式（拖选、双击、键盘选择、长按、自定义快捷键），AI 结果支持替换原文、复制或弹窗展示。可接入 OpenAI、OpenRouter、Ollama、LM Studio 或任意 OpenAI 兼容端点，API key 经 Windows DPAPI 本地加密存储。提供安装包与便携版，另附源码构建步骤；二进制当前未签名，可能被杀软误报。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意应用中划词即弹出动作条，五种触发方式
- 接入 OpenAI 兼容端点，支持 Ollama/LM Studio 本地模型离线使用
- 自定义提示词模板（{text} 占位符）与自定义动作
- API key 经 Windows DPAPI 加密，本地存储

## 适用场景

- 阅读外文网页时划词即翻译或总结
- 写作时选中文本一键改写或润色
- 用本地模型在完全离线环境下处理选中文本
- 为常用操作配置一键提示词动作

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L39: - **Utility actions** - Copy, Cut, Paste, Delete, key simulation, and Google Search without any AI calls
> L45: - **Bring your own model** - works with OpenAI, OpenRouter (including free models), Ollama, LM Studio, or any OpenA
> L69: - Windows 10 or 11 (x64)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e1280cab3e3a` · [字段定义](../../DATASET.md)*
