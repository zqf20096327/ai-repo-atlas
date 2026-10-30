# ciouskeila-hue/cybercode-cli

⭐ 45 · Python · NOASSERTION · 推送 2026-07-01 · [GitHub](https://github.com/ciouskeila-hue/cybercode-cli) · 个人维护 · 中文 README

**本地运行的浏览器 AI Agent，通过 32+ 模型执行文件、代码与多媒体任务**

在本地浏览器中运行的 AI Agent：通过统一网关接入 GPT-5.5、Claude Opus 4.8、GLM-5.2、Gemini 3.1 Pro、DeepSeek V4 等 32+ 模型，核心约 1,300 行 Python（仅依赖 requests 与 Python 标准库），提供 9 个原子工具执行代码、读写/修补文件、网页抓取、JS 执行、图像生成与视觉理解，支持 OpenAI 兼容 function calling 与流式输出。内置 HyperFrames 技能集（HTML+GSAP/Lottie/Three.js 经 ffmpeg 合成 MP4）与三级记忆。可通过 CyberCode 账号零配置使用平台模型，或跳过登录自行配置 API key。Agent 核心架构源自 lsdefine 的 GenericAgent 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个原子工具：代码执行、文件读写/修补、网页抓取、JS 执行、图像生成、视觉理解、用户交互
- 统一网关代理 32+ 前沿模型，默认 zero-cost 的 free/glm-5.2
- HyperFrames 视频引擎：HTML 组合 + GSAP/Lottie/Three.js 动画 + edge-tts 配音，ffmpeg 合成 MP4
- 核心仅依赖 Python stdlib + requests，提供 HTTP API 与 SSE 流式响应

## 适用场景

- 让 Agent 代替我写脚本、跑数据分析并读写项目文件
- 生成配图并做视觉理解（如读截图找问题）
- 抓取网页内容并提取正文信息
- 一句话生成带中文配音的短视频

## 场景标签

`编码 Agent` `数据分析` `网页抓取` `图像生成` · 领域:效率与自动化

## 证据(README 行号)

> L18: CyberCode is an AI Agent that runs in your local browser. It's not a chatbot shell — it's a **doer with hands and f
> L20: The key point: **use GPT-5.5, Claude Opus 4.8, GLM-5.2, Gemini 3.1 Pro, DeepSeek V4 and 32+ frontier models for fre
> L32: |**9 Atomic Tools**|Code execution / File read-write / Web scraping / JS execution / Image gen / Vision / User inte

## 星数曲线

```mermaid
xychart-beta
    title "ciouskeila-hue/cybercode-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5bfafd23b6a4` · [字段定义](../../DATASET.md)*
