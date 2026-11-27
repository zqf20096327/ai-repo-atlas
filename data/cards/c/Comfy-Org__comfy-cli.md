# Comfy-Org/comfy-cli

⭐ 1,067 · Python · GPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/Comfy-Org/comfy-cli) · [官网](https://docs.comfy.org/comfy-cli/getting-started) · 组织维护

**安装、运行和扩展 ComfyUI 的命令行工具**

comfy-cli 提供 ComfyUI 的终端工作流：一条命令完成 ComfyUI 与 ComfyUI-Manager 的安装与启动，管理自定义节点（安装/更新/快照/二分定位）、从 CivitAI 与 Hugging Face 下载模型、对本地服务器运行工作流，或经 --where cloud 路由到 Comfy Cloud（消耗订阅 credits）。支持 pip/pipx/uv tool 安装，Python 3.10+，跨 Windows/macOS/Linux。命令输出结构化 --json 信封，附带供 Claude/Cursor 驱动 comfy 的技能包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令安装并启动 ComfyUI 与 ComfyUI-Manager
- comfy generate 直接调用合作方图像/视频节点（Flux、Ideogram、DALL·E 等）
- 自定义节点管理：安装、更新、快照、bisect
- 每个命令输出结构化 --json 信封，附带 Claude/Cursor 可用的技能

## 适用场景

- 在终端一站式安装、更新、启动 ComfyUI
- 批量管理 ComfyUI 自定义节点与模型下载
- 无本地 GPU 时将工作流提交到 Comfy Cloud 运行
- 编写脚本或让编程 Agent 驱动 ComfyUI 操作

## 场景标签

 · 领域:开发工具/生成媒体工作流

## 证据(README 行号)

> L10: comfy-cli is a command-line tool for installing, running, and extending
> L22: - 🎨 Direct calls to partner image and video nodes (Flux, Ideogram, DALL·E, Recraft, Reve, Gemini/nano-banana, Kling
> L29: - ☁️ Route any workflow to **Comfy Cloud** with `--where cloud` (no GPU required)

## 星数曲线

```mermaid
xychart-beta
    title "Comfy-Org/comfy-cli 星数(近 24 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 1022 --> 1071
    line [1026, 1027, 1028, 1032, 1034, 1035, 1039, 1042, 1044, 1026, 1048, 1047, 1048, 1049, 1051, 1052, 1053, 1054, 1055, 1056, 1058, 1061, 1066, 1067]
```

2026-10-25 1,026 → 2026-11-27 1,067（+41）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a5c2f728acc2` · [字段定义](../../DATASET.md)*
