# cholletflorentin/Local-IA-Runner

⭐ 3 · C# · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/cholletflorentin/Local-IA-Runner) · 个人维护

**Windows 桌面应用：本地运行 GGUF 对话与图像生成**

基于 WinForms（.NET 10）的 Windows 应用，通过内置的 llama.cpp 引擎运行 GGUF 文本/多模态模型，通过 stable-diffusion.cpp（Vulkan 与 CPU 引擎）生成图像。支持向多模态模型发送图片/音频/视频、子代理与模型工具调用、本地模型论坛、双模型对比、Markdown 渲染与对话保存。安装包与便携版自带推理运行时，无需 Python/.NET/管理员权限；模型文件需另行准备。README 为法语，开发语言标注为 Python（后端仅用标准库）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 llama.cpp（CPU/CUDA）与 stable-diffusion.cpp（Vulkan/CPU）推理引擎
- 支持多模态输入：图片、音频、视频附件（视频按每秒一帧采样）
- 模型工具调用：图像分析（Omni 视觉模型）、图像生成、文件查找/复制/重命名
- 扫描 LM Studio、Jan、GPT4All 等常见本地目录自动发现 GGUF 模型

## 适用场景

- 在 Windows 上本地对话运行 GGUF 模型而无需命令行
- 本地文生图并管理生成的图像文件
- 并排对比两个模型的回答
- 让文本模型调用 Omni 视觉模型分析图片

## 场景标签

`聊天机器人` `图像生成` `推理引擎` · 领域:对话与助手

## 证据(README 行号)

> L3: Application Windows WinForms (.NET 10) pour exécuter des modèles GGUF avec llama.cpp et générer des images avec stab
> L7: - Génération locale à partir de fichiers `.gguf`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `cc8c47bdc775` · [字段定义](../../DATASET.md)*
