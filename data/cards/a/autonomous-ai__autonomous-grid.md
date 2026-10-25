# autonomous-ai/autonomous-grid

⭐ 269 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/autonomous-ai/autonomous-grid) · [官网](https://www.autonomous.ai/grid) · 组织维护

**把多台自有电脑组成一个 OpenAI 兼容端点的本地推理与训练网格**

Grid 是一个 CLI 工具：在一台电脑上启动网格地址，其余电脑安装引擎（如 llama.cpp）、下载 GGUF 模型后加入网格；请求被路由到持有对应模型的电脑。支持接入已在运行的 Ollama/vLLM/LM Studio 引擎，也支持远程模式连接不同网络的机器。面向拥有多台机器、想本地共享模型算力的开发者与 homelab 用户；另提供桌面应用下载。macOS/Linux 通过 curl 脚本安装，本地默认无需账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多台电脑聚合为单一 OpenAI 兼容端点，按模型路由请求
- 可接入已运行的 Ollama / vLLM / LM Studio 引擎，不替换它们
- grid engine install 按机器自动选择 Metal/Vulkan/CPU 构建
- 支持本地与远程两种模式，模型文件下载一次多机共享

## 适用场景

- 把家里几台电脑的算力组成一个本地推理端点供所有应用调用
- 保留现有 Ollama/vLLM 服务，将其纳入统一路由
- 异地机器通过远程模式加入同一网格

## 场景标签

`模型网关` `推理引擎` `微调` `强化学习` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Grid** puts every computer you own behind one OpenAI-compatible endpoint, and sends each request
> L17: If you already run Ollama, vLLM or LM Studio, keep them — Grid networks them, it does not replace them.
> L226: Grid attaches to any engine that speaks the OpenAI API — Ollama, vLLM and LM Studio among them — so

## 星数曲线

```mermaid
xychart-beta
    title "autonomous-ai/autonomous-grid 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-25"]
    y-axis "stars" 264 --> 270
    line [265, 267, 269, 269]
```

2026-10-18 265 → 2026-10-25 269（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `387097e48f21` · [字段定义](../../DATASET.md)*
