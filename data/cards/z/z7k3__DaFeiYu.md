# z7k3/DaFeiYu

⭐ 3 · JavaScript · AGPL-3.0 · 推送 2026-11-18 · [GitHub](https://github.com/z7k3/DaFeiYu) · 个人维护 · 中文 README

**微信 AI 陪伴机器人：群聊回复、记忆与语音/表情消息**

基于 Node.js 与 Python 的本地微信 AI 陪伴机器人，通过 UI 自动化与微信 4.x 桥接，支持群聊 @ 回复、事实记忆与历史压缩、表情包、语音转写与回复、朋友圈读取、每日 Markdown 日记、联网搜索与群管理。所有操作经 Windows 桌面启动器 WhaleLauncher.exe 完成，本地 HTTP API 绑定 127.0.0.1。本仓库为 whale_girl 的改进 fork，叠加双源并行检索、时效强制检索、静默发送、群聊判定仲裁与 RAG 知识库。要求 Windows 10/11、已登录微信 4.x 账号及管理员权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 群聊 @-mention 回复、记忆压缩与拟人化分条发送
- 语音转写（DeepSeek ASR/阿里云）与可选语音回复
- 双源并行联网检索、时效统计强制检索、RAG 知识库（fork 改进）
- 单一启动器完成启动、配置、诊断与更新（SHA256 校验）

## 适用场景

- 在微信群聊中运行一个有记忆的 AI 陪伴机器人
- 让机器人记录私聊事实并写每日日记
- 为机器人接入联网搜索与 RAG 知识库

## 场景标签

`聊天机器人` `RAG` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L17: A local-first AI companion for WeChat. She replies in group chats, remembers what people tell her, and can also sen
> L36: - One model API key: DeepSeek, Zhipu GLM, SiliconFlow, Qwen, Doubao, OpenCode, or any OpenAI-compatible endpoint
> L131: - The bridge uses UI automation and reads the local WeChat database. It does not patch WeChat or inject code, but 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `caf8e50264e1` · [字段定义](../../DATASET.md)*
