# atharvakarval-dev/Form-Flow-AI

⭐ 22 · Python · 推送 2026-04-21 · [GitHub](https://github.com/atharvakarval-dev/Form-Flow-AI) · 个人维护

**语音对话驱动的 AI 表单自动填写与 PDF 填写代理**

基于 FastAPI + React + Playwright 的自动填表代理：通过语音对话（Web Speech API）下达指令，由 LLM（Gemini，可切换 Phi-2 本地模型）推断字段语义并自动填写网页表单与 PDF 表单。表单解析支持 Google Forms、Typeform 与通用 HTML，可递归穿透 Shadow DOM；自动化层实现拟人化输入延迟与多策略 CAPTCHA 处理（含 2Captcha API）；提供 RAG 用户画像上下文与建议引擎。支持 Docker 与全离线模式（Vosk 语音识别 + Phi-2）。当前仅 Web 端，Chrome 扩展在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 工厂模式路由 URL 到 GoogleForms/Typeform/StandardHTML 专用解析器，支持 Shadow DOM 穿透
- 多策略 CAPTCHA 处理：reCAPTCHA v2/v3、hCaptcha、Cloudflare Turnstile、2Captcha
- PDF 引擎提供视觉布局分析、动态字号适配与可提交的扁平化输出
- 离线模式：Vosk 语音识别 + Phi-2 本地 LLM（约 6GB 磁盘、4GB 内存/显存）

## 适用场景

- 通过语音对话让 AI 代为填写冗长的网页表单
- 自动填写并生成可提交的 PDF 表单文件
- API 成本敏感或隐私场景下用本地 Phi-2 模型离线运行

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: **Form Flow AI** is the world's most advanced **AI Form Filler** and **Automated Form Filling** agent, designed to 
> L44: - **Factory Pattern**: Dynamically routes URLs to specialized extractors (`GoogleForms`, `Typeform`, `StandardHTML`

## 星数曲线

```mermaid
xychart-beta
    title "atharvakarval-dev/Form-Flow-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2e73413dc505` · [字段定义](../../DATASET.md)*
