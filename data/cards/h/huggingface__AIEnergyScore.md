# huggingface/AIEnergyScore

⭐ 43 · Python · MIT · 推送 2025-12-02 · [GitHub](https://github.com/huggingface/AIEnergyScore) · [官网](https://huggingface.github.io/AIEnergyScore/) · 组织维护

**AI 模型能效基准测试框架：测量并对比模型能耗**

Hugging Face 维护的 AI 能效评测项目：通过 Docker 镜像（内置 optimum-benchmark 与 ai_energy_benchmarks）在 GPU 上对文本/图像生成等任务运行基准测试，输出 GPU_ENERGY_WH.txt 与 GPU_ENERGY_SUMMARY.json 等能耗数据，供模型间能效对比并提交排行榜。支持 pytorch/optimum/vllm 三种后端，支持从 CSV 批量测试多个模型、门控模型自动认证与推理模式开关对比。所提供 Dockerfile 面向 NVIDIA H100-80GB，其他硬件结果暂不与主数据可比。面向需要评测模型能效的开发者与企业。

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

- Docker 化基准测试，输出总能耗与详细指标文件
- pytorch / optimum / vllm 三种基准后端可选
- CSV 配置批量测试多模型并按名称/类别/任务过滤
- 门控模型自动认证（HF CLI 登录或 HF_TOKEN 环境变量）

## 适用场景

- 对比不同大小或不同家族模型的能耗效率
- 批量测试一组模型并汇总到 master_results.csv
- 测试推理模式开/关对能耗的影响并提交排行榜

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Welcome to AI Energy Score! This is an initiative to establish comparable energy efficiency ratings for AI models, h
> L239: |`pytorch` (default)|ai_energy_benchmarks|ai_energy_benchmarks generates load|Local GPU (in container)|Standard AI
> L314: |`requirements.txt`|Runtime dependencies for the Docker container|Installed automatically during `./build.sh`|

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/AIEnergyScore 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-25 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `632e89c657e2` · [字段定义](../../DATASET.md)*
