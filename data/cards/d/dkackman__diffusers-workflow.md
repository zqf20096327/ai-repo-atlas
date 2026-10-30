# dkackman/diffusers-workflow

⭐ 18 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/dkackman/diffusers-workflow) · 个人维护

**把 GPU 上的 Diffusers 封装成 agent 可驱动的任务引擎**

将 Hugging Face Diffusers 库包装为以作业方式运行图像/视频/音频生成的引擎，前端提供三套：MCP 服务器（供 Claude Code 等 MCP 客户端调用 65 个工具创作、运行、检查生成）、Web UI（内省真实 pipeline 签名生成表单、画廊即配方、模型管理）和 CLI。工作流为 JSON 步骤文档，支持多工作区共享 GPU；昂贵操作需显式确认。量化与缓存加速由引擎处理，Python 3.10-3.14，支持 CUDA/MPS/CPU。工作流文件经动态导入可执行任意 Python，需按脚本对待。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器暴露 65 个工具，覆盖工作流目录、任务队列、画廊与模型缓存
- Web UI 表单由内省 diffusers pipeline 签名生成，加载前校验 schema 与参数
- run_workflow 等高成本操作需 acknowledged_cost=true 才执行
- 量化（BitsAndBytes/GGUF/TorchAO 等）与多种推理缓存加速、固定种子结果缓存

## 适用场景

- 让 Claude Code 等 agent 直接驱动本机 GPU 做图像/视频生成
- 在浏览器中编辑、复现与二次创作 Diffusers 工作流
- 远程 GPU 机器上跑引擎、笔记本通过 HTTP/MCP 连接

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: diffusers-workflow wraps the Hugging Face Diffusers library
> L9: two front ends on it: an **MCP server**, so Claude Code (or any MCP client)
> L80: Then just ask. The agent has 65 tools covering the whole surface — the

## 星数曲线

```mermaid
xychart-beta
    title "dkackman/diffusers-workflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e3e31f9ca99e` · [字段定义](../../DATASET.md)*
