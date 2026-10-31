# jaeseok614/ai-hardware-fit

⭐ 44 · JavaScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/jaeseok614/ai-hardware-fit) · [官网](https://jaeseok614.github.io/ai-hardware-fit/) · 个人维护

**GPU 与 AI 模型适配查询工具：选 GPU 得可跑模型与运行命令**

面向本地推理选型的网页工具：内置 160 种 GPU 预设（含 NVIDIA/AMD/Intel/Apple Silicon/笔记本）与 349 种模型（LLM、嵌入、重排、OCR/VLM、图像、语音），选定 GPU 后给出 3 个可运行模型、推荐量化、VRAM 与速度范围及 Ollama/llama.cpp/vLLM/MLX 运行命令；也支持从模型反查 GPU、批量部署规划与成本估算。结果区分实测与计算估计并链接官方来源，速度为计划用范围非保证值。本地开发需 Node.js 20 以上，npm 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 160 种 GPU 预设 + 349 种模型，含直接规格输入
- 按 Q4_K_M/4K context/llama.cpp 基准计算 VRAM–性能前沿
- 区分实测/实测校正/计算估计四种数值依据并链接来源
- 生成 Ollama/llama.cpp/vLLM/MLX 运行命令与 Docker Compose、Excel、PDF 产出

## 适用场景

- 我的显卡能跑哪些本地模型，选 GPU 直接看推荐和命令
- 按模型、预算、功耗反查合适 GPU
- 规划多模型部署的 GPU 分配与 API/云/自建成本对比

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5:  GPU 하나를 고르면 실행 가능한 AI 모델 3개, 권장 양자화, VRAM·예상 속도와 바로 쓸 수 있는 실행 명령어를 보여줍니다.
> L59: - Ollama, llama.cpp, vLLM, MLX 실행 설정과 명령어

## 星数曲线

```mermaid
xychart-beta
    title "jaeseok614/ai-hardware-fit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-31 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3cb767ced73c` · [字段定义](../../DATASET.md)*
