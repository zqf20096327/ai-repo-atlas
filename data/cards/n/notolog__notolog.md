# notolog/notolog

⭐ 31 · Python · MIT · 推送 2026-11-14 · [GitHub](https://github.com/notolog/notolog) · [官网](https://notolog.app) · 个人维护

**面向桌面用户的本地优先 Markdown 编辑器，带 AI 助手与 TTS**

基于 Python 与 PySide6 构建的开源 Markdown 编辑器，提供编辑态语法高亮、实时预览、代码块、文件加密（Fernet AES-128 CBC）、19 种语言界面与 6 个内置主题。AI 部分作为可选能力接入三种后端：OpenAI API 云端推理、ONNX Runtime GenAI 本地推理（Phi-3、Llama 等）、llama.cpp 本地 GGUF 模型推理；另支持通过 NeMo-Speech.cpp 与 MagpieTTS 在本地朗读文档或选区。通过 pip/conda/Debian 包分发，跨 Windows/macOS/Linux，编辑器本体最低 4 GB 内存，本地模型另需按模型要求增加内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 助手支持 OpenAI API、ONNX Runtime GenAI 本地推理、llama.cpp GGUF 三种后端
- 本地文本转语音：NeMo-Speech.cpp 与 MagpieTTS，含播放/暂停/停止控制
- 可选文件加密（PBKDF2HMAC + Fernet AES-128 CBC），无遥测或跟踪
- 19 种语言界面、6 个内置主题、跨 Windows/macOS/Linux

## 适用场景

- 在本地离线环境下用 GGUF/ONNX 模型辅助写作 Markdown
- 对笔记文件做可选加密保存
- 本地朗读文档或选中文本

## 场景标签

`AI 助手` `语音合成` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L7: Notolog is an open-source Markdown editor built with Python and PySide6, featuring AI-powered assistance and local-f
> L51: - **AI Assistant** - Supports: OpenAI API, ONNX Runtime GenAI (local), and llama.cpp (local, GGUF models)
> L80: Notolog supports three AI backends:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cfad6d9c3ae1` · [字段定义](../../DATASET.md)*
