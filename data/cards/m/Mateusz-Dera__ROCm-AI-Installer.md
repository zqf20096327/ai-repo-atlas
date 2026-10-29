# Mateusz-Dera/ROCm-AI-Installer

⭐ 52 · Shell · GPL-3.0 · 推送 2026-10-09 · [GitHub](https://github.com/Mateusz-Dera/ROCm-AI-Installer) · 个人维护

**AMD GPU (ROCm) 上安装各类 AI 应用的 Linux 一键安装脚本集**

面向 Linux + AMD Radeon GPU 用户的 Bash 安装器，通过 Podman 容器按需安装并运行约 17 个 AI 应用，覆盖文本生成（llama.cpp、vLLM、SillyTavern、KoboldCPP、Strata）、图像/视频生成（ComfyUI、Krea 2）、音乐（ACE-Step）、语音、3D 生成等类别。安装器读取 GPU 架构预选 ROCm 包，每个应用固定到指定显卡（HIP_VISIBLE_DEVICES）。所有应用在 24GB VRAM 显卡上测试，更低显存可能不可用；仅在单卡环境验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单脚本安装 17 个 ROCm AI 应用（文本/图像/音乐/语音/3D 生成）
- 按 GPU 架构自动预选 ROCm 包构建容器
- 每应用可绑定不同显卡（HIP_VISIBLE_DEVICES 写入 run.sh）
- llama.cpp 与 trellis.cpp 提供 ROCm 或 Vulkan 构建选项

## 适用场景

- AMD 显卡用户在 Linux 上一键部署本地 AI 应用
- 在一台机器的不同显卡上分别运行不同 AI 应用
- 搭建本地文本、图像、语音、3D 生成工具集

## 场景标签

 · 领域:AI 部署工具/AMD GPU 计算

## 证据(README 行号)

> L2: Installation scripts for an AI applications using ROCm on Linux.
> L101: 4\. Clone repository.

## 星数曲线

```mermaid
xychart-beta
    title "Mateusz-Dera/ROCm-AI-Installer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0d237483802a` · [字段定义](../../DATASET.md)*
