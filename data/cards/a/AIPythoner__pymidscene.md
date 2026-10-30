# AIPythoner/pymidscene

⭐ 19 · Python · MIT · 推送 2026-06-16 · [GitHub](https://github.com/AIPythoner/pymidscene) · 个人维护 · 中文 README

**AI 驱动的自然语言 UI 自动化 Python SDK，用中文描述即可操作浏览器与手机**

Midscene.js 的 Python 实现：以自然语言描述代替 CSS 选择器/XPath 驱动浏览器，核心 API 包括 ai_click/ai_input/ai_locate/ai_query/ai_assert 等，ai_action 走 plan-execute-replan 规划循环。支持 Doubao、Qwen、GPT-4V、Claude 等视觉 LLM，集成 Playwright，可经 ADB 控制 Android 真机、经 WebDriverAgent 驱动 iPhone。XPath 缓存与 Midscene.js 格式互通，缓存文件跨 JS/Python 版本互换；另提供跑 YAML 脚本的 pymidscene CLI，无需写 Python。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言代替选择器操作浏览器（ai_click/ai_input/ai_query 等 10 个核心 API）
- 支持 Doubao、Qwen、GPT-4V、Claude 等视觉 LLM
- Playwright 集成 + Android(ADB)/iOS(WebDriverAgent) 设备控制
- XPath 缓存与 Midscene.js 格式兼容，CLI 可直接运行 YAML 自动化脚本

## 适用场景

- 用自然语言编写网页自动化与 UI 测试脚本，摆脱脆弱选择器
- 从页面提取结构化数据（ai_query）
- 在 Android 真机与 iPhone 上做自然语言驱动的自动化
- 通过 YAML 脚本和 CLI 批量执行自动化任务

## 场景标签

`浏览器自动化` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: PyMidscene is a Python port of Midscene.js - an AI-powered UI automation framework. It allows you to control web br
> L33: - **Multi-Model Support** - Works with Doubao, Qwen, GPT-4V, Claude, and other vision LLMs

## 星数曲线

```mermaid
xychart-beta
    title "AIPythoner/pymidscene 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2aec168769f7` · [字段定义](../../DATASET.md)*
