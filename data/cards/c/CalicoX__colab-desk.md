# CalicoX/colab-desk

⭐ 4 · HTML · MIT · 推送 2026-11-25 · [GitHub](https://github.com/CalicoX/colab-desk) · 个人维护 · 中文 README

**macOS 原生工作台：图形化驱动 google-colab-cli 操作 Colab GPU**

将官方 google-colab-cli 封装为可视化工作台，提供四种驱动 Colab VM 的方式：多 Agent 中心（ACP 协议、Grok NDJSON、OpenAI 兼容 API 多配置）、零 Agent 参数化脚本直跑、手动 CLI 命令、以及基于 xterm.js + PTY 的交互终端。附带 GPU/VRAM 遥测、进程查杀、端口自动转发、云端文件浏览器、Env Vault 密钥管理与本地-云端文件夹同步。零运行时 npm 依赖，支持预编译 macOS app 与本地 Web 应用两种形态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Agent 中心：ACP 协议、Grok 流式聊天、OpenAI 兼容多配置，无需本地 Agent CLI 也可用
- 参数化脚本直跑：{{param}} 占位符自动生成表单，绕过云 LLM 直接在 VM 上运行
- GPU 遥测与端口自动检测转发（ComfyUI/Gradio/Jupyter/Ollama/vLLM 预设）
- 本地存储（0600 权限），凭证不经本产品处理，全部经官方 colab CLI

## 适用场景

- 不想记 CLI 参数，图形化操作 Google Colab GPU 会话
- 一键部署 ComfyUI 并端口转发到本地浏览器
- 通过 AI Agent 调试远程终端输出的报错
- 管理 HF_TOKEN 等密钥并自动注入 Colab VM

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: **A lightweight, native macOS desktop workbench & local web app for the official `google-colab-cli` (`colab`).**
> L14: Colab Desk turns the official `google-colab-cli` (`colab` binary) into a complete visual GPU/TPU workbench. Drive G


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `85dd79b6c92e` · [字段定义](../../DATASET.md)*
