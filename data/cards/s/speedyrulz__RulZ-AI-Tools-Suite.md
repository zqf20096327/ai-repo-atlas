# speedyrulz/RulZ-AI-Tools-Suite

⭐ 3 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/speedyrulz/RulZ-AI-Tools-Suite) · 个人维护

**统一安装、更新和启动整套 RulZ AI 桌面工具的 Windows 启动器**

Electron 桌面启动器，集中管理 13 个 RulZ 应用（LoRA 训练器、本地 LLM 套件、图像/视频工具、ComfyUI 启动器等）：以截图与 README 浏览、一键安装（zip/安装包/源码三种方式）、通过 GitHub Releases 检查自身与应用的更新、逐个或批量更新、启动与卸载。每个应用页面自动检查 Python、FFmpeg、Git、NVIDIA GPU、.NET Framework 等前置条件，缺失项经 winget 安装或给分步指引。启动器默认安装包分发，也可从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键安装/更新/启动 13 个应用，含源码分支与 portable zip 多种安装方式
- 自动检查前置条件并经 winget 安装缺失项，GPU 驱动给分步指引
- 每个应用保存配置的 ComfyUI（WSL）多服务器管理与实时日志
- 从 Android 手机经 QR 码下载并远程查看 Coding Agent

## 适用场景

- 在 Windows 上一站式管理整套本地 AI 工具的安装与更新
- 集中启动和监控多个本地 LLM/图像训练工具
- 用 Huggingface Manager 管理模型与数据集的上传下载

## 场景标签

 · 领域:开发工具/AI 工具管理

## 证据(README 行号)

> L5: One launcher for the RulZ apps. Browse every tool with screenshots and its full README, install it with one
> L20: |RulzTrainer|LoRA trainer for nine image models (MOSS-Image, FIBO 2.0, Krea 2, Qwen-Image 2.1, MiniMax-H3-Image and
> L60: - **Prerequisites** (Python, FFmpeg, Git, an NVIDIA GPU, .NET Framework) are checked on each app's page. When you


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8161fbb55297` · [字段定义](../../DATASET.md)*
