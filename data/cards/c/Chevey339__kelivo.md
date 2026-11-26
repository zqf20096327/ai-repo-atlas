# Chevey339/kelivo

⭐ 4,780 · Dart · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/Chevey339/kelivo) · [官网](https://kelivo.psycheas.top) · 个人维护 · 中文 README

**跨平台移动与桌面 LLM 聊天客户端，多模型接入**

Kelivo 是用 Flutter 构建的开源 LLM 客户端，覆盖 Android、iOS、macOS、Windows、Linux 与 HarmonyOS。用户接入自己的 API key 或订阅账号，可在 OpenAI、Gemini、Claude、DeepSeek、OpenRouter 等 OpenAI 兼容服务间切换。除聊天外，模型可调用 MCP 服务器、技能、网络搜索，并可绑定工作区读取/编辑文件与运行命令（手机端经 Linux 沙箱，桌面端经系统 shell）。数据本地存储，无自有账号系统，支持 WebDAV/S3 备份与从 Cherry Studio、Chatbox 导入。

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

- 一套应用接入 OpenAI、Gemini、Claude、DeepSeek、OpenRouter 等及任意 OpenAI 兼容端点
- 工作区为模型提供 8 种文件/终端工具，移动端经 PRoot/iSH 运行 Linux 沙箱
- MCP 服务器连接（Streamable HTTP/SSE/STDIO），支持 OAuth 与按工具审批
- 长期记忆管线、世界书、技能导入与定时任务

## 适用场景

- 在手机和电脑上用一个应用切换多家模型服务
- 让模型在本地工作区里读写文件、执行命令完成任务
- 数据留在本机的私密聊天与 WebDAV/S3 备份
- 为不同助手配置模型、提示词、工具与记忆

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: **An open-source LLM client for mobile and desktop.**
> L26: Kelivo is a cross-platform LLM client built with Flutter for Android, iOS, macOS, Windows and Linux. Connect your o
> L28: Kelivo goes beyond chat. Models can search the web, call MCP servers, follow skills and remember what matters to yo

## 星数曲线

```mermaid
xychart-beta
    title "Chevey339/kelivo 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 4254 --> 4827
    line [4301, 4311, 4325, 4331, 4345, 4355, 4367, 4381, 4386, 4393, 4311, 4464, 4477, 4492, 4507, 4523, 4536, 4539, 4545, 4595, 4662, 4681, 4695, 4712, 4737, 4747, 4780]
```

2026-10-24 4,301 → 2026-11-26 4,780（+479）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `076e5b2ccfcc` · [字段定义](../../DATASET.md)*
