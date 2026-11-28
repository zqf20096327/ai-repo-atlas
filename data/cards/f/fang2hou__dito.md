# fang2hou/dito

⭐ 3 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/fang2hou/dito) · 个人维护 · 中文 README

**macOS 本地优先语音助手：听写、改写、翻译与会纪转写**

基于 Rust 与 GPUI 构建的 macOS 应用，默认在本地运行模型，历史、音频与模型数据保留在用户机器上，也可按阶段选择云端模型。功能包括快捷键听写并就地润色插入、对选中文本发出语音指令（润色/改写/翻译/摘要/回复/问答）、系统音频与麦克风会议实时转写、以及聊天与 OpenAI 兼容本地 API/MCP 端点。处于早期开发阶段，未发布预编译安装包，需从源码用脚本构建，要求 Apple Silicon Mac 与 macOS 13+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 快捷键语音听写：转写、润色并就地插入光标处
- 离线指令路由：小模型分类器在本地分流语音指令
- 会议转写支持系统音频与麦克风，结束后按上下文逐段润色并生成标题
- OpenAI 兼容 HTTP 端点与 MCP，让本机其他应用复用 Dito 所配模型

## 适用场景

- 在任意应用中按快捷键语音输入并自动润色文本
- 开会时录制系统音频与麦克风获得实时逐段转写
- 选中一段文字用语音下达改写或翻译指令
- 把本地模型通过本地 API 提供给 Mac 上的其他应用使用

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L8: Dito runs local models by default, so your history, audio, and models stay on your Mac.
> L41: Press your shortcut, speak, and press it again. Dito transcribes your speech and inserts the polished text at the c
> L65: Chat uses your selected text model, supports attaching files or completed meeting transcripts, and streams replies 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `79c57e810400` · [字段定义](../../DATASET.md)*
