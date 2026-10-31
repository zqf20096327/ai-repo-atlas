# OnlyTerp/windows-is-fine-for-llms

⭐ 14 · PowerShell · MIT · 推送 2026-06-02 · [GitHub](https://github.com/OnlyTerp/windows-is-fine-for-llms) · 个人维护

**Windows 上跑本地大模型的故障排查指南：修 TDR 崩溃与 WSL2 内存问题**

面向在 Windows 11 + NVIDIA 显示 GPU 上运行本地 LLM 的用户的操作手册：定位两类常见问题——加载大模型时 WDDM TDR 超时导致桌面崩溃（调高注册表 TdrDelay 至 20s）、WSL2 内 Blackwell 架构约 16 GiB 隐性 CUDA 上下文开销导致 OOM——并给出注册表与 NVIDIA 设置等可逆修复。推荐工作流留在 WSL2、经 HTTP 调用原生 Windows 的 llama-server.exe 起服务。MIT 许可，接受 PR。作者基于 RTX 5090 日常使用经验撰写，非可安装软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两项可逆修复：注册表调高 TdrDelay 与 NVIDIA 面板两项全局设置
- WSL2 与原生 Windows 起服务的对比表及推荐架构（WSL 工具链 + 原生 Windows 服务）
- 提供 llama-server.exe 的 PowerShell 启动命令示例（-ngl 99、flash attention、8080 端口）
- 区分官方文档与社区经验，引用微软/NVIDIA/ollama/WSL issue 作为出处

## 适用场景

- 在显示 GPU 上加载 20 GB+ 模型时桌面黑屏/崩溃，需要定位与修复
- WSL2 内 cudaMalloc OOM 但显存充足时排查 Blackwell 隐性开销
- 规划 WSL 工作流加原生 Windows 推理服务的本地部署架构

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L12: > **The short version:** The old advice — *"don't run local LLMs on Windows, use Mac or Linux"* — had real reasons 
> L24: - You want to run local LLMs (llama.cpp, Ollama, LM Studio, vLLM, ComfyUI, …) without your desktop crashing or your
> L27: ## The two real problems

## 星数曲线

```mermaid
xychart-beta
    title "OnlyTerp/windows-is-fine-for-llms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b8473c6664d5` · [字段定义](../../DATASET.md)*
