# NingzeXu/lovephone-studio

⭐ 18 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/NingzeXu/lovephone-studio) · 个人维护 · 中文 README

**面向个人的 AI 陪伴小手机 DIY 搭建器（网页/Electron）**

面向个人 DIY 用户的开源开发版工具：在浏览器中搭建包含角色、聊天、记忆、日记、纪念日、音乐等 App 的『小手机』，可自定义主题、图标、小组件与手机壳，通过本机 AI 桥接服务接入 OpenAI/Anthropic/Gemini 等多种模型协议实现 AI 聊天。API Key 用 Windows DPAPI 加密保存，数据存于浏览器 IndexedDB 并支持自动备份；搭建结果可导出为独立 HTML ZIP 部署到静态托管，或用 Electron 生成 Windows 安装包。目前主要支持 Windows，公开安装包前尚有代码签名与内容授权待完成事项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 OpenAI 兼容、Anthropic Messages、Gemini 等协议及 15+ 内置服务商
- 角色/主题/小组件/自定义 App 沙箱化定制，主题包带导入预检与哈希校验
- API Key 由本机桥接用 Windows DPAPI 按用户加密保存
- 可导出独立 HTML ZIP 部署到静态托管，或构建 Electron Windows 桌面版

## 适用场景

- DIY 搭建一台专属 AI 陪伴小手机并日常聊天
- 自定义主题、小组件与手机壳美化自己的小手机
- 将搭建好的小手机导出为网页或 Windows 桌面应用使用

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: 面向个人 DIY 的 AI 陪伴小手机搭建器。
> L92: 4. 点击“连接并测试”，成功后聊天 App 会使用真实模型并流式显示回复。
> L105: 内置服务商包括 OpenAI、Anthropic、Gemini、xAI、DeepSeek、火山引擎方舟 / 豆包、通义千问、Kimi、智谱、MiniMax、腾讯混元、百度千帆、硅基流动、OpenRouter、Ollama，以及自

## 星数曲线

```mermaid
xychart-beta
    title "NingzeXu/lovephone-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `53aa153793db` · [字段定义](../../DATASET.md)*
