# JMAN730/opendroid

⭐ 1,227 · Kotlin · NOASSERTION · 推送 2026-10-31 · [GitHub](https://github.com/JMAN730/opendroid) · [官网](https://jman730.github.io/opendroid/) · 个人维护

**Android 全自主 AI 代理：本地/云端 LLM 驱动手机自动化**

运行在 Android 手机上的自主 AI 代理应用：将自然语言指令拆解为多步计划并逐步执行、验证与重规划，通过 Accessibility API 与无障碍树实现系统设置、WhatsApp/Telegram 消息、通话、日历、叫车、UPI 支付等设备控制。内置基于 LiteRT-LM 的本地模型下载与导入管理，支持 13 家 LLM 提供商及自动故障切换，提供离线唤醒词、语音识别与屏幕视觉理解。面向终端用户，从源码用 Gradle 构建，需 JDK 21 与 Android SDK 35。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自规划引擎：任务拆解、依赖跟踪、失败时动态重规划
- LiteRT-LM 本地模型管理：下载、SHA-256 校验、离线导入 .task/.litertlm 文件
- 13 家 LLM 提供商支持与自动故障切换
- 视觉引擎 + 4 层个人知识图谱 + 离线唤醒词语音接口

## 适用场景

- 用一句话让手机代为完成多步任务（查天气、发消息、设闹钟）
- 完全离线运行本地模型执行设备自动化
- 自动挖掘日常 App 使用规律并生成一键例程

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L24: OpenDroid isn't just another chatbot. It's a **fully autonomous AI agent** that lives on your Android phone and act
> L28: OpenDroid will **plan** this as 3 steps, **execute** each one, **verify** the results, and **adapt** if anything fa
> L118: OpenDroid supports **13 LLM providers** with automatic failover:


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `28e823b471e8` · [字段定义](../../DATASET.md)*
