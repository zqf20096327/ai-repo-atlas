# gegewu26-source/Onvyra-Releases

⭐ 3 · Kotlin · AGPL-3.0 · 推送 2026-11-21 · [GitHub](https://github.com/gegewu26-source/Onvyra-Releases) · [官网](https://github.com/gegewu26-source/Onvyra-Releases/releases/latest) · 个人维护 · 中文 README

**Android 本地 AI 客户端：多模型对话、手机操控与文件工作区**

原生 Android 应用，让用户与自带的模型服务对话：用户提供 API key、自托管网关或兼容代理，应用在其上提供多模型聊天（长对话上下文压缩）、网页搜索与页面读取、PDF 抽取、MCP 服务器、任务级 skills、模型可读写的沙箱工作区，以及可选的手机操控（无线调试/root，逐工具审批）、小说阅读、影视搜索与网盘解析。全部运行在手机本地，无官方账号与后端；内置 web 服务器可在桌面浏览器访问。提供 arm64/x86_64/universal APK，需 Android 8.0+，源码构建需 JDK 24 等工具链。基于 RikkaHub，AGPL-3.0 发行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 provider 接入：任意数量服务，按会话切换模型，长线程上下文压缩
- 内置搜索、页面读取、PDF 抽取、MCP 服务器与任务级 skills
- 可选手机操控（无线调试/root），逐工具审批，默认关闭
- 内置 web 服务器提供 React 界面，局域网内桌面浏览器可用

## 适用场景

- 在手机上用自备 API key 或自托管网关与多个模型对话
- 让模型在本地文件工作区中读写文档并执行任务
- 通过 AI 助手操控 Android 设备功能
- 阅读小说、搜索影视并解析网盘分享链接

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: Onvyra is a native Android app for talking to the AI models you already use. Everything runs on the phone: conversa
> L23: You bring a model service — your own API key, a self-hosted gateway, or a compatible proxy — and the app gives it a
> L29: |**Multi-model chat**|Add any number of providers, pick a model per conversation, switch assistants freely. Long th

## 星数曲线

```mermaid
xychart-beta
    title "gegewu26-source/Onvyra-Releases 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-25 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `007e8e0c1f5f` · [字段定义](../../DATASET.md)*
