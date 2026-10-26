# diandiancha/LittleAIBox

⭐ 113 · JavaScript · MIT · 推送 2026-04-24 · [GitHub](https://github.com/diandiancha/LittleAIBox) · [官网](https://littleaibox.com) · 个人维护 · 中文 README

**跨平台 Gemini AI 聊天应用：本地处理文件、隐私优先**

基于 Vite/Capacitor/Cloudflare 的全栈跨平台 AI 对话应用，接入 Google Gemini API。浏览器端直接解析 PDF/DOCX/XLSX/PPTX 文件（无需上传），支持实时网页搜索、Semantic Scholar 研究模式、图像生成、语音输入与多格式导出；后端含弹性 API 密钥池（多密钥轮换、健康检查、自动故障转移）以绕过地区限制。面向受限地区用户、学生、开发者与注重隐私的用户；无需注册即可使用，提供 PWA 离线与 Android 原生支持。限制：本仓库仅开源前端，订阅/支付后端闭源；声明用于教育与研究目的，商业部署由作者另行运营。

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

- 客户端直接解析 PPTX/DOCX/PDF/XLSX 文件，处理不上传
- 弹性 Gemini API 密钥池：多密钥轮换、健康检查、自动故障转移
- 研究模式对接 Semantic Scholar 并输出结构化带引文回答
- PWA 离线可用 + Android 原生（Capacitor），免注册使用

## 适用场景

- 在浏览器里让 AI 分析论文、PPT 与文档且不上传文件
- 受限地区用户通过内置中继稳定访问 Gemini
- 用自备 API 密钥进行私密 AI 对话并多端同步

## 场景标签

`聊天机器人` `图像生成` `科研工具` · 领域:对话与助手

## 证据(README 行号)

> L14: This project is built using **Google Gemini API** for conversational AI interactions, providing an intelligent AI e
> L58: > LittleAIBox is a full-stack, cross-platform Gemini AI chat application (built with Vite/Capacitor/Cloudflare) fea
> L68: > Unlike traditional AI applications, LittleAIBox runs locally, ensuring your files and messages never leave your d

## 星数曲线

```mermaid
xychart-beta
    title "diandiancha/LittleAIBox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-26 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a8e3f76d3746` · [字段定义](../../DATASET.md)*
